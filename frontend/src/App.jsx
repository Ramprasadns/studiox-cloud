import React from 'react'
import Welcome from './components/Welcome'
export default function App(){
  return (
    <div className="app-shell">
      <header className="app-header">
        <div className="logo">StudioX Cloud</div>
        <div className="tag">Turn Stories into Stunning AI Narration Videos</div>
      </header>
      <main className="app-main">
        <Welcome />
      </main>
    </div>
  )
}
