// Typing effect function
function typeText(text, elementId, delay, callback = null) {
const element = document.getElementById(elementId);
let index = 0;

function typeCharacter() {
    if (index < text.length) {
    element.innerHTML += text.charAt(index);
    index++;
    setTimeout(typeCharacter, delay);
    } else if (callback) {
    callback(); // Call callback function after typing is done
    }
}

typeCharacter();
}

// Function to hide the typing cursor
function removeCursor(elementId) {
document.getElementById(elementId).classList.add('no-cursor');
}

// Fade-in button function
function fadeInButton() {
document.getElementById('start-btn').classList.add('visible');
}

// Text to be typed
const welcomeText = "Welcome!";
const subText = "Just write your algorithm and our AI model will analyze it ;)";

// Start typing when the page is loaded
window.onload = function() {
typeText(welcomeText, 'welcome-text', 100, function() {
    removeCursor('welcome-text'); // Hide cursor after typing "Welcome!"
    typeText(subText, 'sub-text', 50, function() {
    fadeInButton(); // Show button after typing
    });
});
};