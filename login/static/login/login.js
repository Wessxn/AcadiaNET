// Get form elements
const step1 = document.getElementById('signupStep1');
const step2 = document.getElementById('signupStep2');
const step3 = document.getElementById('signupStep3');
const stepIndicator = document.getElementById('stepIndicator');

// Get all 'Next' and 'Back' buttons
const toStep2Button = step1.querySelector('button[type="submit"]'); // Next button in step 1
const backTo1Button = document.getElementById('backTo1');
const toStep3Button = document.getElementById('toStep3'); // Next button in step 2
const backTo2Button = document.getElementById('backTo2');
const finishSignupButton = document.getElementById('finishSignup');

/**
 * Updates the visibility of the form steps and the step indicator text.
 * @param {number} currentStep The step number to show (1, 2, or 3).
 */
function showStep(currentStep) {
    step1.classList.add('hidden');
    step2.classList.add('hidden');
    step3.classList.add('hidden');

    if (currentStep === 1) {
        step1.classList.remove('hidden');
        stepIndicator.textContent = 'Step 1 of 3';
    } else if (currentStep === 2) {
        step2.classList.remove('hidden');
        stepIndicator.textContent = 'Step 2 of 3';
    } else if (currentStep === 3) {
        step3.classList.remove('hidden');
        stepIndicator.textContent = 'Step 3 of 3';
        updateSummary(); // Populate review data when going to step 3
    }
}

/**
 * Collects data from the first two steps and populates the review section.
 */
function updateSummary() {
    // Data from Step 1
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const major = document.getElementById('major').value;

    // Data from Step 2
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;

    // Update Step 3 review section
    document.getElementById('summaryName').textContent = `${firstName} ${lastName}`;
    document.getElementById('summaryMajor').textContent = major;
    document.getElementById('summaryUsername').textContent = username;
    document.getElementById('summaryEmail').textContent = email;
}

// --- Event Listeners for Navigation ---

// Step 1 'Next' button
step1.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    // Basic form validation is handled by 'required' attribute in HTML.
    // If you need complex validation (e.g., password strength), add it here.
    showStep(2);
});

// Step 2 'Back' button
backTo1Button.addEventListener('click', function() {
    showStep(1);
});

// Step 2 'Next' button
step2.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Check if passwords match before proceeding
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if (password !== confirmPassword) {
        alert("Passwords do not match!");
        document.getElementById('confirmPassword').focus();
        return; // Stop execution
    }
    
    showStep(3);
});

// Step 3 'Back' button
backTo2Button.addEventListener('click', function() {
    showStep(2);
});

// Step 3 'Create Account' button (Final submission)
step3.addEventListener('submit', function(event) {
    event.preventDefault(); 
    
    // NOTE: This is where you would typically use fetch() or XMLHttpRequest 
    // to send all the collected data (name, major, credentials, profile pic) 
    // to your Django view for processing and database storage.
    
    alert("Account creation simulated! Data would now be sent to Django server.");
    // In a real application, you would redirect the user upon successful submission.
});

// Initialize the form to show Step 1
showStep(1);