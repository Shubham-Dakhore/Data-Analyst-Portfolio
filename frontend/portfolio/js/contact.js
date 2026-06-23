/* File: frontend/portfolio/js/contact.js */

const contactForm =
    document.getElementById(
        "contactForm"
    );

if (contactForm) {

    contactForm.addEventListener(
        "submit",
        submitContactForm
    );
}

async function submitContactForm(
    event
) {

    event.preventDefault();

    const name =
        document.getElementById("name").value;

    const email =
        document.getElementById("email").value;

    const subject =
        document.getElementById("subject").value;

    const message =
        document.getElementById("message").value;

    try {

        await apiPost(
            "/api/contact",
            {
                name,
                email,
                subject,
                message
            }
        );

        alert(
            "Message sent successfully."
        );

        contactForm.reset();

    } catch (error) {

        alert(
            "Unable to send message."
        );
    }
}