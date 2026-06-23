async function loadAbout() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/about/"
            );

        const data =
            await response.json();

        if (data.length === 0)
            return;

        const about = data[0];

        document.getElementById(
            "aboutLocation"
        ).value = about.location || "";

        document.getElementById(
            "aboutEmail"
        ).value = about.email || "";

        document.getElementById(
            "aboutPhone"
        ).value = about.phone || "";

        document.getElementById(
            "aboutEducation"
        ).value = about.education || "";

        document.getElementById(
            "aboutSummary"
        ).value = about.summary || "";

        document.getElementById(
            "aboutJourney"
        ).value = about.journey || "";

    }

    catch(error) {

        console.error(error);
    }
}


document
.getElementById("aboutForm")
.addEventListener(
    "submit",
    async function(e) {

        e.preventDefault();

        try {

            const imageFile =
                document.getElementById(
                    "aboutImageUpload"
                ).files[0];

            let imageUrl = "";

            if (imageFile) {

                const imageForm =
                    new FormData();

                imageForm.append(
                    "image",
                    imageFile
                );

                const uploadResponse =
                    await fetch(
                        "http://127.0.0.1:8000/api/upload/about-image",
                        {
                            method: "POST",
                            body: imageForm
                        }
                    );

                if (!uploadResponse.ok) {

                    throw new Error(
                        "Image upload failed"
                    );
                }

                const uploadData =
                    await uploadResponse.json();

                imageUrl =
                    uploadData.image_url;
            }

            const data = {

                location:
                    document.getElementById(
                        "aboutLocation"
                    ).value,

                email:
                    document.getElementById(
                        "aboutEmail"
                    ).value,

                phone:
                    document.getElementById(
                        "aboutPhone"
                    ).value,

                education:
                    document.getElementById(
                        "aboutEducation"
                    ).value,

                summary:
                    document.getElementById(
                        "aboutSummary"
                    ).value,

                journey:
                    document.getElementById(
                        "aboutJourney"
                    ).value,

                image_url:
                    imageUrl
            };

            const response =
                await fetch(
                    "http://127.0.0.1:8000/api/about/",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(
                                data
                            )
                    }
                );

            if (!response.ok) {

                throw new Error(
                    "Failed to update About section"
                );
            }

            alert(
                "About Updated Successfully"
            );

        }

        catch(error) {

            console.error(error);

            alert(
                error.message
            );
        }

    }
);

loadAbout();