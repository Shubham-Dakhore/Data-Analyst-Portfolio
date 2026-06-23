/* File: frontend/admin/js/admin-api.js */

const loginForm =
    document.getElementById(
        "loginForm"
    );

if (loginForm) {

    loginForm.addEventListener(
        "submit",
        login
    );
}

async function login(
    event
) {

    event.preventDefault();

    const email =
        document.getElementById(
            "email"
        ).value;

    const password =
        document.getElementById(
            "password"
        ).value;

    try {

        const result =
            await fetch(
                "http://127.0.0.1:8000/api/login",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({
                            email,
                            password
                        })
                }
            );

            if (!result.ok) {
                throw new Error("Invalid credentials");
            }

            const data = await result.json();

            localStorage.setItem(
                "portfolio_token",
                data.access_token
            );

            window.location.href = "dashboard.html";

    } catch (error) {

        alert(
            "Login failed."
        );
    }
}