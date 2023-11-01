// script.js
document.addEventListener("DOMContentLoaded", function () {
    var links = document.querySelectorAll("nav a");

    links.forEach(function (link) {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            alert("Vous avez cliqué sur " + link.textContent);
        });
    });
});
