/* File: frontend/js/resume.js */

document.addEventListener(
    "DOMContentLoaded",
    loadResume
);

async function loadResume() {

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/api/resume/"
            );

        const data =
            await response.json();

        if (data.length === 0) {
            return;
        }

        const resume =
            data[0];

        const resumeUrl =
            "http://127.0.0.1:8000" +
            resume.file_url;

        const previewFrame =
            document.getElementById(
                "resumePreviewFrame"
            );

        if (previewFrame) {

            previewFrame.src =
                resumeUrl;
        }


        const heroBtn =
            document.getElementById(
                "heroResumeBtn"
            );

        const resumeBtn =
            document.getElementById(
                "resumeDownloadBtn"
            );

        if (heroBtn) {
            heroBtn.href = resumeUrl;
        }

        if (resumeBtn) {
            resumeBtn.href = resumeUrl;
        }

    } catch (error) {

        console.error(
            "Resume Load Error:",
            error
        );
    }
}