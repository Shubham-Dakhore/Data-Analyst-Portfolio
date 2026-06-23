document.addEventListener(
    "DOMContentLoaded",
    loadHero
);

async function loadHero() {

    try {

        const data =
            await apiGet(
                "/api/hero/"
            );

        if (!data.length) {

            console.warn(
                "No hero data found"
            );

            return;
        }

        const hero =
            data[0];

        document.getElementById(
            "heroName"
        ).textContent =
            hero.full_name || "";

        document.getElementById(
            "heroProfession"
        ).textContent =
            hero.profession || "";

        document.getElementById(
            "heroBio"
        ).textContent =
            hero.short_bio || "";

        const linkedin =
            document.getElementById(
                "linkedinLink"
            );

        if (hero.linkedin_url) {
            linkedin.href =
                hero.linkedin_url;
        } else {
            linkedin.style.display =
                "none";
        }

        const github =
            document.getElementById(
                "githubLink"
            );

        if (hero.github_url) {
            github.href =
                hero.github_url;
        } else {
            github.style.display =
                "none";
        }

        const email =
            document.getElementById(
                "emailLink"
            );

        if (hero.email) {
            email.href =
                `mailto:${hero.email}`;
        } else {
            email.style.display =
                "none";
        }

        const profileImage =
            document.getElementById(
                "heroProfileImage"
            );

        profileImage.src =
            hero.profile_image
                ? `${API_BASE_URL}${hero.profile_image}`
                : "images/default-profile.png";

        profileImage.alt =
            hero.full_name;

        document.title =
            `${hero.full_name} | ${hero.profession}`;

    }

    catch (error) {

        console.error(
            "Hero Load Error:",
            error
        );
    }
}