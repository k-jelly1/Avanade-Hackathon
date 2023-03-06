import React, { useState, useEffect } from 'react';
import axios from 'axios';
import YouTube from 'react-youtube';
import './employer.css';

const API_KEY = '';
const SEARCH_QUERY = 'unconscious bias in hiring';

const Employer = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    axios.get(`https://www.googleapis.com/youtube/v3/search?key=${API_KEY}&part=snippet&type=video&maxResults=8&q=${SEARCH_QUERY}`)
      .then((response) => {
        setVideos(response.data.items);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div className="employer">
      <h1>Resources</h1>
      <h2>Unconscious Bias in Hiring</h2>
      <div className="video-grid">
        {videos.map((video) => (
          <div className="video-thumbnail" key={video.id.videoId}>
            <h3>{video.snippet.title}</h3>
            <div className="video-wrapper">
              <YouTube videoId={video.id.videoId} />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Employer;
