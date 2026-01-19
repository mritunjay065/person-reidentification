import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Features from './components/Features';
import HowItWorks from './components/HowItWorks';
import Projects from './components/Projects';
import Footer from './components/Footer';
import AuroraBackground from './components/AuroraBackground';

function App() {
  return (
    <div className="app">
      <AuroraBackground />
      <div className="content-wrapper">
        <Navbar />
        <Hero />
        <Features />
        <HowItWorks />
        <Projects />
        <Footer />
      </div>
    </div>
  );
}

export default App;
