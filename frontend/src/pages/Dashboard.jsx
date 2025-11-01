import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { API_BASE } from '../config';

export default function Dashboard(){
  const [status, setStatus] = useState(null);
  const [sample, setSample] = useState(null);

  useEffect(()=> {
    fetch(`${API_BASE}/api/health`).then(r=> r.json()).then(setStatus).catch(()=>setStatus(null));
    fetch(`${API_BASE}/api/sample`).then(r=> r.json()).then(setSample).catch(()=>setSample(null));
  },[]);

  async function generateSample(){
    try {
      const res = await fetch(`${API_BASE}/api/sample`);
      const data = await res.json();
      setSample(data);
    } catch(e){}
  }

  return (
    <motion.div initial={{opacity:0, y:8}} animate={{opacity:1, y:0}} className="card max-w-3xl w-full">
      <header className="flex items-center gap-4 mb-6">
        <div style={{width:56,height:56, borderRadius:12, background:'linear-gradient(135deg,#7b61ff,#ffb86b)'}}/>
        <div>
          <h1 className="text-2xl font-semibold">StudioX Cloud — Preview</h1>
          <div className="text-sm" style={{color:'rgba(255,255,255,0.7)'}}>Turn Stories into Visual Magic</div>
        </div>
      </header>

      <div className="space-y-6">
        <section>
          <h3 className="text-lg font-medium">Sample Stories (preloaded)</h3>
          <ol className="mt-2 list-decimal list-inside" style={{color:'var(--muted)'}}>
            <li>The Pebble Path — <em>Click Generate to create a sample video</em></li>
            <li>Rise of Anu</li>
            <li>The Box of Dreams</li>
          </ol>

          <div className="mt-4">
            <button onClick={generateSample} className="btn-primary">Generate Sample Video</button>
          </div>
        </section>

        <section>
          <h3 className="text-md font-semibold">Status</h3>
          <div style={{color:'var(--muted)'}} className="mt-2">
            {status ? <pre style={{whiteSpace:'pre-wrap'}}>{JSON.stringify(status)}</pre> : <span>Backend unreachable</span>}
            {sample && <div className="mt-2 p-3 rounded-md" style={{background:'rgba(0,0,0,0.25)'}}><strong>Sample:</strong> {sample.sample_story || JSON.stringify(sample)}</div>}
          </div>
        </section>

        <footer style={{color:'var(--muted)'}}>This is a preview UI. Replace with full product later.</footer>
      </div>
    </motion.div>
  );
}
