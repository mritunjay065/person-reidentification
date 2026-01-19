import React from 'react';
import { motion } from 'framer-motion';
import { FiGithub, FiLinkedin, FiMail, FiHeart } from 'react-icons/fi';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer" id="footer">
      <div className="container">
        <div className="footer-content">
          <motion.div
            className="footer-brand"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <div className="footer-logo">
              <svg viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="20" cy="12" r="8" stroke="url(#gradient2)" strokeWidth="2" fill="none"/>
                <path d="M8 35c0-8 5-12 12-12s12 4 12 12" stroke="url(#gradient2)" strokeWidth="2" fill="none"/>
                <defs>
                  <linearGradient id="gradient2" x1="0" y1="0" x2="40" y2="40">
                    <stop offset="0%" stopColor="#00ff88"/>
                    <stop offset="100%" stopColor="#00d4ff"/>
                  </linearGradient>
                </defs>
              </svg>
              <span>Person<span className="gradient-text">Re-ID</span></span>
            </div>
            <p className="footer-tagline">
              Advanced AI-powered person re-identification system built with 
              OpenCV, deep learning, and computer vision technologies.
            </p>
          </motion.div>

          <motion.div
            className="footer-links"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
          >
            <h4>Quick Links</h4>
            <a href="#features">Features</a>
            <a href="#how-it-works">How It Works</a>
            <a href="#projects">Projects</a>
          </motion.div>

          <motion.div
            className="footer-tech"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
          >
            <h4>Technologies</h4>
            <span>Python & OpenCV</span>
            <span>YuNet & SFace</span>
            <span>Deep Learning</span>
            <span>React.js</span>
          </motion.div>

          <motion.div
            className="footer-contact"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.3 }}
          >
            <h4>Connect</h4>
            <div className="social-links">
              <a href="#" className="social-link" aria-label="GitHub">
                <FiGithub />
              </a>
              <a href="#" className="social-link" aria-label="LinkedIn">
                <FiLinkedin />
              </a>
              <a href="#" className="social-link" aria-label="Email">
                <FiMail />
              </a>
            </div>
          </motion.div>
        </div>

        <div className="footer-bottom">
          <p>
            Made with <FiHeart className="heart-icon" /> for Computer Vision
          </p>
          <p className="copyright">
            © 2026 Person Re-ID Project. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
