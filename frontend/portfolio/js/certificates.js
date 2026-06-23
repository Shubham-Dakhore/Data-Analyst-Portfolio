document.addEventListener(
    "DOMContentLoaded",
    loadCertificates
);

async function loadCertificates() {

    try {

        const certificates =
            await apiGet(
                "/api/certificates/"
            );

        renderCertificates(
            certificates
        );

    } catch (error) {

        console.error(
            "Certificates Error:",
            error
        );
    }
}

function renderCertificates(
    certificates
) {

    const container =
        document.getElementById(
            "certificatesContainer"
        );

    if (!container) return;

    container.innerHTML = "";

    if (
        certificates.length === 0
    ) {

        container.innerHTML =

        `
        <p>
            No certificates available.
        </p>
        `;

        return;
    }

    certificates.forEach(cert => {

        let imageUrl =
            cert.image_url || "";

        if (
            imageUrl.startsWith("/")
        ) {

            imageUrl =
                `http://127.0.0.1:8000${imageUrl}`;
        }

        container.innerHTML += `

        <div class="certificate-card">

            <img
                src="${imageUrl}"
                alt="${cert.title}"
                class="certificate-image"
            >

            <h4>
                ${cert.title}
            </h4>

            <p>
                <strong>Issuer:</strong>
                ${cert.issuer || ""}
            </p>

            <p>
                ${cert.description || ""}
            </p>

            ${
                cert.certificate_url
                ?
                `
                <a
                    href="${cert.certificate_url}"
                    target="_blank"
                    class="btn"
                >
                    View Certificate
                </a>
                `
                :
                ""
            }

        </div>

        `;
    });
}