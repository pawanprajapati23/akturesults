/**
 * AKTU Results - Floating Community Banner Widget
 * Injects a responsive, non-intrusive floating bar promoting AKTU Telegram & WhatsApp communities.
 */

(function () {
    const DISMISS_KEY = 'aktu_community_banner_dismissed_v1';
    const DISMISS_DURATION_MS = 24 * 60 * 60 * 1000; // 24 hours

    function isDismissed() {
        try {
            const lastDismissed = localStorage.getItem(DISMISS_KEY);
            if (lastDismissed && Date.now() - parseInt(lastDismissed, 10) < DISMISS_DURATION_MS) {
                return true;
            }
        } catch (e) {
            // Local storage not accessible
        }
        return false;
    }

    function dismissBanner() {
        try {
            localStorage.setItem(DISMISS_KEY, Date.now().toString());
        } catch (e) {}

        const banner = document.getElementById('aktu-community-banner');
        if (banner) {
            banner.style.transform = 'translateY(120%)';
            banner.style.opacity = '0';
            setTimeout(() => {
                banner.remove();
            }, 400);
        }
    }

    function initCommunityBanner() {
        if (isDismissed()) return;
        if (document.getElementById('aktu-community-banner')) return;

        // Create CSS styles
        const style = document.createElement('style');
        style.setAttribute('id', 'aktu-community-banner-styles');
        style.innerHTML = `
            #aktu-community-banner {
                position: fixed;
                bottom: 20px;
                left: 50%;
                transform: translateX(-50%) translateY(0);
                width: calc(100% - 30px);
                max-width: 960px;
                background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #1e1b4b 100%);
                color: #ffffff;
                padding: 16px 22px;
                border-radius: 16px;
                box-shadow: 0 12px 35px rgba(0, 0, 0, 0.35), 0 0 0 1px rgba(255, 255, 255, 0.12);
                z-index: 99999;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 16px;
                transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease;
                font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
                backdrop-filter: blur(12px);
                -webkit-backdrop-filter: blur(12px);
            }

            .aktu-cb-info {
                display: flex;
                align-items: center;
                gap: 14px;
                flex: 1 1 auto;
            }

            .aktu-cb-badge {
                background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);
                color: #ffffff;
                font-size: 11px;
                font-weight: 800;
                padding: 5px 10px;
                border-radius: 20px;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                white-space: nowrap;
                display: inline-flex;
                align-items: center;
                gap: 5px;
                box-shadow: 0 2px 8px rgba(245, 158, 11, 0.4);
            }

            .aktu-cb-badge-dot {
                width: 7px;
                height: 7px;
                background-color: #ffffff;
                border-radius: 50%;
                display: inline-block;
                animation: aktuCbPulse 1.4s infinite ease-in-out;
            }

            @keyframes aktuCbPulse {
                0%, 100% { opacity: 1; transform: scale(1); }
                50% { opacity: 0.4; transform: scale(0.75); }
            }

            .aktu-cb-text {
                font-size: 14px;
                line-height: 1.4;
                color: #e2e8f0;
            }

            .aktu-cb-text strong {
                color: #ffffff;
                font-weight: 700;
            }

            .aktu-cb-actions {
                display: flex;
                align-items: center;
                gap: 10px;
                flex-shrink: 0;
            }

            .aktu-cb-btn {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                padding: 9px 16px;
                border-radius: 10px;
                font-size: 13px;
                font-weight: 700;
                text-decoration: none;
                transition: all 0.2s ease;
                white-space: nowrap;
            }

            .aktu-cb-btn-telegram {
                background: #0088cc;
                color: #ffffff;
                box-shadow: 0 4px 12px rgba(0, 136, 204, 0.35);
            }

            .aktu-cb-btn-telegram:hover {
                background: #0077b5;
                transform: translateY(-2px);
                box-shadow: 0 6px 16px rgba(0, 136, 204, 0.5);
            }

            .aktu-cb-btn-whatsapp {
                background: #25d366;
                color: #ffffff;
                box-shadow: 0 4px 12px rgba(37, 211, 102, 0.35);
            }

            .aktu-cb-btn-whatsapp:hover {
                background: #20bd5a;
                transform: translateY(-2px);
                box-shadow: 0 6px 16px rgba(37, 211, 102, 0.5);
            }

            .aktu-cb-close {
                background: rgba(255, 255, 255, 0.12);
                border: none;
                color: #94a3b8;
                width: 28px;
                height: 28px;
                border-radius: 50%;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 16px;
                line-height: 1;
                transition: all 0.2s ease;
                margin-left: 4px;
            }

            .aktu-cb-close:hover {
                background: rgba(255, 255, 255, 0.25);
                color: #ffffff;
            }

            @media (max-width: 768px) {
                #aktu-community-banner {
                    bottom: 12px;
                    width: calc(100% - 20px);
                    padding: 14px;
                    flex-direction: column;
                    align-items: stretch;
                    gap: 12px;
                }

                .aktu-cb-info {
                    flex-direction: column;
                    align-items: flex-start;
                    gap: 8px;
                }

                .aktu-cb-actions {
                    justify-content: space-between;
                    width: 100%;
                }

                .aktu-cb-btn {
                    flex: 1;
                    justify-content: center;
                    padding: 9px 10px;
                    font-size: 12px;
                }

                .aktu-cb-close {
                    position: absolute;
                    top: 10px;
                    right: 10px;
                }
            }
        `;
        document.head.appendChild(style);

        // Create Banner HTML
        const banner = document.createElement('div');
        banner.setAttribute('id', 'aktu-community-banner');
        banner.innerHTML = `
            <div class="aktu-cb-info">
                <span class="aktu-cb-badge">
                    <span class="aktu-cb-badge-dot"></span> LIVE COMMUNITY
                </span>
                <div class="aktu-cb-text">
                    Join <strong>50,000+ AKTU Students</strong> on Telegram & WhatsApp for instant result updates, notes & placement alerts!
                </div>
            </div>
            <div class="aktu-cb-actions">
                <a href="https://t.me/akturesults_official" target="_blank" rel="noopener noreferrer" class="aktu-cb-btn aktu-cb-btn-telegram">
                    ✈️ Join Telegram
                </a>
                <a href="https://chat.whatsapp.com/aktu_community_2026" target="_blank" rel="noopener noreferrer" class="aktu-cb-btn aktu-cb-btn-whatsapp">
                    💬 Join WhatsApp
                </a>
                <button class="aktu-cb-close" id="aktu-cb-close-btn" aria-label="Close community banner">&times;</button>
            </div>
        `;

        document.body.appendChild(banner);

        // Add close event
        document.getElementById('aktu-cb-close-btn').addEventListener('click', dismissBanner);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCommunityBanner);
    } else {
        initCommunityBanner();
    }
})();
