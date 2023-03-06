import React from 'react';
import YouTube from 'react-youtube';
import './employer.css';

const videoId = 'QbK4Ge8zgF8';

const opts = {
  height: '100%',
  width: '100%',
  playerVars: {
    autoplay: 0,
  },
};

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Resources</h1>
        <h2>Unconscious Bias in Hiring</h2>
      </header>
      <div className="Video-grid">
  {[...Array(5)].map((_, i) => (
    <div className="video-thumbnail" key={i}>
      <h3>Video {i + 1}</h3>
      <div className="video-wrapper">
        <iframe src={`https://www.youtube.com/embed/${videoId}`} frameborder="0" allowfullscreen></iframe>
      </div>
    </div>
  ))}
</div>
    </div>
  );
}

export default App;
