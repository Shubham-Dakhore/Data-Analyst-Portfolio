/* File: frontend/admin/js/login.js */

const loginForm =
    document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener(
        "submit",
        (event) => {

            event.preventDefault();

            const email =
                document.getElementById("email").value;

            const password =
                document.getElementById("password").value;

            /*
            Temporary Demo Login
            */

            if (
                email === "admin@email.com" &&
                password === "admin123"
            ) {

                localStorage.setItem(
                    "portfolio_token",
                    "demo_token"
                );

                window.location.href =
                    "dashboard.html";

            } else {

                alert("Invalid credentials");
            }

        }
    );
}