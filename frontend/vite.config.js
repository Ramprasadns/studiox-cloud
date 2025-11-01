import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// Vite configuration
export default defineConfig({
  plugins: [react()],
  root: '.', // ensures correct relative paths for subfolder builds
  base: './', // ensures static files load correctly after deployment
  build: {
    outDir: 'dist',
    emptyOutDir: true, // clears dist before rebuild
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 5173,
    open: true,
  },
})
