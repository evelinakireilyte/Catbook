import './App.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import DocumentList from './pages/DocumentList'

function App() {
  return (
    <div>
      <BrowserRouter>
        <main>
          <Routes>
            <Route path="/" element={<DocumentList />} />
          </Routes>
        </main>
      </BrowserRouter>
    </div>
  )
}

export default App
