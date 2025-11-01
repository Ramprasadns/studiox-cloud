export default {
  content: ['./index.html', './src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: '#7b61ff',
        accent: '#ffb86b'
      },
      boxShadow: {
        glow: '0 8px 30px rgba(123,97,255,0.22), 0 2px 6px rgba(0,0,0,0.2)'
      }
    }
  },
  plugins: []
};
