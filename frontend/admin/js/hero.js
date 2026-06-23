document
.addEventListener(
    "DOMContentLoaded",
    setupHeroForm
);

function setupHeroForm() {

    const form =
        document.getElementById(
            "heroForm"
        );

    if(!form) return;

    form.addEventListener(
        "submit",
        saveHero
    );
}

async function saveHero(event) {

    event.preventDefault();

    let imageUrl = "";

    const imageInput =
        document.getElementById(
            "heroImage"
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
                "http://127.0.0.1:8000/api/upload/hero-image",
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

    const heroData = {

        full_name:
            heroName.value,

        profession:
            heroProfession.value,

        short_bio:
            heroBio.value,

        linkedin_url:
            heroLinkedin.value,

        github_url:
            heroGithub.value,

        email:
            heroEmail.value,

        profile_image:
            imageUrl
    };

    await fetch(
        "http://127.0.0.1:8000/api/hero/",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body:
            JSON.stringify(heroData)
        }
    );

    alert(
        "Hero Updated"
    );
}