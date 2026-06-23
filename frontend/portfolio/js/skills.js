/* File: frontend/portfolio/js/skills.js */

document.addEventListener(
    "DOMContentLoaded",
    loadSkills
);

async function loadSkills() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/skills/"
            );

        const skills =
            await response.json();

        const container =
            document.querySelector(
                ".skills-container"
            );

        container.innerHTML = "";

        skills.forEach(skill => {

            container.innerHTML += `

            <div class="skill-card">

                <h3>
                    ${skill.name}
                </h3>

                <div
                    style="
                        width:${skill.percentage}%;
                        height:10px;
                        background:#4CAF50;
                        margin-top:10px;
                    "
                ></div>

                <p>
                    ${skill.percentage}%
                </p>

            </div>

            `;
        });

    } catch(error) {

        console.error(error);
    }
}
