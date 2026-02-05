document_id = "dark-ai-v1";

document.addEventListener('DOMContentLoaded', () => {
    const micBtn = document.getElementById('mic-btn');
    const sendBtn = document.getElementById('send-btn');
    const userInput = document.getElementById('user-input');
    const chatContainer = document.getElementById('chat-container');
    const aiOrb = document.getElementById('ai-orb');
    const statusText = document.getElementById('status-text');
    const statusDot = document.getElementById('status-dot');

    // Speech Recognition Setup
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    let recognition;

    if (SpeechRecognition) {
        recognition = new SpeechRecognition();
        recognition.continuous = false;
        recognition.lang = 'en-US';
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onstart = () => {
            aiOrb.classList.add('listening');
            updateStatus('Listening...', '#00d4ff');
            micBtn.classList.add('active');
        };

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            userInput.value = transcript;
            sendCommand(transcript);
        };

        recognition.onerror = (event) => {
            console.error('Speech recognition error:', event.error);
            stopListening();
        };

        recognition.onend = () => {
            stopListening();
        };
    }

    function stopListening() {
        aiOrb.classList.remove('listening');
        updateStatus('System Online', '#00ff88');
        micBtn.classList.remove('active');
    }

    function updateStatus(text, color) {
        statusText.innerText = text;
        statusDot.style.background = color;
        statusDot.style.boxShadow = `0 0 8px ${color}`;
    }

    // Text to Speech
    function speak(text) {
        if ('speechSynthesis' in window) {
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 1.0;
            utterance.pitch = 1.0;

            // Try to find a nice male voice if possible, or just default
            const voices = window.speechSynthesis.getVoices();
            if (voices.length > 0) {
                // Look for a deep/premium sounding voice
                const preferredVoice = voices.find(v => v.name.includes('Google US English') || v.name.includes('Male')) || voices[0];
                utterance.voice = preferredVoice;
            }

            utterance.onstart = () => {
                aiOrb.classList.add('thinking');
                updateStatus('Speaking...', '#9d00ff');
            };

            utterance.onend = () => {
                aiOrb.classList.remove('thinking');
                updateStatus('System Online', '#00ff88');
            };

            window.speechSynthesis.speak(utterance);
        }
    }

    async function sendCommand(command) {
        if (!command.trim()) return;

        console.log("Sending command:", command);
        addBubble(command, 'user');
        userInput.value = '';

        aiOrb.classList.add('thinking');
        updateStatus('Thinking...', '#ffcc00');

        try {
            const response = await fetch('/api/command', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ command: command })
            });

            if (!response.ok) {
                throw new Error(`Server returned ${response.status}`);
            }

            const data = await response.json();
            console.log("Server response:", data);

            if (data.response && data.response.trim()) {
                addBubble(data.response, 'ai');
                speak(data.response);
            } else if (data.error) {
                addBubble("Error: " + data.error, 'ai');
            } else {
                addBubble("I heard you, but I don't have a response for that.", 'ai');
            }
        } catch (error) {
            console.error('Fetch Error:', error);
            addBubble("System Error: Could not connect to the backend server.", 'ai');
        } finally {
            aiOrb.classList.remove('thinking');
            updateStatus('System Online', '#00ff88');
        }
    }

    function addBubble(text, sender) {
        const bubble = document.createElement('div');
        bubble.className = `bubble ${sender}-bubble`;
        bubble.innerText = text;
        chatContainer.appendChild(bubble);

        // Auto scroll
        chatContainer.scrollTop = chatContainer.scrollHeight;

        // Remove welcome message if it exists
        const welcome = document.querySelector('.welcome-msg');
        if (welcome) welcome.style.display = 'none';
    }

    // Event Listeners
    micBtn.addEventListener('click', () => {
        if (recognition) {
            try {
                recognition.start();
            } catch (e) {
                recognition.stop();
            }
        } else {
            alert('Speech recognition is not supported in your browser.');
        }
    });

    sendBtn.addEventListener('click', () => {
        sendCommand(userInput.value);
    });

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendCommand(userInput.value);
        }
    });

    // Clear Chat Button
    const clearBtn = document.getElementById('clear-btn');
    clearBtn.addEventListener('click', () => {
        chatContainer.innerHTML = `
            <div class="welcome-msg">
                <h2>Welcome, Sir</h2>
                <p>How can I assist you today?</p>
            </div>
        `;
    });
});
