import { useState, useEffect } from 'react'
import DocumentCard from '../components/DocumentCard'
import CountDownTimer from '../components/CountDownTimer'
import { fetchDocuments } from '../helpers/api'
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd'

const DocumentList = () => {
  const [documents, setDocuments] = useState([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const getDocumentCards = async () => {
      setLoading(true)
      const allDocs = await fetchDocuments()
      setDocuments(allDocs)
      setInterval(() => {
        setLoading(true)
        fetchDocuments().then(setDocuments)
        // Unnecessary timeout to demonstrate loading
        setTimeout(() => setLoading(false), 500)
      }, 300000)

      // Unnecessary timeout to demonstrate loading
      setTimeout(() => setLoading(false), 500)
    }
    getDocumentCards()
  }, [])

  function handleOnDragEnd(result) {
    const items = Array.from(documents)
    const [reorderItem] = items.splice(result.source.index, 1)
    items.splice(result.destination.index, 0, reorderItem)
    console.log(result)
    setDocuments(items)
  }

  return (
    <>
      <div className="wrapper">
        <h1 class="header text-center">Catbook</h1>
        <CountDownTimer />
        <DragDropContext onDragEnd={handleOnDragEnd}>
          <Droppable droppableId="docs">
            {(provided) => (
              <ul {...provided.droppableProps} ref={provided.innerRef}>
                {documents.map((item, index) => {
                  return (
                    <Draggable
                      key={item.id}
                      draggableId={item.title}
                      index={index}
                    >
                      {(provided) => (
                        <li
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                          ref={provided.innerRef}
                        >
                          <div style={{ padding: '15px' }}>
                            <DocumentCard {...item} loading={loading} />
                          </div>
                        </li>
                      )}
                    </Draggable>
                  )
                })}
                {provided.placeholder}
              </ul>
            )}
          </Droppable>
        </DragDropContext>
      </div>
    </>
  )
}

export default DocumentList
