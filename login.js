document.addEventListener("DOMContentLoaded", () => {
  // Get DOM elements
  const step1 = document.getElementById("signupStep1");
  const step2 = document.getElementById("signupStep2");
  const step3 = document.getElementById("signupStep3");
  const stepIndicator = document.querySelector(".step-indicator");

  const toStep3 = document.getElementById("toStep3");
  const backTo1 = document.getElementById("backTo1");
  const backTo2 = document.getElementById("backTo2");

  // Initialize: hide steps 2 and 3
  step2.style.display = "none";
  step3.style.display = "none";

  // Helper: show a step and hide the others
  function showStep(stepNumber) {
    step1.style.display = stepNumber === 1 ? "block" : "none";
    step2.style.display = stepNumber === 2 ? "block" : "none";
    step3.style.display = stepNumber === 3 ? "block" : "none";
    stepIndicator.textContent = `Step ${stepNumber} of 3`;
  }

  // Step 1 → Step 2
  step1.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!step1.checkValidity()) {
      step1.reportValidity();
      return;
    }
    showStep(2);
  });

  // Step 2 → Step 3
  toStep3.addEventListener("click", () => {
    const password = document.getElementById("password").value.trim();
    const confirm = document.getElementById("confirmPassword").value.trim();

    if (!step2.checkValidity()) {
      step2.reportValidity();
      return;
    }

    if (password !== confirm) {
      alert("Passwords do not match!");
      return;
    }

    // Fill summary on Step 3
    document.getElementById("summaryName").textContent =
      document.getElementById("firstName").value + " " + document.getElementById("lastName").value;

    document.getElementById("summaryMajor").textContent =
      document.getElementById("major").value;

    document.getElementById("summaryUsername").textContent =
      document.getElementById("username").value;

    document.getElementById("summaryEmail").textContent =
      document.getElementById("email").value;

    showStep(3);
  });

  // Back buttons
  backTo1.addEventListener("click", () => showStep(1));
  backTo2.addEventListener("click", () => showStep(2));

  // Finish signup
  step3.addEventListener("submit", (e) => {
    e.preventDefault();

    // Collect all data (optional: store in localStorage or send to backend)
    const signupData = {
      firstName: document.getElementById("firstName").value.trim(),
      lastName: document.getElementById("lastName").value.trim(),
      major: document.getElementById("major").value.trim(),
      username: document.getElementById("username").value.trim(),
      email: document.getElementById("email").value.trim(),
      password: document.getElementById("password").value.trim(),
      profilePic: document.getElementById("profilePic").files[0] ? document.getElementById("profilePic").files[0].name : null
    };

    console.log("Signup Data:", signupData); // For demo, print in console

    alert("Account successfully created!");

    // Redirect to login page
    window.location.href = "index.html";
  });
});
