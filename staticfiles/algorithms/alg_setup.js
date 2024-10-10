function handleAlgorithmTypeSelection(current) {
  const buttons = document.querySelectorAll(".alg-button");

  // Deselect all buttons and apply 'dimmed' class
  buttons.forEach((button) => {
    if (button !== current) {
      button.classList.remove("active");
    }
  });

  // Activate the selected button and remove 'dimmed' class
  current.classList.add("active");

  // Clear the input field
  myCodeMirror.setValue("");

  // If the button is selected, make a POST request
  const postUrl = "../../algorithms/receive_alg_type/";
  const csrfToken = getCookie("csrftoken"); // Get the CSRF token from cookies

  fetch(postUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken, // Include the CSRF token in the request headers
    },
    body: JSON.stringify({
      algorithm_type: current.value,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      const in_type = document.getElementById(data.input_type);
      console.log(in_type);
      console.log(current.value);
      myCodeMirror.setValue(data.template);
      myCodeMirror.setOption("readOnly", false);
      if (current.value !== "Custom") {
        handleInputTypeSelection(in_type);
      } else {
        handleUnrestrictedInputTypeSelection(in_type);
      }

      updateFormWithAlgorithms(data);
    })
    .catch((error) => console.error("Error:", error));
}

function handleAlgorithmSelection() {
  const selectElement = document.getElementById("algorithmSelect");
  const selectedValue = selectElement.value;

  if (selectedValue) {
    const postUrl = "../../algorithms/receive_alg/";
    const csrfToken = getCookie("csrftoken"); // Get the CSRF token from cookies

    fetch(postUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken, // Include the CSRF token in the request headers
      },
      body: JSON.stringify({
        algorithm: selectedValue,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        myCodeMirror.setValue(data.algorithm);
      })
      .catch((error) => console.error("Error:", error));
  }
}

// Attach the handler to the select element for change events

function handleCodeSubmission(event) {
  event.preventDefault();

  const inputType = document.querySelector(
    "#input-selection-form .input-button.active"
  ).value;
  const textareaValue = myCodeMirror.getValue();
  const postUrl = "../../algorithms/send_alg/";
  const csrfToken = getCookie("csrftoken");

  const nValue = document.getElementById("slider1").value;
  const aValue = document.getElementById("slider2").value;

  if (!textareaValue.trim() || !inputType) {
    document.getElementById("code_errors").textContent =
      "Error: Please fill all the required fields";
    return; // Stop the function here if the validation fails
  }

  // Proceed with the form submission

  document.getElementsByClassName("content-box")[0].style.display = "none";
  document.getElementsByClassName("waiting-box")[0].style.display = "block";

  // Start timer for 1 minute (60000 milliseconds)
  const timeoutId = setTimeout(function () {
    // Redirect to another URL if no response is received within 1 minute
    window.location.href = "../../algorithms/alg_setup/";
  }, 60000);

  fetch(postUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      alg_code: textareaValue,
      input_type: inputType,
      n: nValue,
      a: aValue,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        clearTimeout(timeoutId);
        return response.json().then((err) => {
          document.getElementsByClassName("content-box")[0].style.display =
            "flex";
          document.getElementsByClassName("waiting-box")[0].style.display =
            "none";
          document.getElementById("code_errors").textContent =
            "Error: " + err.error;
          throw new Error("Error from server: " + err.error);
        });
      }
      return response.json(); // Parse the response as JSON
    })
    .then((data) => {
      clearTimeout(timeoutId);

      // Hide the forms and textarea
      document.getElementsByClassName("content-box")[0].style.display = "flex";
      document.getElementsByClassName("waiting-box")[0].style.display = "none";
      document.getElementById("algorithm-selection-form").style.display =
        "none";
      document.getElementById("input-selection-form").style.display = "none";
      document.getElementById("algorithmForm").style.display = "none";
      document.getElementById("analyze-button-form").style.display = "none";
      document.getElementById("range-slider-container").style.display = "none";
      document.getElementById("analyze-button").style.display = "none";
      document.getElementsByClassName(
        "analyze-button-container"
      )[0].style.display = "none";

      // Handle and display the image
      const imageElement = document.getElementById("imageElement");
      const imageBase64 = data.image;
      imageElement.src = `data:image/png;base64,${imageBase64}`;
      imageElement.style.display = "block"; // Show the image

      // Display the AI analysis text (predictions)
      const predictions = data.predictions;
      const classSign = data.class_sign;

      const predictionsElement = document.getElementById("anal_description");

      // Convert predictions object to an array of [key, value] pairs
      const sortedPredictions = Object.entries(predictions); // Assuming predictions are already sorted

      // Extract the main result (first item)
      const [mainResult, mainProb] = sortedPredictions[0];

      // Format the confidence percentage for the main result
      const mainResultText = `
            <div style="text-align: center;">
                Model predicts with <span style="font-size: 1.5em; color: #d89b18; font-family: 'Oswald-VariableFont';">${(
                  mainProb * 100
                ).toFixed(1)}% confidence</span>
            </div>
            <div style="text-align: center; margin-top: 10px;">
                Time Complexity: <span style="font-size: 1.5em; font-family: 'Oswald-VariableFont'; color: #d89b18;">${classSign} - ${
        mainResult.charAt(0).toUpperCase() + mainResult.slice(1)
      }</span>
            </div>
`;
      // Display the main result in the element
      predictionsElement.innerHTML = mainResultText;

      // If the main result isn't 100%, display secondary results
      if (mainProb < 1) {
        let secondaryResultsText = "<div style='margin-top: 20px;'>Also:</div>";
        for (let i = 1; i < sortedPredictions.length; i++) {
          const [result, prob] = sortedPredictions[i];
          if (prob > 0) {
            secondaryResultsText += `<div>with ${(prob * 100).toFixed(1)}% - ${
              result.charAt(0).toUpperCase() + result.slice(1)
            }</div>`;
          }
        }
        // Append secondary results to the main result
        predictionsElement.innerHTML += secondaryResultsText;
      }
      predictionsElement.style.display = "block"; // Show the predictions text
      document.getElementById("return-button").style.display = "block"; // Show the return button
      document.getElementById("imageElement").style.display = "block";
      document.getElementsByClassName(
        "back-button-container"
      )[0].style.display = "block";
    })

    .catch((error) => console.error("Error:", error));
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function updateFormWithAlgorithms(data) {
  console.log("hello");
  const selectElement = document.getElementById("algorithmSelect");

  // Clear previous options (useful for updates or re-fetches)
  selectElement.innerHTML =
    '<option value="">(Optional) Algorithm Examples</option>';

  // Iterate through the algorithms array in the data

  data.algorithms.forEach((algorithm) => {
    // Create an option element for each algorithm
    const option = document.createElement("option");
    option.value = algorithm;
    option.textContent = algorithm; // Set the text of the option to the algorithm name

    // Append the option to the select element
    selectElement.appendChild(option);
  });
}

function handleInputTypeSelection(current) {
  const buttons = document.querySelectorAll(".input-button");

  // Deselect all buttons and apply 'dimmed' class
  buttons.forEach((button) => {
    if (button !== current) {
      button.classList.remove("active");
      button.classList.add("dimmed");
      button.disabled = true;
    }
  });

  document.getElementById("algorithmSelect").disabled = false;

  // Activate the selected button and remove 'dimmed' class
  current.disabled = true;
  current.classList.add("active");
  current.classList.remove("dimmed");

  // Show the range sliders
  const rangeSliderContainer = document.getElementById(
    "range-slider-container"
  );
  rangeSliderContainer.style.display = "block";

  // Update the first slider with the values from the selected button
  const slider1 = document.getElementById("slider1");
  const slider1Label = document.getElementById("slider1-label");
  const slider1Value = document.getElementById("slider1-value");

  slider1.min = 1;
  slider1.max = current.getAttribute("data-n-max");
  slider1.value = current.getAttribute("data-n");
  slider1Label.textContent = current.getAttribute("data-input-name");
  slider1Value.textContent = slider1.value; // Update the display of slider1 value

  // Update the second slider with the values from the selected button
  const slider2 = document.getElementById("slider2");
  const slider2Value = document.getElementById("slider2-value");
  const slider2Label = document.getElementById("slider2-label");

  slider2.min = 1;
  slider2.max = current.getAttribute("data-a-max");
  slider2.value = current.getAttribute("data-a");
  slider2Label.textContent = slider2Label.getAttribute("data-input-name");
  slider2Value.textContent = slider2.value; // Update the display of slider2 value

  // Enable the sliders (optional, if you want sliders to be active immediately)
  slider1.disabled = false;
  slider2.disabled = false;
  const sliderOne = document.getElementById("slider" + "1");
  const sliderValueDisplayOne = document.getElementById(
    "slider" + "1" + "-value"
  );
  sliderValueDisplayOne.textContent = sliderOne.value + " (recommended)";
  const sliderTwo = document.getElementById("slider" + "2");
  const sliderValueDisplayTwo = document.getElementById(
    "slider" + "2" + "-value"
  );
  sliderValueDisplayTwo.textContent = sliderTwo.value + " (recommended)";
}

function updateSliderValue(sliderNum) {
  const slider = document.getElementById("slider" + sliderNum);
  const sliderValueDisplay = document.getElementById(
    "slider" + sliderNum + "-value"
  );
  sliderValueDisplay.textContent = slider.value;
}

function handleUnrestrictedInputTypeSelection(current) {
  const buttons = document.querySelectorAll(".input-button");

  // Deselect all buttons and apply 'dimmed' class
  buttons.forEach((button) => {
    if (button !== current) {
      button.classList.remove("active");
      button.classList.remove("dimmed");
      button.disabled = false;
    }
  });

  if (current.value !== "Custom") {
    current.classList.add("active");
  }

  // Handle range slider visibility and update values
  const rangeSliderContainer = document.getElementById(
    "range-slider-container"
  );

  // If "Custom" is selected, hide the sliders
  if (current.value === "Custom") {
    const slider1 = document.getElementById("slider1");
    const slider2 = document.getElementById("slider2");
    const slider1Label = document.getElementById("slider1-label");
    const slider1Value = document.getElementById("slider1-value");
    const slider2Label = document.getElementById("slider2-label");
    const slider2Value = document.getElementById("slider2-value");

    slider1.disabled = true;
    slider2.disabled = true;
    document.getElementById("algorithmSelect").disabled = true;
    slider1Value.textContent = "N";
    slider2Value.textContent = "A";
    slider1Label.textContent = "N Size";
    slider2Label.textContent = "A Range";
  } else {
    rangeSliderContainer.style.display = "block";

    // Update the first slider with the values from the selected button
    const slider1 = document.getElementById("slider1");
    const slider1Label = document.getElementById("slider1-label");
    const slider1Value = document.getElementById("slider1-value");

    slider1.min = 1;
    slider1.max = current.getAttribute("data-n-max");
    slider1.value = current.getAttribute("data-n");
    slider1Label.textContent = current.getAttribute("data-input-name");
    slider1Value.textContent = slider1.value; // Show initial value

    // Update the second slider with the values from the selected button
    const slider2 = document.getElementById("slider2");
    const slider2Value = document.getElementById("slider2-value");

    slider2.min = 1;
    slider2.max = current.getAttribute("data-a-max");
    slider2.value = current.getAttribute("data-a");
    slider2Value.textContent = slider2.value; // Show initial value
    const sliderOne = document.getElementById("slider" + "1");
    const sliderValueDisplayOne = document.getElementById(
      "slider" + "1" + "-value"
    );
    sliderValueDisplayOne.textContent = sliderOne.value + " (recommended)";
    const sliderTwo = document.getElementById("slider" + "2");
    const sliderValueDisplayTwo = document.getElementById(
      "slider" + "2" + "-value"
    );
    sliderValueDisplayTwo.textContent = sliderTwo.value + " (recommended)";
    slider1.disabled = false;
    slider2.disabled = false;
  }
}

// Get the textarea element by its ID
var myTextArea = document.getElementById("algInput");

// Initialize CodeMirror from the textarea
var myCodeMirror = CodeMirror.fromTextArea(myTextArea, {
  lineNumbers: true, // Show line numbers
  mode: "python", // Set the syntax highlighting mode to Python
  theme: "paraiso-light", // Optional theme (you can choose any theme or remove this line)
  indentUnit: 4, // Set indentation to 4 spaces
  matchBrackets: true, // Highlight matching brackets
  autoCloseBrackets: true,
  readOnly: true,
  lineWrapping: false,
});

myCodeMirror.setSize("97%", "100%");

// bae16-light, duotone-light, juejin, paraiso-light, solarized light, yeti, cobalt

function returnToSetup() {
  window.location.href = "../../algorithms/alg_setup/";
}

myCodeMirror.setValue("Choose your Algorithm Type first"); //#endregion

document.addEventListener("DOMContentLoaded", function () {
  // Select the container, CodeMirror editor, and the range slider container
  const container = document.querySelector(".left-side");
  const editorElement = document.querySelector(".CodeMirror");
  const rangeSliderContainer = document.querySelector(
    "#range-slider-container"
  );

  if (container && editorElement && rangeSliderContainer) {
    // Get the container's height
    const containerHeight = container.clientHeight;

    // Get the range slider container's height
    const sliderHeight = rangeSliderContainer.clientHeight;

    // Calculate the available height for the CodeMirror editor (98% of remaining space)
    const maxHeight = (containerHeight - sliderHeight) * 0.98;

    // Set the max-height of the .CodeMirror element
    editorElement.style.maxHeight = maxHeight + "px";
  }
});
