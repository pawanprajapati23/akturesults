/**
 * Mini - AKTU AI Student Assistant Widget
 * Smart Hinglish / English AI Assistant for AKTU Results, UPTAC Counselling, Fees & Notes
 */

(function () {
    // Inject Mini Assistant Styles
    const style = document.createElement('style');
    style.innerHTML = `
        .mini-widget-container { position: fixed; bottom: 20px; right: 20px; z-index: 99999; font-family: 'Plus Jakarta Sans', -apple-system, sans-serif; }
        
        .mini-bubble-tooltip { position: absolute; bottom: 75px; right: 0; background: #1e1b4b; color: #ffffff; padding: 12px 18px; border-radius: 16px; font-size: 13px; font-weight: 600; white-space: nowrap; box-shadow: 0 10px 25px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.15); animation: floatPulse 3s infinite ease-in-out; display: flex; align-items: center; gap: 8px; cursor: pointer; }
        .mini-bubble-tooltip::after { content: ''; position: absolute; bottom: -8px; right: 25px; border-width: 8px 8px 0; border-style: solid; border-color: #1e1b4b transparent; display: block; width: 0; }
        @keyframes floatPulse { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
        
        .mini-avatar-btn { width: 60px; height: 60px; border-radius: 50%; background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%); color: white; border: 3px solid white; box-shadow: 0 8px 25px rgba(79, 70, 229, 0.4); cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 28px; position: relative; transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }
        .mini-avatar-btn:hover { transform: scale(1.1); box-shadow: 0 12px 30px rgba(79, 70, 229, 0.6); }
        
        .mini-online-dot { position: absolute; top: 2px; right: 2px; width: 14px; height: 14px; background: #22c55e; border: 2px solid white; border-radius: 50%; }

        /* Chat Modal */
        .mini-chat-modal { display: none; position: fixed; bottom: 90px; right: 20px; width: 380px; max-width: calc(100vw - 40px); height: 520px; max-height: calc(100vh - 120px); background: #ffffff; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.25); border: 1px solid #cbd5e1; flex-direction: column; overflow: hidden; z-index: 99999; animation: slideUp 0.3s ease; }
        @keyframes slideUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

        .mini-chat-header { background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%); color: white; padding: 16px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); }
        .mini-header-info { display: flex; align-items: center; gap: 10px; }
        .mini-header-info strong { font-size: 16px; font-weight: 800; }
        .mini-header-info span { font-size: 11px; color: #4ade80; display: block; }
        .mini-close-btn { background: none; border: none; color: white; font-size: 24px; cursor: pointer; opacity: 0.8; }
        .mini-close-btn:hover { opacity: 1; }

        .mini-chat-body { flex: 1; padding: 15px; overflow-y: auto; background: #f8fafc; display: flex; flex-direction: column; gap: 12px; }

        .mini-msg { max-width: 85%; padding: 12px 16px; border-radius: 14px; font-size: 14px; line-height: 1.5; word-wrap: break-word; }
        .mini-msg-bot { background: white; color: #1e293b; border: 1px solid #e2e8f0; align-self: flex-start; border-bottom-left-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.03); }
        .mini-msg-user { background: #4f46e5; color: white; align-self: flex-end; border-bottom-right-radius: 4px; font-weight: 500; }

        .mini-suggestions { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
        .mini-sug-btn { background: #e0e7ff; color: #3730a3; border: 1px solid #c7d2fe; padding: 6px 12px; border-radius: 16px; font-size: 12px; font-weight: 700; cursor: pointer; transition: 0.2s; }
        .mini-sug-btn:hover { background: #4f46e5; color: white; }

        .mini-chat-footer { padding: 12px; background: white; border-top: 1px solid #e2e8f0; display: flex; gap: 8px; }
        .mini-input { flex: 1; padding: 12px 16px; border: 2px solid #e2e8f0; border-radius: 10px; font-size: 14px; outline: none; font-weight: 500; }
        .mini-input:focus { border-color: #4f46e5; }
        .mini-send-btn { background: #4f46e5; color: white; border: none; padding: 0 18px; border-radius: 10px; font-weight: 700; cursor: pointer; font-size: 16px; }
        .mini-send-btn:hover { background: #3730a3; }
    `;
    document.head.appendChild(style);

    // Create Widget HTML Structure
    const widget = document.createElement('div');
    widget.className = 'mini-widget-container';
    widget.innerHTML = `
        <div id="miniTooltip" class="mini-bubble-tooltip" onclick="toggleMiniChat()">
            🤖 <span>Hi! Need help with AKTU Results or UPTAC Choice Filling?</span>
        </div>
        <button class="mini-avatar-btn" onclick="toggleMiniChat()" aria-label="Ask Mini AI Assistant">
            🤖
            <span class="mini-online-dot"></span>
        </button>

        <div id="miniChatModal" class="mini-chat-modal">
            <div class="mini-chat-header">
                <div class="mini-header-info">
                    <div style="font-size:24px;">🤖</div>
                    <div>
                        <strong>Mini AI Assistant</strong>
                        <span>🟢 Online | AKTU & UPTAC Expert</span>
                    </div>
                </div>
                <button class="mini-close-btn" onclick="toggleMiniChat()">×</button>
            </div>

            <div id="miniChatBody" class="mini-chat-body">
                <div class="mini-msg mini-msg-bot">
                    Namaste! I am <strong>Mini</strong>, your AKTU AI Assistant. How can I help you today?
                    <div class="mini-suggestions">
                        <button class="mini-sug-btn" onclick="askMini('How to check AKTU Result?')">📊 Check Result</button>
                        <button class="mini-sug-btn" onclick="askMini('UPTAC Choice Predictor')">🎯 Choice Predictor</button>
                        <button class="mini-sug-btn" onclick="askMini('AKTU College Fees & TFW')">💰 College Fees</button>
                        <button class="mini-sug-btn" onclick="askMini('AKTU CGPA Formula')">🧮 CGPA Formula</button>
                        <button class="mini-sug-btn" onclick="askMini('Download Quantum PDFs')">📚 Quantum PDFs</button>
                    </div>
                </div>
            </div>

            <form class="mini-chat-footer" onsubmit="sendMiniMessage(event)">
                <input type="text" id="miniInput" class="mini-input" placeholder="Type your AKTU doubt here..." autocomplete="off" />
                <button type="submit" class="mini-send-btn">➔</button>
            </form>
        </div>
    `;
    document.body.appendChild(widget);
})();

function toggleMiniChat() {
    const modal = document.getElementById('miniChatModal');
    const tooltip = document.getElementById('miniTooltip');
    const isOpen = modal.style.display === 'flex';

    if (isOpen) {
        modal.style.display = 'none';
        if (tooltip) tooltip.style.display = 'flex';
    } else {
        modal.style.display = 'flex';
        if (tooltip) tooltip.style.display = 'none';
        document.getElementById('miniInput').focus();
    }
}

function askMini(text) {
    document.getElementById('miniInput').value = text;
    sendMiniMessage(new Event('submit'));
}

function sendMiniMessage(e) {
    e.preventDefault();
    const input = document.getElementById('miniInput');
    const query = input.value.trim();
    if (!query) return;

    const chatBody = document.getElementById('miniChatBody');

    // Add User Message
    const userMsg = document.createElement('div');
    userMsg.className = 'mini-msg mini-msg-user';
    userMsg.innerText = query;
    chatBody.appendChild(userMsg);

    input.value = '';
    chatBody.scrollTop = chatBody.scrollHeight;

    // Simulate AI thinking
    const typing = document.createElement('div');
    typing.className = 'mini-msg mini-msg-bot';
    typing.innerText = 'Mini is thinking... 💭';
    chatBody.appendChild(typing);
    chatBody.scrollTop = chatBody.scrollHeight;

    setTimeout(() => {
        typing.remove();
        const botMsg = document.createElement('div');
        botMsg.className = 'mini-msg mini-msg-bot';
        botMsg.innerHTML = getMiniAIResponse(query);
        chatBody.appendChild(botMsg);
        chatBody.scrollTop = chatBody.scrollHeight;
    }, 600);
}

function getMiniAIResponse(q) {
    const query = q.toLowerCase();

    if (query.includes('result') || query.includes('one view') || query.includes('check')) {
        return `You can check your AKTU semester result directly on the <strong>AKTU One View Portal</strong> using your Roll Number without needing an ERP password! <br/><br/><a href="/results/aktu-one-view-result-2026.html" style="color:#4f46e5; font-weight:700;">👉 Open One View Result Portal</a>`;
    }
    if (query.includes('choice') || query.includes('predictor') || query.includes('uptac') || query.includes('rank')) {
        return `Try our free <strong>UPTAC 2026 Choice Filling Predictor Tool</strong>! Enter your JEE Main/CUET rank to predict top AKTU colleges (IET, KNIT, JSS, AKGEC) and copy your preference list.<br/><br/><a href="/admissions/uptac-choice-filling-predictor-2026.html" style="color:#4f46e5; font-weight:700;">🎯 Open Choice Filling Predictor</a>`;
    }
    if (query.includes('fee') || query.includes('cost') || query.includes('college fee')) {
        return `Top AKTU Govt Colleges (IET, KNIT, BIET) tuition fees are ~₹65k - ₹89k/yr. Top Private NCR Colleges (JSS, AKGEC, KIET) fees are ~₹1.28L - ₹1.40L/yr.<br/><br/><a href="/colleges/aktu-college-fees-structure-2026.html" style="color:#4f46e5; font-weight:700;">💰 View College Fee Structure</a>`;
    }
    if (query.includes('cgpa') || query.includes('percentage') || query.includes('formula')) {
        return `Official AKTU Formula: <code>Percentage = (CGPA - 0.75) × 10</code>. E.g., 8.00 CGPA = 72.50%.<br/><br/><a href="/tools/aktu-marks-analyzer.html" style="color:#4f46e5; font-weight:700;">🧮 Use CGPA & Percentage Calculator</a>`;
    }
    if (query.includes('quantum') || query.includes('pdf') || query.includes('notes') || query.includes('pyq')) {
        return `Download free branch-wise Quantum series PDFs, notes, and past 5 years solved question papers for 1st to 8th semester!<br/><br/><a href="/syllabus/aktu-quantum-pdf-downloads.html" style="color:#4f46e5; font-weight:700;">📚 Download Quantum Series PDFs</a>`;
    }
    if (query.includes('scholarship') || query.includes('up scholarship')) {
        return `UP Govt reimburses tuition fees up to ₹56,600 (Private) or 100% (Govt) for eligible students with family income < ₹2.0 Lakhs (General/OBC) or < ₹2.5 Lakhs (SC/ST). Ensure your bank account has <strong>NPCI Aadhaar Seeding</strong>.<br/><br/><a href="/admissions/aktu-scholarship-guide-2026.html" style="color:#4f46e5; font-weight:700;">💵 View UP Scholarship Guide</a>`;
    }
    if (query.includes('grace') || query.includes('cop') || query.includes('back')) {
        return `AKTU awards up to <strong>7 Grace Marks</strong> per year if external theory score is at least 25 out of 70 (35%). Carry Over Paper (COP) fee is ₹1,000/subject.<br/><br/><a href="/tools/aktu-grace-cop-fee-calculator.html" style="color:#4f46e5; font-weight:700;">⚖️ Use Grace & COP Calculator</a>`;
    }

    return `Thanks for asking! You can explore our master portal for all AKTU tools, One View results, fee structures, and UPTAC predictors.<br/><br/><a href="/aktu-all-in-one-directory.html" style="color:#4f46e5; font-weight:700;">🌐 Open AKTU All-in-One Directory</a>`;
}
