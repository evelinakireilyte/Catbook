import Card from 'react-bootstrap/Card'
import { useState } from 'react'
import Modal from 'react-bootstrap/Modal'
import * as ReactBootStrap from 'react-bootstrap'

const DocumentCard = ({ title, img, loading }) => {
  const [show, setShow] = useState(false)
  const handleClose = () => setShow(false)
  const handleShow = () => setShow(true)

  return (
    <>
      <div class="card">
        <Card style={{ width: '15rem', padding: '5px' }}>
          <Card.Body>
            <h5 class="card-title text-center">{title}</h5>
          </Card.Body>
          {!loading ? (
            <Card.Img
              style={{ height: '13rem' }}
              onClick={handleShow}
              src={img}
            />
          ) : (
            <div>
              <ReactBootStrap.Spinner animation="border" />
            </div>
          )}
          <Modal
            show={show}
            onHide={handleClose}
            backdrop="static"
            keyboard={true}
            centered
            size="lg"
          >
            <Card.Img
              style={{ height: '40rem' }}
              onClick={handleShow}
              src={img}
            />
          </Modal>
        </Card>
      </div>
    </>
  )
}

export default DocumentCard
