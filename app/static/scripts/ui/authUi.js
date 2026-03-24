import { login, register } from "../auth/auth.js";
import { logoutRequest } from "../api/authApi.js";


const loginShowBtn = document.getElementById("login-show-btn");
const regShowBtn = document.getElementById("reg-show-btn");
const loginForm = document.getElementById("login-form");
const regForm = document.getElementById("reg-form");
const loginBtn = document.getElementById("login-btn");
const regBtn = document.getElementById("register-btn");
const guestBtn = document.getElementById("guest-btn");

loginShowBtn.addEventListener("click", showLoginForm);
regShowBtn.addEventListener("click", showRegisterForm);
loginBtn.addEventListener("click", loginUi);
regBtn.addEventListener("click", registerUi);
guestBtn.addEventListener("click", loginAsGuestUi);


console.log("Auth UI loaded");


export async function loginUi() {
    try {
        const email = document.getElementById("login-email").value;
        const password = document.getElementById("login-password").value;

        await login(email, password);

        window.location.href = "/products";
    } catch (error) {
        console.error("Login failed:", error);
    }
}

export async function registerUi() {
    try {
        const email = document.getElementById("reg-email").value;
        const password = document.getElementById("reg-password").value;
       
        await register(email, password);
    } catch (error) {
        console.error("Registration failed:", error);
    }
}

export async function loginAsGuestUi() {
    window.location.href = "/products/guest";
}




async function showLoginForm() {
    regForm.classList.remove("auth-form");
    regForm.classList.add("hidden");

    loginForm.classList.remove("hidden");
    loginForm.classList.add("auth-form");
    
}

async function showRegisterForm() {
    loginForm.classList.remove("auth-form");
    loginForm.classList.add("hidden");

    regForm.classList.remove("hidden");
    regForm.classList.add("auth-form");
}