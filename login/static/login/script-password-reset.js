document.addEventListener("DOMContentLoaded", () => {
  const resetForm = document.getElementById("resetForm");

  resetForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const emailInput = document.getElementById("email");
    const email = emailInput.value.trim();

    if (!validateEmail(email)) {
      alert("Please enter a valid email address.");
      return;
    }
    
    // Simulate sending reset email
    alert("A password reset link has been sent to: " + email);

    // Optional: Clear the input
    emailInput.value = "";

    // Redirect back to login after 2 seconds
    setTimeout(() => {
      window.location.href = "index.html";
    }, 2000);
  });
});

// Simple email validation
function validateEmail(email) {
  const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return pattern.test(email);
}