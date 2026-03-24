export async function loginRequest(formData) {
    return fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData
    });
}

export async function registerRequest(formData) {
    return fetch("/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: formData
    });
}

export async function logoutRequest() {
    return fetch("/logout", {
        method: "POST"
    });
}
