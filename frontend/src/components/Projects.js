import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FiCamera, FiUser, FiPlay, FiSquare, FiCheck, FiX, FiLoader } from 'react-icons/fi';
import api from '../api';
import './Projects.css';

const Projects = () => {
  const [serverStatus, setServerStatus] = useState('checking');
  const [processStatus, setProcessStatus] = useState({});
  const [launching, setLaunching] = useState({});
  const [notification, setNotification] = useState(null);

  // Check server status on mount and periodically
  useEffect(() => {
    checkStatus();
    const interval = setInterval(checkStatus, 3000);
    return () => clearInterval(interval);
  }, []);

  const checkStatus = async () => {
    const status = await api.getStatus();
    if (status.server === 'online') {
      setServerStatus('online');
      setProcessStatus(status.processes || {});
    } else {
      setServerStatus('offline');
    }
  };

  const showNotification = (message, type = 'success') => {
    setNotification({ message, type });
    setTimeout(() => setNotification(null), 4000);
  };

  const handleLaunchReID = async () => {
    if (processStatus.reid === 'running') {
      setLaunching(prev => ({ ...prev, reid: true }));
      const result = await api.stopProject('reid');
      if (result.success) {
        showNotification('Person Re-ID stopped', 'info');
      } else {
        showNotification(result.message, 'error');
      }
      setLaunching(prev => ({ ...prev, reid: false }));
    } else {
      setLaunching(prev => ({ ...prev, reid: true }));
      const result = await api.launchReID();
      if (result.success) {
        showNotification('🚀 Person Re-ID launched! Check the new window.', 'success');
      } else {
        showNotification(result.message, 'error');
      }
      setLaunching(prev => ({ ...prev, reid: false }));
    }
    checkStatus();
  };

  const handleLaunchCloak = async () => {
    if (processStatus.cloak === 'running') {
      setLaunching(prev => ({ ...prev, cloak: true }));
      const result = await api.stopProject('cloak');
      if (result.success) {
        showNotification('Harry Potter Cloak stopped', 'info');
      } else {
        showNotification(result.message, 'error');
      }
      setLaunching(prev => ({ ...prev, cloak: false }));
    } else {
      setLaunching(prev => ({ ...prev, cloak: true }));
      const result = await api.launchCloak();
      if (result.success) {
        showNotification('🧙 Harry Potter Cloak launched! Check the new window.', 'success');
      } else {
        showNotification(result.message, 'error');
      }
      setLaunching(prev => ({ ...prev, cloak: false }));
    }
    checkStatus();
  };

  const projects = [
    {
      id: 'reid',
      icon: <FiUser />,
      title: 'Person Re-Identification',
      description: 'Real-time face recognition system using SFace deep learning model. Register identities and track people across camera feeds with high accuracy.',
      features: ['YuNet Face Detection', 'SFace Recognition', 'Persistent Gallery', 'Real-time Processing'],
      gradient: 'linear-gradient(135deg, #00ff88, #00cc6a)',
      onLaunch: handleLaunchReID,
      status: processStatus.reid,
    },
    {
      id: 'cloak',
      icon: <FiCamera />,
      title: 'Harry Potter Invisible Cloak',
      description: 'Magic invisibility effect using computer vision. Click to select a color and watch it become invisible with real-time background replacement.',
      features: ['HSV Color Detection', 'Background Capture', 'Morphological Operations', 'Live Video Effect'],
      gradient: 'linear-gradient(135deg, #00d4ff, #0099cc)',
      onLaunch: handleLaunchCloak,
      status: processStatus.cloak,
    },
  ];

  return (
    <section className="projects" id="projects">
      {/* Notification */}
      <AnimatePresence>
        {notification && (
          <motion.div
            className={`notification ${notification.type}`}
            initial={{ opacity: 0, y: -50, x: '-50%' }}
            animate={{ opacity: 1, y: 0, x: '-50%' }}
            exit={{ opacity: 0, y: -50, x: '-50%' }}
          >
            {notification.type === 'success' && <FiCheck />}
            {notification.type === 'error' && <FiX />}
            {notification.type === 'info' && <FiSquare />}
            <span>{notification.message}</span>
          </motion.div>
        )}
      </AnimatePresence>

      <div className="container">
        <motion.div
          className="section-header"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <h2 className="section-title">
            Our <span className="gradient-text">Projects</span>
          </h2>
          <p className="section-subtitle">
            Two powerful computer vision applications built with OpenCV and Python
          </p>
          
          {/* Server Status Indicator */}
          <div className={`server-status ${serverStatus}`}>
            <span className="status-dot"></span>
            <span>
              {serverStatus === 'online' ? 'Backend Server Online' : 
               serverStatus === 'offline' ? 'Backend Server Offline - Start it first!' : 
               'Checking server...'}
            </span>
          </div>
        </motion.div>

        <div className="projects-grid">
          {projects.map((project, index) => (
            <motion.div
              key={index}
              className={`project-card glass-card ${project.status === 'running' ? 'running' : ''}`}
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.2 }}
              whileHover={{ y: -10 }}
            >
              {project.status === 'running' && (
                <div className="running-indicator">
                  <span className="pulse-dot"></span>
                  Running
                </div>
              )}
              
              <div className="project-icon" style={{ background: project.gradient }}>
                {project.icon}
              </div>
              <h3 className="project-title">{project.title}</h3>
              <p className="project-description">{project.description}</p>
              <div className="project-features">
                {project.features.map((feature, i) => (
                  <span key={i} className="project-feature">{feature}</span>
                ))}
              </div>
              
              <motion.button
                className={`project-btn ${project.status === 'running' ? 'stop' : 'launch'}`}
                onClick={project.onLaunch}
                disabled={serverStatus !== 'online' || launching[project.id]}
                whileHover={{ scale: serverStatus === 'online' ? 1.05 : 1 }}
                whileTap={{ scale: 0.95 }}
              >
                {launching[project.id] ? (
                  <>
                    <FiLoader className="spinner" />
                    {project.status === 'running' ? 'Stopping...' : 'Launching...'}
                  </>
                ) : project.status === 'running' ? (
                  <>
                    <FiSquare />
                    Stop Project
                  </>
                ) : (
                  <>
                    <FiPlay />
                    Launch Project
                  </>
                )}
              </motion.button>
            </motion.div>
          ))}
        </div>

        <motion.div
          className="launch-section"
          initial={{ opacity: 0 }}
          whileInView={{ opacity: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8, delay: 0.4 }}
        >
          <div className="launch-content glass-card">
            <h3>How to Start</h3>
            <p>Start the backend server first, then click Launch Project buttons above</p>
            <div className="launch-commands">
              <div className="command-block">
                <span className="command-label">1. Start Backend:</span>
                <code>cd backend && python app.py</code>
              </div>
              <div className="command-block">
                <span className="command-label">2. Start Frontend:</span>
                <code>cd frontend && npm start</code>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default Projects;
