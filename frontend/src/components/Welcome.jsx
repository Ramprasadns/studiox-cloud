import React from 'react'
export default function Welcome(){
  return (
    <div>
      <h2 style={{marginTop:0}}>Welcome to StudioX Cloud</h2>
      <p style={{color:'#bcdff6'}}>This is a minimal, deploy-ready frontend. Click generate after backend is live.</p>
      <div style={{marginTop:16}}>
        <button style={{padding:'10px 16px',background:'linear-gradient(90deg,#7b61ff,#4fd1c5)',border:'none',borderRadius:8,color:'#fff',cursor:'pointer'}}>Generate Sample Video</button>
      </div>
    </div>
  )
}
