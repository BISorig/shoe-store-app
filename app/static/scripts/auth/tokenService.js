let accessToken = null
let currentUserId = null

export function setAccessToken(token) {
    accessToken = token
}

export function getAccessToken() {
    return accessToken
}

export function setUserId(id) {
    currentUserId = id
}

export function getUserId() {
    return currentUserId
}

export function clearAuth() {
    accessToken = null
    currentUserId = null
}