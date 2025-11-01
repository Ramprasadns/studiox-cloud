import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// Vite configuration optimized for Render
export default defineConfig({
  plugins: [react()],
  root: '.', // main project folder
  base: './', // ensures correct relative asset paths
  build: {
    outDir: 'dist',          // output build to frontend/dist
    emptyOutDir: true,       // clear previous build files
    assetsDir: 'assets',     // folder for static assets
    sourcemap: false,        // disable maps in production
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: true,              // required for Render’s preview builds
    port: 5173,
    open: false,
  },
  preview: {
    port: 4173,
  },
})
