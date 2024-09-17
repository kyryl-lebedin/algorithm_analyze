// Typing effect function
function typeText(text, elementId, delay, callback = null) {
    const element = document.getElementById(elementId);
    element.classList.add('blink-cursor'); // Add cursor
    let index = 0;
  
    function typeCharacter() {
      if (index < text.length) {
        element.innerHTML += text.charAt(index);
        index++;
        setTimeout(typeCharacter, delay);
      } else {
        element.classList.remove('blink-cursor'); // Remove cursor after typing
        if (callback) {
          callback(); // Call callback function after typing is done
        }
      }
    }
  
    typeCharacter();
  }
  
  // Function to hide the typing cursor
  function removeCursor(elementId) {
    document.getElementById(elementId).classList.add('no-cursor');
  }
  
  // Ensure DOM is fully loaded before running the script
  document.addEventListener('DOMContentLoaded', function () {
    const headerText = "algorithm.analyze";
    typeText(headerText, 'header-text', 100); // Typing effect for the header
  });
  