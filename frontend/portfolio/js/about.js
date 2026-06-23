document.addEventListener(
    "DOMContentLoaded",
    loadAbout
);

async function loadAbout() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/about/"
            );

        const data =
            await response.json();

        if(data.length === 0)
            return;

        const about =
            data[data.length - 1];

        document.getElementById(
            "aboutLocation"
        ).innerText =
            "📍 " + about.location;

        document.getElementById(
            "aboutEmail"
        ).innerText =
            "✉️ " + about.email;

        document.getElementById(
            "aboutPhone"
        ).innerText =
            "📞 " + about.phone;

        document.getElementById(
            "aboutEducation"
        ).innerText =
            about.education;

        document.getElementById(
            "aboutSummary"
        ).innerText =
            about.summary;

        document.getElementById(
            "aboutJourney"
        ).innerText =
            about.journey;

        document.getElementById(
            "aboutImage"
        ).src =
            "http://127.0.0.1:8000" +
            about.image_url;

    }

    catch(error) {

        console.error(error);
    }
}
