import React from 'react';
import { motion } from 'framer-motion';
import { FiCamera, FiCpu, FiSearch, FiMonitor } from 'react-icons/fi';
import './HowItWorks.css';

const HowItWorks = () => {
  const steps = [
    {
      number: '01',
      icon: <FiCamera />,
      title: 'Capture Face',
      description: 'Camera captures live video feed and YuNet model detects faces in real-time.',
    },
    {
      number: '02',
      icon: <FiCpu />,
      title: 'Extract Features',
      description: 'SFace neural network generates 128-dimensional embedding vectors.',
    },
    {
      number: '03',
      icon: <FiSearch />,
      title: 'Match Identity',
      description: 'Cosine similarity compares embeddings against registered gallery.',
    },
    {
      number: '04',
      icon: <FiMonitor />,
      title: 'Display Results',
      description: 'Real-time overlay shows identity labels and confidence scores.',
    },
  ];

  return (
    <section className="how-it-works" id="how-it-works">
      {/* Animated background waves */}
      <div className="hiw-background">
        <div className="wave wave-1"></div>
        <div className="wave wave-2"></div>
        <div className="wave wave-3"></div>
      </div>

      <div className="container">
        <motion.div
          className="section-header"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <span className="section-badge">How It Works</span>
          <h2 className="section-title">
            From Beginner to <span className="gradient-text">Builder</span>
          </h2>
          <p className="section-subtitle">
            Understanding the person re-identification pipeline
          </p>
        </motion.div>

        <div className="steps-horizontal">
          {/* Connecting line with glow */}
          <div className="connecting-line">
            <div className="line-glow"></div>
          </div>

          {steps.map((step, index) => (
            <motion.div
              key={index}
              className="step-item"
              initial={{ opacity: 0, y: 50 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: index * 0.15 }}
            >
              <motion.div
                className="step-number-circle"
                whileHover={{ scale: 1.1 }}
                animate={{
                  boxShadow: [
                    '0 0 20px rgba(0, 255, 136, 0.3)',
                    '0 0 40px rgba(0, 255, 136, 0.5)',
                    '0 0 20px rgba(0, 255, 136, 0.3)'
                  ]
                }}
                transition={{
                  boxShadow: { duration: 2, repeat: Infinity, delay: index * 0.3 }
                }}
              >
                <span className="step-num">{step.number}</span>
                <div className="step-icon">{step.icon}</div>
              </motion.div>

              <div className="step-content">
                <h3 className="step-title">{step.title}</h3>
                <p className="step-description">{step.description}</p>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default HowItWorks;
