import { getAccessToken } from "../auth/tokenService.js";
import { setAccessToken, clearAuth, getUserId } from "../auth/tokenService.js";

export async function fetchWithAuth(url, options = {}) {
    if (!options.headers) {
        options.headers = {};
    }

    options.headers["Authorization"] = `Bearer ${getAccessToken()}`;
    let response = await fetch(url, options);


    if (response.status !== 401) {
        return response;
    }

    try {

        await refreshAccessToken();

        const user = await loadCurrentUser();
        const currentUserId = getUserId();

        if (currentUserId && currentUserId !== user.user.id) {
            console.log("User changed in another tab");

            clearAuth();
            location.reload();
            return;
        }

        options.headers["Authorization"] = `Bearer ${getAccessToken()}`;
        response = await fetch(url, options);

        return response;

    } catch (err) {
        clearAuth();
        location.reload();
    }
}

export async function loadCurrentUser() {
    const response = await fetch("/api/auth/me", {
        headers: {
            "Authorization": `Bearer ${getAccessToken()}`
        }
    });

    if (!response.ok) {
        throw new Error("Cannot load user");
    }

    const user = await response.json();
    return user;
}