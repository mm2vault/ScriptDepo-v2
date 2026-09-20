import {useEffect} from 'react';

export default function App() {
  useEffect(() => {
    // The production app is the static ScriptDepo index.html used by GitHub Pages.
    // Keep the Vite entry from rendering a misleading blank screen if opened directly.
    if (window.location.pathname.endsWith('/App.tsx')) window.location.href = './index.html';
  }, []);
  return null;
}
