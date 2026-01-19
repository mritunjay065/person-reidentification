import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FiArrowRight, FiPlay, FiX, FiBook } from 'react-icons/fi';
import './Hero.css';

const Hero = () => {
  const [showDocs, setShowDocs] = useState(false);
  const [showDemo, setShowDemo] = useState(false);

  return (
    <section className="hero">
      <div className="container">
        <div className="hero-content">
          <motion.div
            className="hero-badge"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <span className="badge-dot"></span>
            <span>AI-Powered Identity Recognition</span>
          </motion.div>

          <motion.h1
            className="hero-title"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2 }}
          >
            Advanced
            <span className="gradient-text"> Person </span>
            <br />
            Re-Identification
          </motion.h1>

          <motion.p
            className="hero-description"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.4 }}
          >
            Cutting-edge AI system for real-time face recognition and person
            re-identification. Using deep learning models like SFace and YuNet
            for accurate identity matching across camera feeds.
          </motion.p>

          <motion.div
            className="hero-buttons"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.6 }}
          >
            <button className="btn-primary" onClick={() => setShowDocs(true)}>
              Get Started
              <FiArrowRight />
            </button>
            <button className="btn-secondary" onClick={() => setShowDemo(true)}>
              <FiPlay />
              Watch Demo
            </button>
          </motion.div>

          <motion.div
            className="hero-stats"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 1, delay: 0.8 }}
          >
            <div className="stat">
              <span className="stat-value">99.5%</span>
              <span className="stat-label">Accuracy</span>
            </div>
            <div className="stat-divider"></div>
            <div className="stat">
              <span className="stat-value">&lt;50ms</span>
              <span className="stat-label">Latency</span>
            </div>
            <div className="stat-divider"></div>
            <div className="stat">
              <span className="stat-value">Real-Time</span>
              <span className="stat-label">Processing</span>
            </div>
          </motion.div>
        </div>

        <motion.div
          className="hero-visual"
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 1, delay: 0.4 }}
        >
          <div className="visual-container">
            <div className="face-scan-effect">
              <div className="scan-line"></div>
              <div className="face-grid"></div>
              <div className="face-points">
                {[...Array(12)].map((_, i) => (
                  <motion.div
                    key={i}
                    className="face-point"
                    style={{
                      left: `${20 + (i % 4) * 20}%`,
                      top: `${20 + Math.floor(i / 4) * 25}%`,
                    }}
                    animate={{
                      scale: [1, 1.5, 1],
                      opacity: [0.5, 1, 0.5],
                    }}
                    transition={{
                      duration: 2,
                      delay: i * 0.1,
                      repeat: Infinity,
                    }}
                  />
                ))}
              </div>
              <div className="recognition-box">
                <span className="recognition-label">Identity Verified</span>
                <span className="recognition-score">Confidence: 98.7%</span>
              </div>
            </div>
          </div>
        </motion.div>
      </div>

      {/* Documentation Modal */}
      <AnimatePresence>
        {showDocs && (
          <motion.div
            className="modal-overlay"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setShowDocs(false)}
          >
            <motion.div
              className="modal-content docs-modal"
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.8, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
            >
              <button className="modal-close" onClick={() => setShowDocs(false)}>
                <FiX />
              </button>

              <div className="modal-header">
                <FiBook className="modal-icon" />
                <h2>Getting Started Guide</h2>
              </div>

              <div className="modal-body">
                <div className="doc-section">
                  <h3>🚀 Quick Start</h3>
                  <div className="code-block">
                    <code>cd person-reidentification</code>
                    <code>.\start_app.bat</code>
                  </div>
                  <p>This will start both the backend server and frontend automatically!</p>
                </div>

                <div className="doc-section">
                  <h3>🧠 Neural Networks Used</h3>
                  <ul>
                    <li><strong>YuNet CNN</strong> - Lightweight Convolutional Neural Network for face detection</li>
                    <li><strong>SFace ResNet</strong> - Deep neural network for face recognition (128D embeddings)</li>
                    <li><strong>ONNX Runtime</strong> - Optimized model inference</li>
                  </ul>
                </div>

                <div className="doc-section">
                  <h3>📋 How to Use Person Re-ID</h3>
                  <ol>
                    <li>Click on <strong>"Launch Project"</strong> in the Projects section</li>
                    <li>Allow camera access when prompted</li>
                    <li>Press <strong>1-9</strong> to register a person's face</li>
                    <li>Press <strong>R</strong> to toggle Re-ID mode</li>
                    <li>The system will identify registered faces in real-time!</li>
                  </ol>
                </div>

                <div className="doc-section">
                  <h3>🧙 Harry Potter Invisible Cloak</h3>
                  <p>A fun computer vision project that makes you invisible using color detection!</p>
                  <ul>
                    <li><strong>How it works:</strong> Uses HSV color space to detect a specific color (like green/red cloth)</li>
                    <li><strong>Technology:</strong> OpenCV morphological operations and background subtraction</li>
                    <li><strong>Steps:</strong></li>
                  </ul>
                  <ol>
                    <li>Click <strong>"Launch Project"</strong> for Harry Potter Cloak</li>
                    <li>Click on the cloth color you want to make invisible</li>
                    <li>The system captures the background</li>
                    <li>Hold the cloth in front of you - it becomes invisible!</li>
                    <li>Press <strong>Q</strong> to quit</li>
                  </ol>
                </div>

                <div className="doc-section">
                  <h3>⌨️ Keyboard Controls</h3>
                  <div className="controls-grid">
                    <div className="control-item">
                      <kbd>1-9</kbd>
                      <span>Register person</span>
                    </div>
                    <div className="control-item">
                      <kbd>R</kbd>
                      <span>Toggle Re-ID mode</span>
                    </div>
                    <div className="control-item">
                      <kbd>D</kbd>
                      <span>Toggle debug scores</span>
                    </div>
                    <div className="control-item">
                      <kbd>C</kbd>
                      <span>Clear gallery</span>
                    </div>
                    <div className="control-item">
                      <kbd>S</kbd>
                      <span>Save gallery</span>
                    </div>
                    <div className="control-item">
                      <kbd>+/-</kbd>
                      <span>Adjust threshold</span>
                    </div>
                    <div className="control-item">
                      <kbd>Q</kbd>
                      <span>Quit</span>
                    </div>
                  </div>
                </div>

                <div className="doc-section">
                  <h3>🔧 Requirements</h3>
                  <ul>
                    <li>Python 3.8+ with virtual environment</li>
                    <li>OpenCV, NumPy (auto-installed)</li>
                    <li>Webcam or camera device</li>
                    <li>Node.js for frontend (optional)</li>
                  </ul>
                </div>
              </div>

              <div className="modal-footer">
                <a href="#projects" className="btn-primary" onClick={() => setShowDocs(false)}>
                  Go to Projects
                  <FiArrowRight />
                </a>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Demo Modal */}
      <AnimatePresence>
        {showDemo && (
          <motion.div
            className="modal-overlay"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setShowDemo(false)}
          >
            <motion.div
              className="modal-content demo-modal"
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.8, opacity: 0 }}
              onClick={(e) => e.stopPropagation()}
            >
              <button className="modal-close" onClick={() => setShowDemo(false)}>
                <FiX />
              </button>

              <div className="modal-header">
                <FiPlay className="modal-icon" />
                <h2>Person Re-ID Demo</h2>
              </div>

              <div className="modal-body">
                <div className="demo-video-placeholder">
                  <div className="demo-preview">
                    <FiPlay className="play-icon" />
                    <p>Interactive Demo</p>
                  </div>
                </div>

                <div className="demo-description">
                  <h3>What You'll See:</h3>
                  <ul>
                    <li>✅ Real-time face detection using YuNet CNN</li>
                    <li>✅ Face recognition with SFace deep learning model</li>
                    <li>✅ Identity matching with confidence scores</li>
                    <li>✅ Multi-person tracking across frames</li>
                  </ul>
                </div>

                <div className="demo-steps">
                  <h3>Demo Workflow:</h3>
                  <div className="demo-step">
                    <span className="step-num">1</span>
                    <div>
                      <strong>Register Identities</strong>
                      <p>Press 1-9 to register different people</p>
                    </div>
                  </div>
                  <div className="demo-step">
                    <span className="step-num">2</span>
                    <div>
                      <strong>Enable Re-ID Mode</strong>
                      <p>Press R to start real-time identification</p>
                    </div>
                  </div>
                  <div className="demo-step">
                    <span className="step-num">3</span>
                    <div>
                      <strong>See Results</strong>
                      <p>Watch as the system identifies faces with confidence scores</p>
                    </div>
                  </div>
                </div>
              </div>

              <div className="modal-footer">
                <a href="#projects" className="btn-primary" onClick={() => setShowDemo(false)}>
                  Try It Yourself
                  <FiArrowRight />
                </a>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
};

export default Hero;
