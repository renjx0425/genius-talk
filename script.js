// Send the message when the user presses the Enter key
document.getElementById('userInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

// Enter the hint content to the input when clicking on a hint button
function handleHintButtonClick(event) {
    const hintMessage = event.target.innerText;
    document.getElementById('userInput').value = hintMessage;
}
document.querySelectorAll('.hint button').forEach(button => {
    button.addEventListener('click', handleHintButtonClick);
});

document.getElementById('finishButton').addEventListener('click', function() {
    document.querySelector('.summary').classList.remove('hidden');
    document.getElementById('overlay').style.display = 'block';
});

// Hide the summary and overlay when clicking outside the summary
document.getElementById('overlay').addEventListener('click', function() {
    document.querySelector('.summary').classList.add('hidden');
    document.getElementById('overlay').style.display = 'none';
});

document.getElementById('geniusTalk').addEventListener('click', function() {
    window.location.href = 'index.html';
});

document.getElementById('continueButton').addEventListener('click', function() {
    window.location.href = 'index.html';
});

document.getElementById('chatButton').addEventListener('click', function() {
    window.location.href = 'main.html';
});

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatMessages = document.querySelector('.chat-messages');
    const audioPlayer = document.getElementById('audioPlayer'); // Reference the audio player



    if (userInput.value.trim() !== "") {
        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'user');
        userMessage.innerHTML = `<p>${userInput.value}</p>`;
        chatMessages.appendChild(userMessage);

        // Call the backend
        try {
            const response = await fetch('http://127.0.0.1:5000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userInput.value }),
            });

            const data = await response.json();

            // Add bot reply to the chat
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot');
            botMessage.innerHTML = `<p>${data.reply || "Sorry, something went wrong."}</p>`;
            chatMessages.appendChild(botMessage);

            // Play audio if available
            if (data.audio_url) {
                audioPlayer.src = data.audio_url; // Set the audio source
                audioPlayer.style.display = 'block'; // Make the player visible
                try {
                    await audioPlayer.play(); // Play the audio
                } catch (error) {
                    console.error("Error playing audio:", error);
                }
            } else {
                console.warn("No audio URL received.");
            }
        } catch (error) {
            // Handle server connection errors
            console.error("Error communicating with backend:", error);
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot');
            botMessage.innerHTML = `<p>Sorry, I couldn't connect to the server.</p>`;
            chatMessages.appendChild(botMessage);
        }

        // Clear the input and scroll to the latest message
        userInput.value = "";
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
}

