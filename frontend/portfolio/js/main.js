/* File: frontend/portfolio/js/main.js */

/*
=========================================
MAIN WEBSITE FUNCTIONALITY
=========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    initializeSmoothScrolling();

    initializeActiveNavigation();

    initializeNavbarShadow();

});

/*
=========================================
SMOOTH SCROLLING
=========================================
*/

function initializeSmoothScrolling() {

    const navLinks = document.querySelectorAll('a[href^="#"]');

    navLinks.forEach(link => {

        link.addEventListener("click", function (event) {

            event.preventDefault();

            const targetId = this.getAttribute("href");

            const targetSection = document.querySelector(targetId);

            if (targetSection) {

                targetSection.scrollIntoView({
                    behavior: "smooth"
                });

            }

        });

    });

}

/*
=========================================
ACTIVE NAVIGATION LINK
=========================================
*/

function initializeActiveNavigation() {

    const sections = document.querySelectorAll("section");

    const navLinks = document.querySelectorAll(".nav-links a");

    window.addEventListener("scroll", () => {

        let currentSection = "";

        sections.forEach(section => {

            const sectionTop = section.offsetTop - 150;

            const sectionHeight = section.clientHeight;

            if (window.scrollY >= sectionTop) {

                currentSection = section.getAttribute("id");

            }

        });

        navLinks.forEach(link => {

            link.classList.remove("active");

            if (
                link.getAttribute("href") ===
                `#${currentSection}`
            ) {
                link.classList.add("active");
            }

        });

    });

}

/*
=========================================
NAVBAR SHADOW EFFECT
=========================================
*/

function initializeNavbarShadow() {

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", () => {

        if (window.scrollY > 50) {

            navbar.style.boxShadow =
                "0 10px 30px rgba(0,0,0,0.12)";

        } else {

            navbar.style.boxShadow =
                "0 10px 30px rgba(0,0,0,0.08)";
        }

    });

}

window.addEventListener(
    "load",
    () => {

        const loader =
            document.getElementById(
                "loader"
            );

        if (loader) {

            loader.style.display =
                "none";
        }
    }
);