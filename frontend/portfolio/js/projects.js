/* File: frontend/portfolio/js/projects.js */

document.addEventListener(
    "DOMContentLoaded",
    loadProjects
);

async function loadProjects() {

    const container =
        document.getElementById(
            "projectsContainer"
        );

    if (!container) return;

    container.innerHTML =
        "<p>Loading projects...</p>";

    try {

        const projects =
            await apiGet(
                "/api/projects/"
            );

        renderProjects(projects);

    } catch (error) {

        console.error(
            "Project Load Error:",
            error
        );

        container.innerHTML = `
            <p class="error-message">
                Failed to load projects.
            </p>
        `;
    }
}

function renderProjects(
    projects
) {

    const container =
        document.getElementById(
            "projectsContainer"
        );

    if (!container) return;

    if (!projects.length) {

        container.innerHTML = `
            <p class="empty-message">
                No projects available.
            </p>
        `;

        return;
    }

    let html = "";

    projects.forEach(project => {

        const imageUrl =
            project.image_url
                ? `${API_BASE_URL}${project.image_url}`
                : "images/project-placeholder.jpg";

        html += `

        <div class="project-card">

            <img
                src="${imageUrl}"
                alt="${project.title}"
                loading="lazy"
            >

            <h3>
                ${project.title}
            </h3>

            <p>
                ${project.description}
            </p>

            <p>
                <strong>
                    Technologies:
                </strong>
                ${project.technologies || "N/A"}
            </p>

            ${
                project.github_url
                ? `
                <a
                    href="${project.github_url}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    GitHub
                </a>
                `
                : ""
            }

            ${
                project.live_url
                ? `
                <a
                    href="${project.live_url}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Live Demo
                </a>
                `
                : ""
            }

        </div>
        `;
    });

    container.innerHTML = html;
}