document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.getElementById("navbar");

    window.onscroll = function () {
        if (window.scrollY > 5) {
            navbar.classList.add("fixed");
        } else {
            navbar.classList.remove("fixed");
        }
    };
});
