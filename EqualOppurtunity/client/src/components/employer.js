import React, { useState, useEffect } from 'react';
import axios from 'axios';
import YouTube from 'react-youtube';
import './employer.css';

const API_KEY = 'AIzaSyD2ugkX5d2Tisuz8zlb3oMAVFC7RTXdeFo';
const SEARCH_QUERY = 'unconscious bias in hiring';

const Employer = () => {
  const [videos, setVideos] = useState([]);
  const [showVideoGrid, setShowVideoGrid] = useState(false);
  const [applicationsReview, setApplicationsReview] = useState('');

  const handleResourcesClick = () => {
    setShowVideoGrid(true);
  };

  const handleApplicationsReviewClick = () => {
    setShowVideoGrid(false);
  };

  useEffect(() => {
    axios
      .get(
        `https://www.googleapis.com/youtube/v3/search?key=${API_KEY}&part=snippet&type=video&maxResults=8&q=${SEARCH_QUERY}`
      )
      .then((response) => {
        setVideos(response.data.items);
      })
      .catch((error) => {
        console.error(error);
      });

    axios
      .get('http://127.0.0.1:8001/api/resumes/1/')
      .then((response) => {
        setApplicationsReview(response.data.text);
        console.log ("resume:", response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  return (
    <div className="employer">
      <div className="title-container">
        <h1 className="main-title">Employer Dashboard</h1>
        <div className="clickable-titles-container">
          <h2
            onClick={handleResourcesClick}
            className={`clickable-title ${showVideoGrid ? 'active' : ''}`}
          >
            Resources
          </h2>
          <h2
            onClick={handleApplicationsReviewClick}
            className={`clickable-title ${!showVideoGrid ? 'active' : ''}`}
          >
            Applications Review
          </h2>
        </div>
      </div>
      {showVideoGrid ? (
        <>
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
        </>
      ) : (
        <>
          <h2>Applications Review</h2>
          <div>
            <p>{applicationsReview}</p>
          </div>
        </>
      )}
    </div>
  );
};

export default Employer;
