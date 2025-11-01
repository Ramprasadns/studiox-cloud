import React from 'react'
import { API_BASE } from './config'
import { motion } from 'framer-motion'

export default function App(){
  const [loading, setLoading] = React.useState(false)
  const [msg, setMsg] = React.useState(null)

  async function generate(){
    setLoading(true); setMsg(null)
    try {
      const res = await fetch(`${API_BASE}/api/sample`)
      const data = await res.json()
      setMsg(data.sample_story ?? JSON.stringify(data))
    } catch(e){
      setMsg('Error: ' + e.message)
    } finally { setLoading(false) }
  }

  return (
    <div className="min-h-screen flex items-start justify-center p-8">
      <div className="card max-w-3xl w-full">
        <header className="flex items-center gap-4">
          <div style={{width:60,height:60, borderRadius:12, background:'linear-gradient(135deg,#7b61ff,#3b82f6)'}} />
          <div>
            <h1 className="text-2xl font-semibold">StudioX Cloud — Preview</h1>
            <div className="small-muted">Turn Stories into Stunning AI Narration Videos</div>
          </div>
        </header>

        <hr className="my-6 border-gray-700"/>

        <main>
          <h3 className="text-xl font-semibold mb-2">Sample Stories (preloaded)</h3>
          <ol className="pl-5 list-decimal space-y-1 text-white/90">
            <li>The Pebble Path — <em>Click Generate to create a sample video</em></li>
            <li>Rise of Anu</li>
            <li>The Box of Dreams</li>
          </ol>

          <div className="mt-6">
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              onClick={generate}
              disabled={loading}
              className="btn-neon"
            >
              {loading ? 'Generating…' : 'Generate Sample Video'}
            </motion.button>
          </div>

          {msg && (
            <div className="mt-6 p-4 bg-white/5 rounded">
              <div className="text-sm small-muted">Result</div>
              <div className="mt-2 text-white">{String(msg)}</div>
            </div>
          )}

          <div className="mt-8">
            <h4 className="font-semibold">Admin</h4>
            <div className="small-muted">Super Admin email: <strong className="text-white">ramaigen2025@gmail.com</strong></div>
          </div>

        </main>
      </div>
    </div>
  )
}
