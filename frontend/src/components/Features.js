import React from 'react';
import { motion } from 'framer-motion';
import { FiCpu, FiEye, FiShield, FiZap, FiDatabase, FiLayers } from 'react-icons/fi';
import './Features.css';

const Features = () => {
  const features = [
    {
      icon: <FiEye />,
      title: 'YuNet CNN',
      subtitle: 'Face Detection',
      description: 'Lightweight Convolutional Neural Network (CNN) for real-time face detection. Uses ONNX model for fast inference.',
      tags: ['CNN', 'ONNX', 'Real-time'],
    },
    {
      icon: <FiCpu />,
      title: 'SFace Deep Network',
      subtitle: 'Face Recognition',
      description: 'ResNet-based deep neural network that generates 128-dimensional face embeddings for identity matching.',
      tags: ['ResNet', 'Deep Learning', '128D Embeddings'],
    },
    {
      icon: <FiZap />,
      title: 'Real-Time Processing',
      subtitle: 'Performance',
      description: 'Lightning-fast recognition with sub-50ms latency for seamless live video stream analysis.',
      tags: ['<50ms', 'GPU Optimized', 'Live Feed'],
    },
    {
      icon: <FiShield />,
      title: 'Cosine Similarity',
      subtitle: 'Matching Algorithm',
      description: '99.5% accuracy using cosine similarity matching between face embeddings with optimized thresholds.',
      tags: ['99.5% Accuracy', 'Threshold: 0.363'],
    },
    {
      icon: <FiDatabase />,
      title: 'Persistent Gallery',
      subtitle: 'Storage',
      description: 'Save and load identity galleries with pickle serialization for long-term identity storage.',
      tags: ['Pickle', 'Persistent', 'Multi-User'],
    },
    {
      icon: <FiLayers />,
      title: 'Multi-Embedding',
      subtitle: 'Robustness',
      description: 'Register multiple embeddings per person for improved matching across expressions and angles.',
      tags: ['Multi-pose', 'Expressions', 'Lighting'],
    },
  ];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 30 },
    visible: { opacity: 1, y: 0 },
  };

  return (
    <section className="features" id="features">
      <div className="container">
        <motion.div
          className="section-header"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <span className="section-badge">AI-Powered</span>
          <h2 className="section-title">
            Neural Network <span className="gradient-text">Features</span>
          </h2>
          <p className="section-subtitle">
            Built with cutting-edge CNN and Deep Learning models for accurate person re-identification
          </p>

          {/* Neural Network Summary */}
          <div className="nn-summary">
            <div className="nn-chip">
              <span className="nn-dot"></span>
              <span>YuNet CNN (Face Detection)</span>
            </div>
            <div className="nn-chip">
              <span className="nn-dot"></span>
              <span>SFace ResNet (Recognition)</span>
            </div>
            <div className="nn-chip">
              <span className="nn-dot"></span>
              <span>ONNX Runtime</span>
            </div>
          </div>
        </motion.div>

        <motion.div
          className="features-grid"
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
        >
          {features.map((feature, index) => (
            <motion.div
              key={index}
              className="feature-card glass-card"
              variants={itemVariants}
              whileHover={{ scale: 1.02, y: -5 }}
            >
              <div className="feature-icon">{feature.icon}</div>
              <div className="feature-header">
                <h3 className="feature-title">{feature.title}</h3>
                <span className="feature-subtitle">{feature.subtitle}</span>
              </div>
              <p className="feature-description">{feature.description}</p>
              <div className="feature-tags">
                {feature.tags.map((tag, i) => (
                  <span key={i} className="feature-tag">{tag}</span>
                ))}
              </div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  );
};

export default Features;
