import re

with open('index_new.html', 'r') as f:
    content = f.read()

# Add reveal-3d CSS
css_addition = """
    /* Reveal & Tilt */
    .reveal-3d {
      opacity: 0;
      transform: perspective(1200px) rotateX(15deg) translateY(40px) translateZ(-50px);
      transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1), transform 1s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
    }
    .reveal-3d.in-view {
      opacity: 1;
      transform: perspective(1200px) rotateX(0deg) translateY(0) translateZ(0);
    }
    .hover-tilt {
      transition: box-shadow 0.4s ease;
    }
    .hover-tilt:hover {
      box-shadow: 0 20px 40px rgba(0,0,0,0.5);
      z-index: 10;
    }
"""

content = content.replace("/* ── HERO SECTION ── */", css_addition + "\n    /* ── HERO SECTION ── */")

# Add scripts
scripts = """
<script>
  // 1. Intersection Observer for Scroll Reveals
  const observerOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      }
    });
  }, observerOptions);

  document.querySelectorAll('.bento-card, .section-title, .mega-text').forEach(el => {
      el.classList.add('reveal-3d');
      observer.observe(el);
  });

  // 2. 3D Tilt Effect on Mouse Move
  const tiltElements = document.querySelectorAll('.bento-card');
  tiltElements.forEach(el => {
    el.classList.add('hover-tilt');
    el.addEventListener('mousemove', (e) => {
      const rect = el.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = ((y - centerY) / centerY) * -5;
      const rotateY = ((x - centerX) / centerX) * 5;
      
      el.style.transform = `perspective(1000px) scale3d(1.02, 1.02, 1.02) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });
    
    el.addEventListener('mouseleave', () => {
      el.style.transform = `perspective(1000px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg)`;
    });
  });
</script>
</body>
"""

content = content.replace("</body>", scripts)

with open('index_new.html', 'w') as f:
    f.write(content)

print("Updated index_new.html with animations")
