// AKTU Results PWA Smart Install Prompt Widget
(function() {
  let deferredPrompt;
  
  // Create styles
  const style = document.createElement('style');
  style.textContent = `
    .pwa-install-banner {
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%) translateY(120px);
      width: calc(100% - 30px);
      max-width: 480px;
      background: #0f172a;
      color: white;
      border: 1.5px solid #334155;
      border-radius: 16px;
      padding: 16px 20px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.5), 0 0 20px rgba(37,99,235,0.2);
      z-index: 999999;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: 'Inter', system-ui, sans-serif;
    }
    .pwa-install-banner.show {
      transform: translateX(-50%) translateY(0);
    }
    .pwa-icon-box {
      width: 46px;
      height: 46px;
      border-radius: 12px;
      background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      flex-shrink: 0;
      box-shadow: 0 4px 10px rgba(37,99,235,0.4);
    }
    .pwa-info {
      flex: 1;
    }
    .pwa-title {
      font-size: 14px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 2px;
    }
    .pwa-desc {
      font-size: 11px;
      color: #94a3b8;
      line-height: 1.3;
    }
    .pwa-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .pwa-btn-install {
      background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
      color: white;
      border: none;
      padding: 9px 16px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      white-space: nowrap;
      box-shadow: 0 4px 10px rgba(37,99,235,0.3);
    }
    .pwa-btn-close {
      background: transparent;
      color: #64748b;
      border: none;
      font-size: 18px;
      cursor: pointer;
      padding: 4px;
      line-height: 1;
    }
    .pwa-btn-close:hover {
      color: #cbd5e1;
    }
  `;
  document.head.appendChild(style);

  // Register service worker if supported
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/service-worker.js').catch(err => console.log('SW reg error:', err));
    });
  }

  // Create Banner Element
  const banner = document.createElement('div');
  banner.className = 'pwa-install-banner';
  banner.innerHTML = `
    <div class="pwa-icon-box">🎓</div>
    <div class="pwa-info">
      <div class="pwa-title">Install AKTU Portal App</div>
      <div class="pwa-desc">Fast 1-click results & offline calculators on your home screen</div>
    </div>
    <div class="pwa-actions">
      <button class="pwa-btn-install" id="pwa-install-btn">Install</button>
      <button class="pwa-btn-close" id="pwa-close-btn">&times;</button>
    </div>
  `;
  document.body.appendChild(banner);

  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    if (!localStorage.getItem('pwa_banner_dismissed')) {
      setTimeout(() => {
        banner.classList.add('show');
      }, 3000);
    }
  });

  document.getElementById('pwa-install-btn').addEventListener('click', async () => {
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;
      if (outcome === 'accepted') {
        banner.classList.remove('show');
      }
      deferredPrompt = null;
    } else {
      alert('To install, tap the Share/Menu icon in your browser and select "Add to Home Screen"');
    }
  });

  document.getElementById('pwa-close-btn').addEventListener('click', () => {
    banner.classList.remove('show');
    localStorage.setItem('pwa_banner_dismissed', 'true');
  });
})();
