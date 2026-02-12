(function () {
    'use strict';

    var fab = document.getElementById('chat-fab');
    var windowEl = document.getElementById('chat-window');
    var closeBtn = document.getElementById('chat-close');
    var messagesEl = document.getElementById('chat-messages');
    var inputEl = document.getElementById('chat-input');
    var sendBtn = document.getElementById('chat-send');
    var clearBtn = document.getElementById('chat-clear');

    if (!fab || !windowEl || !messagesEl || !inputEl || !sendBtn) return;

    function isOpen() {
        return !windowEl.classList.contains('chat-window--closed');
    }

    function openChat() {
        windowEl.classList.remove('chat-window--closed');
        if (messagesEl.children.length === 0) loadHistory();
        setTimeout(function () { scrollToBottom(); }, 100);
    }

    function closeChat() {
        windowEl.classList.add('chat-window--closed');
    }

    function toggleChat() {
        if (isOpen()) closeChat(); else openChat();
    }

    function scrollToBottom() {
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    function formatTime(createdAt) {
        if (!createdAt) return '';
        try {
            var d = new Date(createdAt);
            return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        } catch (e) {
            return '';
        }
    }

    function appendMessage(role, text, createdAt) {
        var div = document.createElement('div');
        div.className = 'chat-msg chat-msg--' + role;
        var timeStr = formatTime(createdAt);
        div.innerHTML = '<span class="chat-msg-text">' + escapeHtml(text) + '</span>' +
            (timeStr ? '<div class="chat-msg-time">' + escapeHtml(timeStr) + '</div>' : '');
        messagesEl.appendChild(div);
        scrollToBottom();
    }

    function escapeHtml(s) {
        var div = document.createElement('div');
        div.textContent = s;
        return div.innerHTML;
    }

    function showLoading() {
        var div = document.createElement('div');
        div.className = 'chat-msg chat-msg--loading chat-msg--loading-indicator';
        div.id = 'chat-loading-msg';
        div.innerHTML = '<span class="chat-msg-text">Thinking...</span>';
        messagesEl.appendChild(div);
        scrollToBottom();
    }

    function hideLoading() {
        var el = document.getElementById('chat-loading-msg');
        if (el) el.remove();
    }

    function loadHistory() {
        fetch('/chat/history', { credentials: 'same-origin' })
            .then(function (res) {
                if (res.status === 401) return { messages: [] };
                return res.json();
            })
            .then(function (data) {
                messagesEl.innerHTML = '';
                (data.messages || []).forEach(function (m) {
                    appendMessage(m.role, m.message, m.created_at);
                });
                scrollToBottom();
            })
            .catch(function () {
                messagesEl.innerHTML = '';
            });
    }

    function sendMessage() {
        var text = (inputEl.value || '').trim();
        if (!text) return;

        inputEl.value = '';
        appendMessage('user', text, new Date().toISOString());

        sendBtn.disabled = true;
        showLoading();

        fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'same-origin',
            body: JSON.stringify({ message: text })
        })
            .then(function (res) {
                return res.json().then(function (data) {
                    if (res.status === 401) {
                        throw new Error('Please log in again.');
                    }
                    if (res.status === 400 || res.status === 502) {
                        throw new Error(data.error || 'Something went wrong.');
                    }
                    return data;
                });
            })
            .then(function (data) {
                hideLoading();
                appendMessage('assistant', data.reply || '', new Date().toISOString());
            })
            .catch(function (err) {
                hideLoading();
                appendMessage('assistant', 'Error: ' + (err.message || 'Could not get a response. Please try again.'), null);
            })
            .then(function () {
                sendBtn.disabled = false;
            });
    }

    function clearChat() {
        fetch('/chat/clear', { method: 'POST', credentials: 'same-origin' })
            .then(function (res) {
                if (res.ok) {
                    messagesEl.innerHTML = '';
                }
            })
            .catch(function () {});
    }

    fab.addEventListener('click', toggleChat);
    closeBtn.addEventListener('click', closeChat);
    sendBtn.addEventListener('click', sendMessage);
    if (clearBtn) clearBtn.addEventListener('click', clearChat);

    inputEl.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
})();
