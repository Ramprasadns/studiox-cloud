import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// base can be left default since we will copy built files to public root
export default defineConfig({
  plugins: [react()],
})
