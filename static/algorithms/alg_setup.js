
function handleAlgorithmTypeSelection(current) {
    const buttons = document.querySelectorAll('.alg-button');
    
    // Deselect all buttons and apply 'dimmed' class
    buttons.forEach(button => {
      if (button !== current) {
        button.classList.remove('active');
        
      }
    });
    
    // Activate the selected button and remove 'dimmed' class
    current.classList.add('active');

    
    // Clear the input field
    myCodeMirror.setValue("");
    
    // If the button is selected, make a POST request
    const postUrl = '../../algorithms/receive_alg_type/';
    const csrfToken = getCookie('csrftoken');  // Get the CSRF token from cookies
    
    fetch(postUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken  // Include the CSRF token in the request headers
      },
      body: JSON.stringify({
        algorithm_type: current.value
      })
    })
    .then(response => response.json())
    .then(data => {
     
      const in_type = document.getElementById(data.input_type);
      console.log(in_type)
      console.log(current.value)
      if (current.value !== 'Custom') {
            
            handleInputTypeSelection(in_type);
        } else {
            
            handleUnrestrictedInputTypeSelection(in_type);
        }


      
      updateFormWithAlgorithms(data);
    })
    .catch(error => console.error('Error:', error));
}
  

function handleAlgorithmSelection() {
    const selectElement = document.getElementById('algorithmSelect');
    const selectedValue = selectElement.value;

    if (selectedValue) {
        const postUrl = '../../algorithms/receive_alg/';
        const csrfToken = getCookie('csrftoken');  // Get the CSRF token from cookies

        fetch(postUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken  // Include the CSRF token in the request headers
            },
            body: JSON.stringify({
                algorithm: selectedValue
            })
        })
        .then(response => response.json())
        .then(data => {

            myCodeMirror.setValue(data.algorithm);
            
        })
        .catch(error => console.error('Error:', error));
    }
}

// Attach the handler to the select element for change events

function handleCodeSubmission(event) {
    event.preventDefault();

    const inputType = document.querySelector('#input-selection-form .input-button.active').value; 
    const textareaValue = myCodeMirror.getValue();
    const postUrl = '../../algorithms/send_alg/';
    const csrfToken = getCookie('csrftoken');
    
    if (!textareaValue.trim() || !inputType) {
        document.getElementById('code_errors').textContent = 'Please fill all the required fields';
        return; // Stop the function here if the validation fails
    }
    
    // Proceed with the form submission
        
    fetch(postUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            alg_code: textareaValue,
            input_type: inputType
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => {
                document.getElementById('code_errors').textContent = err.error;
                throw new Error('Error from server: ' + err.error);
            });
        }
        return response.json(); // Parse the response as JSON
    })
    .then(data => {
        // Hide the forms and textarea
        document.getElementById('algorithm-selection-form').style.display = 'none';
        document.getElementById('input-selection-form').style.display = 'none';
        document.getElementById('algorithmForm').style.display = 'none';
        document.getElementById('analyze-button-form').style.display = 'none';
    
        // Handle and display the image
        const imageElement = document.getElementById('imageElement');
        const imageBase64 = data.image;
        imageElement.src = `data:image/png;base64,${imageBase64}`;
        imageElement.style.display = 'block'; // Show the image
    
        // Display the AI analysis text (predictions)
        const predictions = data.predictions;
        const predictionsElement = document.getElementById('anal_description');
        
        if (predictionsElement) {
            // Find the prediction with the highest probability
            let maxPrediction = { algorithm: '', probability: 0 };
    
            for (const [algorithm, probability] of Object.entries(predictions)) {
                if (probability > maxPrediction.probability) {
                    maxPrediction = { algorithm, probability };
                }
            }
    
            // Update the inner HTML with the highest prediction and its percentage
            predictionsElement.innerHTML = `Our AI model thinks that the complexity of this graph is most likely <strong>${maxPrediction.algorithm}</strong> with ${(maxPrediction.probability * 100).toFixed(2)}% confidence.`;
    
            // Show the updated description
            predictionsElement.style.display = 'block';
    
        } else {
            console.error("Predictions element not found in the DOM.");
        }
    })
    
    .catch(error => console.error('Error:', error));
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
        }
        }
    }
    return cookieValue;
}

function updateFormWithAlgorithms(data) {
    console.log('hello')
    const selectElement = document.getElementById('algorithmSelect');

    // Clear previous options (useful for updates or re-fetches)
    selectElement.innerHTML = '<option value="">(Optional) Algorithm Examples</option>';

    // Iterate through the algorithms array in the data
    
    data.algorithms.forEach(algorithm => {
        // Create an option element for each algorithm
        const option = document.createElement('option');
        option.value = algorithm;
        option.textContent = algorithm;  // Set the text of the option to the algorithm name

        // Append the option to the select element
        selectElement.appendChild(option);
    });
}

function handleInputTypeSelection(current) {
    const buttons = document.querySelectorAll('.input-button');
    
    // Deselect all buttons and apply 'dimmed' class
    buttons.forEach(button => {
        
      if (button !== current) {
        button.classList.remove('active');
        button.classList.add('dimmed');
        button.disabled = true;
      }
    });
    
    // Activate the selected button and remove 'dimmed' class
    current.disabled = true;
    current.classList.add('active');
    current.classList.remove('dimmed');
    
  }

function handleUnrestrictedInputTypeSelection(current) {
    
    const buttons = document.querySelectorAll('.input-button');
    
    // Deselect all buttons and apply 'dimmed' class
    buttons.forEach(button => {
        
      if (button !== current) {
        button.classList.remove('active');
        button.classList.remove('dimmed');
        button.disabled = false;
      }

      
    });
    if (current.value !== 'Custom') {
        current.classList.add('active');
    }

}

//  allow tabs in algorithm input textarea
// document.getElementById('algInput').addEventListener('keydown', function(e) {
    
//     if (e.key === 'Tab') {
//         e.preventDefault();
//         let start = this.selectionStart;
//         let end = this.selectionEnd;

//         // Set textarea value to: text before caret + tab + text after caret
//         this.value = this.value.substring(0, start) + "\t" + this.value.substring(end);

//         // Put caret at right position again
//         this.selectionStart = this.selectionEnd = start + 1;
//     }
// });

// python formating in textarea

    // Get the textarea element by its ID
    


// Get the textarea element by its ID
var myTextArea = document.getElementById("algInput");

// Initialize CodeMirror from the textarea
var myCodeMirror = CodeMirror.fromTextArea(myTextArea, {
    lineNumbers: true,       // Show line numbers
    mode: "python",          // Set the syntax highlighting mode to Python
    theme: "paraiso-light",        // Optional theme (you can choose any theme or remove this line)
    indentUnit: 4,           // Set indentation to 4 spaces
    matchBrackets: true,      // Highlight matching brackets
    autoCloseBrackets: true,
});

    

// bae16-light, duotone-light, juejin, paraiso-light, solarized light, yeti, cobalt


function returnToSetup() {
    window.location.href = '../../algorithms/alg_setup/';
}
