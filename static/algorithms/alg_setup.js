
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
                document.getElementById('input_type').value = data.input_type;
                console.log(data);
                updateFormWithAlgorithms(data);
            })
            .catch(error => console.error('Error:', error));
        }
    }

    function handleAlgorithmSelection(current) {
        document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
            if ((checkbox !== current) && (checkbox.name === 'algorithm')) {
            checkbox.checked = false;
            }
        });

        if (current.checked) {
            const postUrl = '../../algorithms/receive_alg/';
            const csrfToken = getCookie('csrftoken');  // Get the CSRF token from cookies

            fetch(postUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken  // Include the CSRF token in the request headers
            },
            body: JSON.stringify({
                algorithm: current.value
            })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('algInput').value = data.algorithm;
                console.log(data);
                
            })
            .catch(error => console.error('Error:', error));
        } 
    }

    function handleCodeSubmission(event) {
        event.preventDefault();
    
        const textareaValue = document.getElementById('algInput').value;
        const inputType = document.getElementById('input_type').value;
        const postUrl = '../../algorithms/send_alg/';
        const csrfToken = getCookie('csrftoken'); 
        if (!textareaValue.trim() || !inputType.trim()) {
            document.getElementById('code_errors').textContent = 'Please fill all the required fields';
            return; // Stop the function here if the validation fails
        }
    
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
            
            return response.blob(); // Handle the response as a blob (image)
        })
        .then(imageBlob => {
            // Hide the forms and textarea
            document.getElementById('input-form').style.display = 'none';
            document.getElementById('algorithm-selection-form').style.display = 'none';
            document.getElementById('inputType').style.display = 'none';
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
        const form = document.getElementById('algorithmForm');

        // Clear previous contents (useful for updates or re-fetches)
        form.innerHTML = '';

        // Iterate through the algorithms array in the data
        data.algorithms.forEach(algorithm => {
            // Create a checkbox for each algorithm
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.id = algorithm;
            checkbox.name = 'algorithm';
            checkbox.value = algorithm;
            checkbox.onchange = function() { handleAlgorithmSelection(this); };

            // Create a label for each checkbox
            const label = document.createElement('label');
            label.htmlFor = algorithm;
            label.textContent = algorithm;  // Set the text of the label to the algorithm name

            // Append the checkbox and label to the form
            form.appendChild(checkbox);
            form.appendChild(label);
        });
    }
