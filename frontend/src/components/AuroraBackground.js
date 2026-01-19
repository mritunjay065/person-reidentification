import React, { useEffect, useRef } from 'react';
import './AuroraBackground.css';

const AuroraBackground = () => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    let animationId;
    let time = 0;

    const resize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    const drawAurora = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Dark background gradient
      const bgGradient = ctx.createLinearGradient(0, 0, 0, canvas.height);
      bgGradient.addColorStop(0, '#0a0a0a');
      bgGradient.addColorStop(0.5, '#0d1117');
      bgGradient.addColorStop(1, '#0a0a0a');
      ctx.fillStyle = bgGradient;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Aurora waves
      const waves = [
        { color: 'rgba(0, 255, 136, 0.15)', amplitude: 80, frequency: 0.003, speed: 0.02, yOffset: 0.4 },
        { color: 'rgba(0, 212, 255, 0.12)', amplitude: 100, frequency: 0.002, speed: 0.015, yOffset: 0.45 },
        { color: 'rgba(0, 255, 136, 0.1)', amplitude: 120, frequency: 0.0025, speed: 0.018, yOffset: 0.5 },
        { color: 'rgba(0, 180, 255, 0.08)', amplitude: 60, frequency: 0.004, speed: 0.025, yOffset: 0.35 },
        { color: 'rgba(0, 255, 200, 0.1)', amplitude: 90, frequency: 0.0015, speed: 0.012, yOffset: 0.55 },
      ];

      waves.forEach((wave, index) => {
        ctx.beginPath();
        ctx.moveTo(0, canvas.height);

        for (let x = 0; x <= canvas.width; x += 3) {
          const y = canvas.height * wave.yOffset +
            Math.sin(x * wave.frequency + time * wave.speed) * wave.amplitude +
            Math.sin(x * wave.frequency * 1.5 + time * wave.speed * 0.7) * (wave.amplitude * 0.5);
          ctx.lineTo(x, y);
        }

        ctx.lineTo(canvas.width, canvas.height);
        ctx.closePath();

        // Create gradient for each wave
        const gradient = ctx.createLinearGradient(0, canvas.height * 0.3, 0, canvas.height);
        gradient.addColorStop(0, wave.color);
        gradient.addColorStop(1, 'transparent');
        ctx.fillStyle = gradient;
        ctx.fill();
      });

      // Glowing orbs
      const orbs = [
        { x: 0.2, y: 0.4, radius: 300, color: 'rgba(0, 255, 136, 0.05)' },
        { x: 0.8, y: 0.5, radius: 400, color: 'rgba(0, 212, 255, 0.04)' },
        { x: 0.5, y: 0.6, radius: 350, color: 'rgba(0, 255, 180, 0.03)' },
      ];

      orbs.forEach(orb => {
        const gradient = ctx.createRadialGradient(
          canvas.width * orb.x + Math.sin(time * 0.01) * 50,
          canvas.height * orb.y + Math.cos(time * 0.008) * 30,
          0,
          canvas.width * orb.x,
          canvas.height * orb.y,
          orb.radius
        );
        gradient.addColorStop(0, orb.color);
        gradient.addColorStop(1, 'transparent');
        ctx.fillStyle = gradient;
        ctx.fillRect(0, 0, canvas.width, canvas.height);
      });

      // Floating particles
      for (let i = 0; i < 50; i++) {
        const x = ((i * 73 + time * 0.5) % canvas.width);
        const y = ((i * 137 + time * 0.3) % canvas.height);
        const size = (Math.sin(time * 0.05 + i) + 1) * 1.5 + 0.5;
        const alpha = (Math.sin(time * 0.03 + i * 0.5) + 1) * 0.15 + 0.05;
        
        ctx.beginPath();
        ctx.arc(x, y, size, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(0, 255, 136, ${alpha})`;
        ctx.fill();
      }

      time++;
      animationId = requestAnimationFrame(drawAurora);
    };

    resize();
    window.addEventListener('resize', resize);
    drawAurora();

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(animationId);
    };
  }, []);

  return <canvas ref={canvasRef} className="aurora-canvas" />;
};

export default AuroraBackground;
