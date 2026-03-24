import { loginRequest, registerRequest } from "../api/authApi.js";
import { setAccessToken, setUserId, clearAuth } from "./tokenService.js";


export async function register(email, password) {
    const data = {
        email: email,
        password: password
    };

    const response = await registerRequest(JSON.stringify(data));

    if (!response.ok) {
        throw new Error("Registration failed");
    }
}


export async function login(email, password) {

    const formData = new URLSearchParams();
    formData.append("username", email);
    formData.append("password", password);

    const response = await loginRequest(formData);

    if (!response.ok) {
        throw new Error("Login failed");
    }

    const data = await response.json();

    setAccessToken(data.access_token);
    setUserId(data.user_id);
}

export async function logout() {
    clearAuth();
    location.reload();
}