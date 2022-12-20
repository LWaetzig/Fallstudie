const loginForm = document.getElementById("login-field")
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("error-msg");

loginButton.addEventListener("click", (e) =>{
    e.preventDefault();
    
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "web_dev") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})