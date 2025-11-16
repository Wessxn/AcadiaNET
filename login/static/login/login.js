document.getElementById("signupStep1").addEventListener("submit", function(e) {
  e.preventDefault();

  const firstName = document.getElementById("firstName").value;
  const lastName = document.getElementById("lastName").value;
  const major = document.getElementById("major").value;

  // Store data temporarily (for demo)
  localStorage.setItem("signupData", JSON.stringify({ firstName, lastName, major }));

  alert(`Welcome ${firstName}! Proceeding to Step 2...`);
  window.location.href = "signup-step2.html"; // next screen
});