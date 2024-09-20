
function handleAlgorithmTypeSelection(current) {
    document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
        if (checkbox !== current) {
        checkbox.checked = false;
        }
    });

    document.getElementById('algInput').value = '';  

    if (current.checked) {
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
            console.log(data.input_type);
            const form = document.getElementById('input-selection-form');
            const checkboxes = form.querySelectorAll('input[name="input_type"]');
            checkboxes.forEach((checkbox) => {
                if (checkbox.value !== data.input_type) {
                    checkbox.checked = false;
                }else {
                    checkbox.checked = true;
                }
            });

            updateFormWithAlgorithms(data);
        })
        .catch(error => console.error('Error:', error));
    }
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
            document.getElementById('algInput').value = data.algorithm;
        })
        .catch(error => console.error('Error:', error));
    }
}

// Attach the handler to the select element for change events

function handleCodeSubmission(event) {
    event.preventDefault();

    const inputType = document.querySelector('input[name="input_type"]:checked'); // Get the checked checkbox
    console.log(inputType.value);
    const textareaValue = document.getElementById('algInput').value;
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
            input_type: inputType.value
        })
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => {
                document.getElementById('code_errors').textContent = err.error;
                throw new Error('Error from server: ' + err.error);
            });
        }
        
        return response.blob(); // Handle the response as a blob (image)
    })
    .then(imageBlob => {
        // Hide the forms and textarea
        // document.getElementById('input-form').style.display = 'none';
        document.getElementById('algorithm-selection-form').style.display = 'none';
        document.getElementById('input-selection-form').style.display = 'none';
        document.getElementById('algorithmForm').style.display = 'none';
        document.getElementById('analyze-button-form').style.display = 'none';

        // Display the image
        const imageObjectURL = URL.createObjectURL(imageBlob);
        const imageElement = document.getElementById('imageElement');
        imageElement.src = imageObjectURL;
        imageElement.style.display = 'block'; // Show the image

        // Display the AI analysis text
        document.getElementById('anal_description').style.display = 'block';
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

function handleInputTypeSelection(checkbox) {
    // Get all checkboxes in the form
    const checkboxes = document.querySelectorAll('input[name="input_type"]');
    
    // If the checkbox is checked, uncheck all others
    if (checkbox.checked) {
        checkboxes.forEach(function(box) {
            if (box !== checkbox) {
                box.checked = false;
            }
        });
    }
}
