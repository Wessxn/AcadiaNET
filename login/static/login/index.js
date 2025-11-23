<<<<<<< Updated upstream:login/static/login/index.js
document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === "student" && password === "acadia") {
    alert("Login successful! Redirecting to chat...");
    window.location.href = "chat.html"; // future chat page
  } else {
    alert("Invalid credentials. Try username: student, password: acadia");
  }
});
=======
document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (username === "student" && password === "acadia") {
    alert("Login successful! Redirecting to chat...");
    window.location.href = "chat.html"; // future chat page
  } else {
    alert("Invalid credentials. Try username: student user ID, password: ");
  }
});
>>>>>>> Stashed changes:index.js
