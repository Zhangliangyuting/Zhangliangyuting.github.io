class NoiseEffect {
  constructor() {
    this.canvas = document.createElement('canvas');
    this.canvas.classList.add('noise-overlay');
    
    const container = document.querySelector('.noise-background');
    if (container) {
      container.appendChild(this.canvas);
      
      this.canvas.style.position = 'absolute';
      this.canvas.style.top = '0';
      this.canvas.style.left = '0';
      this.canvas.style.width = '100%';
      this.canvas.style.height = '100%';
      this.canvas.style.opacity = '0.05';
      this.canvas.style.mixBlendMode = 'multiply';
    }
    
    this.ctx = this.canvas.getContext('2d');
    this.frame = 0;
    
    this.resize();
    this.createNoise();
    this.animate();
    
    window.addEventListener('resize', () => this.resize());
  }

  resize() {
    const container = document.querySelector('.noise-background');
    if (container) {
      this.canvas.width = container.offsetWidth;
      this.canvas.height = container.offsetHeight;
    }
  }

  createNoise() {
    const imageData = this.ctx.createImageData(this.canvas.width, this.canvas.height);
    const buffer32 = new Uint32Array(imageData.data.buffer);
    
    for (let i = 0; i < buffer32.length; i++) {
      if (Math.random() < 0.5) {
        buffer32[i] = 0xFF000000;
      }
    }
    
    this.ctx.putImageData(imageData, 0, 0);
  }

  animate() {
    this.frame++;
    if (this.frame % 2 === 0) {
      this.createNoise();
    }
    requestAnimationFrame(() => this.animate());
  }
}

if (document.querySelector('.noise-background')) {
  window.addEventListener('DOMContentLoaded', () => {
    new NoiseEffect();
  });
}