document.addEventListener("DOMContentLoaded", () => {
    const ctas = document.querySelectorAll(".cta");
    ctas.forEach(el => {
        el.classList.add("glow");
    });
});
