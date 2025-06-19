document.addEventListener("DOMContentLoaded", function () {
  const hamburger = document.querySelector(".hamburger");
  const menu = document.querySelector(".nav-menu");
  const dropdownBtn = document.querySelector(".dropbtn");
  const dropdownContent = document.querySelector(".dropdown-content");

  if (hamburger && menu) {
    hamburger.addEventListener("click", () => {
      menu.classList.toggle("show");
    });
  }

  if (dropdownBtn && dropdownContent) {
    dropdownBtn.addEventListener("click", () => {
      dropdownContent.classList.toggle("show");
    });
  }
});
