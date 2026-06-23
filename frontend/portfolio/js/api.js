/* File: frontend/portfolio/js/api.js */

const API_BASE_URL =
    "http://127.0.0.1:8000";

/*
=================================
GET REQUEST
=================================
*/

async function apiGet(endpoint) {

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`
    );

    if (!response.ok) {

        throw new Error(
            "Request Failed"
        );
    }

    return await response.json();
}

/*
=================================
POST REQUEST
=================================
*/

async function apiPost(
    endpoint,
    data
) {

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify(data)
        }
    );

    if (!response.ok) {

        throw new Error(
            "Request Failed"
        );
    }

    return await response.json();
}

/*
=================================
DELETE REQUEST
=================================
*/

async function apiDelete(
    endpoint
) {

    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            method: "DELETE"
        }
    );

    return await response.json();
}