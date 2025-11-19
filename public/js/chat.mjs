// Chat Elements
const chatMessages = document.getElementById('chatMessages');
const chatInput = document.getElementById('chatInput');
const sendBtn = document.getElementById('sendBtn');
const formatMsg = `[~ MYA ~]:\nWelcome to ARACHN3T!\n\nI am MYA, (M)icro/acro (Y)early (A)ssistant.\nCurrent Intuitive Assitive AI features include:\n\n\t1.) Information Managenent\n\t2.) Data Analysis / Visualization / Engineering\n\t3.) Defensive & Offensive:\n\t\t- Digital Financial Support Services\n\t\t- Digital Cyber/Information Security Services\n\t4.) Rainai Inc. Support Services\n\nMy understanding is intended to grow based on our communication dynamics and developed workflows.\n\nReport an issue, concern, or emergency here or request collaboration, features, or other personalized support.`
const errMsg = `[~ MYA ~]:\n The prompt provided has not been approved by managment and will flagged as misuse.`

// Keep track of the message count

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
// setTimeout(() => {
//     addChatMessage(formatMsg, 'bot');
// }, 1000);
setTimeout(() => {
    addChatMessage(formatMsg);
}, 900);

// Function to handle sending messages

// function mci() {
//     let z = 0;
//     let y = ``;
//     let a = chatInput.value.trim();
//     let b = a.split(?);
//
//     b.forEach((c, index) => {
//         if (c.length>>z){
//             z=index;
//             y.concat(c);
//         }
//     })
//     do {
//         y.push(b[z-1]);
//         z--;
//     } while(z!=0)
// }

function handleSendMessage() {
    const userMessage = chatInput.value.trim();

    if (userMessage) {
        addChatMessage(userMessage, 'user');
        chatInput.value = ''; // Clear input field
        // The API call is only made on the first message
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
