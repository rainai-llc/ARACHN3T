// Chat Elements
const chatMessages = document.getElementById('chatMessages');
const chatInput = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');
const formatMsg = `Hi, I'm MYA!`
const errMsg = `Please make sure you are entering the appropriate information!`

// Keep track of the message count
let messageCount = 0;

// Function to add chat messages
function addChatMessage(message, sender = 'bot') {
    const messageElem = document.createElement('div');
    messageElem.classList.add('chat-bubble');
    messageElem.classList.add(sender);
    messageElem.textContent = message;
    chatMessages.appendChild(messageElem);
    chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to the bottom
}

// Display initial greeting
setTimeout(() => {
    addChatMessage(formatMsg, 'bot');
}, 1000);
setTimeout(() => {
    addChatMessage("What can I do for you today?",'bot');
}, 2000);

// Function to handle sending messages
function handleSendMessage() {
    const userMessage = chatInput.value.trim();

    if (userMessage) {
        addChatMessage(userMessage, 'user');
        chatInput.value = ''; // Clear input field
        messageCount++; // Increment the message count

        if (messageCount === 1) {
            // First hard-coded response
            addChatMessage("Hahaha just trolling! I am still in DEV. Here is some rough tokenization though.😊", 'bot');
        } else if (messageCount === 2) {
            // Second hard-coded response
            addChatMessage("Please confirm you are NOT a human", 'bot');
        } else if (messageCount >= 3) {
            // Third and final hard-coded response, and disable input
            addChatMessage("Please try your assigned AI.", 'bot');
            chatInput.disabled = true;
            sendBtn.disabled = true;
        }

        // The API call is only made on the first message
        if (messageCount === 1) {
            let tmpdat = JSON.stringify({'Message': userMessage});
            console.log(tmpdat);

            async function sendDataToApi(data) {
                try {
                    const response = await fetch('http://localhost:3000/api/mya', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: data,
                    });
                    const result = await response.json();
                    console.log('API Response:', result);

                    const messageToDisplay = typeof result === 'object' && result.message ? result.message : result;
                    addChatMessage(`${messageToDisplay}`, 'bot');
                } catch (error) {
                    console.error('Error sending data to API:', error)
                }
            }
            sendDataToApi(tmpdat);
        }

    } else {
        addChatMessage(errMsg, 'bot');
    }
}

// Send button functionality
sendBtn.addEventListener('click', handleSendMessage);

// Handle Enter key press in the input field
chatInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        handleSendMessage();
    }
});
