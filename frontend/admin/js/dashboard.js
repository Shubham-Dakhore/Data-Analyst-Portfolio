/* File: frontend/admin/js/dashboard.js */

const token =
    localStorage.getItem(
        "portfolio_token"
    );

let editingProjectId = null;

let editingCertificateId = null;

let editingSkillId = null;

if (!token) {

    window.location.href =
        "login.html";
}

document.addEventListener(
    "DOMContentLoaded",
    initializeDashboard
);

async function initializeDashboard() {

    await loadProjects();

    await loadMessages();
    
    await loadCertificates();

    await loadSkills();

    await loadResume();

    setupProjectForm();

    setupCertificateForm();

    setupSkillForm();

    setupResumeForm();

    setupLogout();
}

async function loadProjects() {

    try {

        const projects =
            await fetch(
                "http://127.0.0.1:8000/api/projects/"
            );

        const data =
            await projects.json();

        document.getElementById(
            "projectCount"
        ).textContent =
            data.length;

        renderProjects(data);

    } catch (error) {

        console.error(error);
    }
}

async function loadMessages() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/messages"
            );

        const messages =
            await response.json();

        document.getElementById(
            "messageCount"
        ).textContent =
            messages.length;

        renderMessages(
            messages
        );

    } catch (error) {

        console.error(error);
    }
}

function setupProjectForm() {

    const projectForm =
        document.getElementById(
            "projectForm"
        );

    if (!projectForm) return;

    projectForm.addEventListener(
        "submit",
        createProject
    );
}

async function createProject(
    event
) {

    event.preventDefault();

    try {

        const imageInput =
            document.getElementById(
                "projectImage"
            );

        let imageUrl = "";

        // =====================================
        // UPLOAD IMAGE IF SELECTED
        // =====================================

        if (
            imageInput &&
            imageInput.files.length > 0
        ) {

            const formData =
                new FormData();

            formData.append(
                "image",
                imageInput.files[0]
            );

            const uploadResponse =
                await fetch(
                    "http://127.0.0.1:8000/api/upload/project-image",
                    {
                        method: "POST",
                        body: formData
                    }
                );

            if (!uploadResponse.ok) {

                throw new Error(
                    "Image upload failed"
                );
            }

            const uploadResult =
                await uploadResponse.json();

            imageUrl =
                uploadResult.image_url;
        }

        const projectData = {

            title:
                document.getElementById(
                    "title"
                ).value,

            description:
                document.getElementById(
                    "description"
                ).value,

            technologies:
                document.getElementById(
                    "technologies"
                ).value,

            github_url:
                document.getElementById(
                    "github"
                ).value,

            live_url:
                document.getElementById(
                    "live"
                ).value,

            image_url:
                imageUrl
        };

        // =====================================
        // EDIT MODE
        // =====================================

        let endpoint =
            "http://127.0.0.1:8000/api/projects/";

        let method =
            "POST";

        if (editingProjectId) {

            endpoint =
                `http://127.0.0.1:8000/api/projects/${editingProjectId}`;

            method =
                "PUT";

            // Keep old image if new image not selected
            if (!imageUrl) {

                const existingProject =
                    await fetch(
                        endpoint
                    );

                const existingData =
                    await existingProject.json();

                projectData.image_url =
                    existingData.image_url;
            }
        }

        const response =
            await fetch(
                endpoint,
                {
                    method: method,

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify(
                            projectData
                        )
                }
            );

        if (!response.ok) {

            throw new Error(
                editingProjectId
                    ? "Failed to update project"
                    : "Failed to create project"
            );
        }

        alert(
            editingProjectId
                ? "Project Updated Successfully"
                : "Project Created Successfully"
        );

        editingProjectId = null;

        document.querySelector(
            "#projectForm button"
        ).textContent =
            "Add Project";

        event.target.reset();

        await loadProjects();

    } catch (error) {

        console.error(error);

        alert(
            error.message
        );
    }
}

function renderProjects(
    projects
) {

    const container =
        document.getElementById(
            "projectsList"
        );

    if (!container) return;

    container.innerHTML = "";

    projects.forEach(project => {

        container.innerHTML += `

        <div class="project-card">

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
                ${project.technologies || ""}
            </p>

            <button
                onclick="editProject(${project.id})"
            >
                Edit
            </button>

            <button
                onclick="deleteProject(${project.id})"
            >
                Delete
            </button>

        </div>

        `;
    });
}

async function editProject(
    projectId
) {

    try {

        const response =
            await fetch(
                `http://127.0.0.1:8000/api/projects/${projectId}`
            );

        if (!response.ok) {

            throw new Error(
                "Project not found"
            );
        }

        const project =
            await response.json();

        document.getElementById(
            "title"
        ).value =
            project.title;

        document.getElementById(
            "description"
        ).value =
            project.description;

        document.getElementById(
            "technologies"
        ).value =
            project.technologies || "";

        document.getElementById(
            "github"
        ).value =
            project.github_url || "";

        document.getElementById(
            "live"
        ).value =
            project.live_url || "";

        editingProjectId =
            project.id;

        document.querySelector(
            "#projectForm button"
        ).textContent =
            "Update Project";

        window.location.hash =
            "projects";

    } catch (error) {

        console.error(error);

        alert(
            error.message
        );
    }
}

async function deleteProject(
    id
) {

    const confirmDelete =
        confirm(
            "Delete this project?"
        );

    if (!confirmDelete) return;

    try {

        await fetch(
            `http://127.0.0.1:8000/api/projects/${id}`,
            {
                method: "DELETE"
            }
        );

        await loadProjects();

    } catch (error) {

        console.error(error);
    }
}

function setupLogout() {

    document
        .getElementById(
            "logoutBtn"
        )
        .addEventListener(
            "click",
            () => {

                localStorage.removeItem(
                    "portfolio_token"
                );

                window.location.href =
                    "login.html";
            }
        );
}



// ==========================================
// CERTIFICATES
// ==========================================

function setupCertificateForm() {

    const form =
        document.getElementById(
            "certificateForm"
        );

    if (!form) return;

    form.addEventListener(
        "submit",
        createCertificate
    );
}

async function loadCertificates() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/certificates/"
            );

        const certificates =
            await response.json();

        document.getElementById(
            "certificationCount"
        ).textContent =
            certificates.length;

        renderCertificates(
            certificates
        );

    } catch (error) {

        console.error(error);
    }
}

async function createCertificate(
    event
) {

    event.preventDefault();

    try {

        let imageUrl = "";

        const imageInput =
            document.getElementById(
                "certificateImage"
            );

        if (
            imageInput.files.length > 0
        ) {

            const formData =
                new FormData();

            formData.append(
                "image",
                imageInput.files[0]
            );

            const uploadResponse =
                await fetch(
                    "http://127.0.0.1:8000/api/upload/certificate-image",
                    {
                        method: "POST",
                        body: formData
                    }
                );

            const uploadData =
                await uploadResponse.json();

            imageUrl =
                uploadData.image_url;
        }

        const certificateData = {

            title:
                document.getElementById(
                    "certificateTitle"
                ).value,

            issuer:
                document.getElementById(
                    "certificateIssuer"
                ).value,

            issue_date:
                document.getElementById(
                    "certificateDate"
                ).value,

            credential_id:
                document.getElementById(
                    "credentialId"
                ).value,

            certificate_url:
                document.getElementById(
                    "certificateUrl"
                ).value,

            description:
                document.getElementById(
                    "certificateDescription"
                ).value,

            image_url:
                imageUrl
        };

        let url =
            "http://127.0.0.1:8000/api/certificates/";

        let method =
            "POST";

        if (
            editingCertificateId
        ) {

            url =
                `http://127.0.0.1:8000/api/certificates/${editingCertificateId}`;

            method =
                "PUT";
        }

        const response =
            await fetch(
                url,
                {
                    method: method,

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify(
                            certificateData
                        )
                }
            );

        if (!response.ok) {

            throw new Error(
                "Failed to save certificate"
            );
        }

        alert(
            "Certificate Saved"
        );

        editingCertificateId =
            null;

        event.target.reset();

        loadCertificates();

    } catch (error) {

        console.error(error);

        alert(
            error.message
        );
    }
}

function renderCertificates(
    certificates
) {

    const container =
        document.getElementById(
            "certificateList"
        );

    if (!container) return;

    container.innerHTML = "";

    certificates.forEach(
        certificate => {

            container.innerHTML += `

            <div class="project-card">

                <h3>
                    ${certificate.title}
                </h3>

                <p>
                    ${certificate.issuer}
                </p>

                <button
                    onclick="editCertificate(${certificate.id})"
                >
                    Edit
                </button>

                <button
                    onclick="deleteCertificate(${certificate.id})"
                >
                    Delete
                </button>

            </div>

            `;
        }
    );
}

async function editCertificate(
    id
) {

    const response =
        await fetch(
            `http://127.0.0.1:8000/api/certificates/${id}`
        );

    const certificate =
        await response.json();

    document.getElementById(
        "certificateTitle"
    ).value =
        certificate.title;

    document.getElementById(
        "certificateIssuer"
    ).value =
        certificate.issuer;

    document.getElementById(
        "certificateDate"
    ).value =
        certificate.issue_date;

    document.getElementById(
        "credentialId"
    ).value =
        certificate.credential_id || "";

    document.getElementById(
        "certificateUrl"
    ).value =
        certificate.certificate_url || "";

    document.getElementById(
        "certificateDescription"
    ).value =
        certificate.description || "";

    editingCertificateId =
        certificate.id;
}

async function deleteCertificate(
    id
) {

    if (
        !confirm(
            "Delete certificate?"
        )
    ) {
        return;
    }

    await fetch(
        `http://127.0.0.1:8000/api/certificates/${id}`,
        {
            method: "DELETE"
        }
    );

    loadCertificates();
}


// ==========================================
// SKILLS
// ==========================================

function setupSkillForm() {

    const form =
        document.getElementById(
            "skillForm"
        );

    if (!form) return;

    form.addEventListener(
        "submit",
        saveSkill
    );
}

async function loadSkills() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/skills/"
            );

        const skills =
            await response.json();

        document.getElementById(
            "skillCount"
        ).textContent =
            skills.length;

        renderSkills(skills);

    } catch (error) {

        console.error(error);
    }
}

async function saveSkill(event) {

    event.preventDefault();

    const skillData = {

        name:
            document.getElementById(
                "skillName"
            ).value,

        percentage:
            parseInt(
                document.getElementById(
                    "skillPercentage"
                ).value
            )
    };

    let url =
        "http://127.0.0.1:8000/api/skills/";

    let method =
        "POST";

    if (editingSkillId) {

        url =
            `http://127.0.0.1:8000/api/skills/${editingSkillId}`;

        method =
            "PUT";
    }

    await fetch(
        url,
        {
            method,

            headers: {
                "Content-Type":
                    "application/json"
            },

            body:
                JSON.stringify(
                    skillData
                )
        }
    );

    editingSkillId = null;

    event.target.reset();

    loadSkills();
}

function renderSkills(skills) {

    const container =
        document.getElementById(
            "skillsList"
        );

    container.innerHTML = "";

    skills.forEach(skill => {

        container.innerHTML += `

        <div class="project-card">

            <h3>
                ${skill.name}
            </h3>

            <p>
                ${skill.percentage}%
            </p>

            <button
                onclick="editSkill(${skill.id})"
            >
                Edit
            </button>

            <button
                onclick="deleteSkill(${skill.id})"
            >
                Delete
            </button>

        </div>

        `;
    });
}

async function editSkill(id) {

    const response =
        await fetch(
            `http://127.0.0.1:8000/api/skills/${id}`
        );

    const skill =
        await response.json();

    document.getElementById(
        "skillName"
    ).value =
        skill.name;

    document.getElementById(
        "skillPercentage"
    ).value =
        skill.percentage;

    editingSkillId =
        skill.id;
}

async function deleteSkill(id) {

    if (
        !confirm(
            "Delete this skill?"
        )
    ) return;

    await fetch(
        `http://127.0.0.1:8000/api/skills/${id}`,
        {
            method: "DELETE"
        }
    );

    loadSkills();
}

function setupResumeForm() {

    const form =
        document.getElementById(
            "resumeForm"
        );

    if (!form) return;

    form.addEventListener(
        "submit",
        uploadResume
    );
}

async function uploadResume(
    event
) {

    event.preventDefault();

    try {

        const fileInput =
            document.getElementById(
                "resumeFile"
            );

        const formData =
            new FormData();

        formData.append(
            "file",
            fileInput.files[0]
        );

        const uploadResponse =
            await fetch(
                "http://127.0.0.1:8000/api/upload/resume",
                {
                    method: "POST",
                    body: formData
                }
            );

        const uploadResult =
            await uploadResponse.json();

        await fetch(
            "http://127.0.0.1:8000/api/resume/",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({

                    file_name:
                        uploadResult.file_name,

                    file_url:
                        uploadResult.file_url
                })
            }
        );

        document.getElementById(
            "resumeStatus"
        ).innerHTML =
            "Resume Uploaded Successfully";

    } catch (error) {

        console.error(error);

        alert(
            "Resume Upload Failed"
        );
    }
}


async function loadResume() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/resume/"
            );

        const resume =
            await response.json();

        console.log(
            "Resume:",
            resume
        );

    } catch (error) {

        console.error(
            "Resume Load Error:",
            error
        );
    }
}


function renderMessages(messages) {

    const container =
        document.getElementById(
            "messagesList"
        );

    if (!container) return;

    container.innerHTML = "";

    messages.forEach(message => {

        container.innerHTML += `

        <div class="project-card">

            <h3>
                ${message.name}
            </h3>

            <p>
                ${message.email}
            </p>

            <p>
                ${message.subject}
            </p>

            <p>
                ${new Date(
                    message.created_at
                ).toLocaleString()}
            </p>

<p>
    Status:
    ${
        message.is_read
            ? "✅ Read"
            : "🔴 Unread"
    }
</p>

<button
    onclick="viewMessage(${message.id})"
>
    View
</button>

<button
    onclick="toggleRead(${message.id})"
>
    ${
        message.is_read
            ? "Mark Unread"
            : "Mark Read"
    }
</button>

<button
    onclick="deleteMessage(${message.id})"
>
    Delete
</button>


        </div>

        `;
    });
}


function viewMessage(id) {

    fetch(
        "http://127.0.0.1:8000/api/messages"
    )

    .then(response =>
        response.json()
    )

    .then(messages => {

        const message =
            messages.find(
                m => m.id === id
            );

        if (!message)
            return;

        alert(

            "Name: " +
            message.name +

            "\n\nEmail: " +
            message.email +

            "\n\nSubject: " +
            message.subject +

            "\n\nMessage:\n" +
            message.message
        );
    });
}


async function deleteMessage(id) {

    if (
        !confirm(
            "Delete this message?"
        )
    ) {
        return;
    }

    await fetch(

        `http://127.0.0.1:8000/api/messages/${id}`,

        {
            method: "DELETE"
        }
    );

    loadMessages();
}


async function toggleRead(id) {

    await fetch(

        `http://127.0.0.1:8000/api/messages/${id}/toggle-read`,

        {
            method: "PUT"
        }
    );

    loadMessages();
}