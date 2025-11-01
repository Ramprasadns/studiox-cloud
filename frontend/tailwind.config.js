export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        neon: '#3b82f6'
      },
      backgroundImage: {
        'dark-grad': 'linear-gradient(180deg,#020617 0%, #0f172a 100%)'
      },
      boxShadow: {
        'neon-glow': '0 6px 30px rgba(59,130,246,0.18), 0 0 20px rgba(59,130,246,0.08)'
      }
    }
  },
  plugins: []
}
