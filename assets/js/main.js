(function () {
  var hlavicka = document.querySelector(".hlavicka");
  var burger = document.querySelector(".burger");
  var menu = document.getElementById("menu");

  function nastavMenu(otevrit) {
    if (!burger || !menu) return;
    burger.setAttribute("aria-expanded", otevrit ? "true" : "false");
    burger.setAttribute("aria-label", otevrit ? burger.dataset.zavrit : burger.dataset.otevrit);
    burger.querySelector("use").setAttribute("href", otevrit ? "#i-x" : "#i-menu-2");
    menu.classList.toggle("je-otevrene", otevrit);
    document.body.classList.toggle("menu-otevrene", otevrit);
  }

  if (burger && menu) {
    burger.addEventListener("click", function () {
      nastavMenu(burger.getAttribute("aria-expanded") !== "true");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) nastavMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && burger.getAttribute("aria-expanded") === "true") {
        nastavMenu(false);
        burger.focus();
      }
    });
    window.matchMedia("(min-width: 961px)").addEventListener("change", function (mq) {
      if (mq.matches) nastavMenu(false);
    });
  }

  if (hlavicka) {
    var naScroll = function () {
      hlavicka.classList.toggle("je-odscrollovano", window.scrollY > 40);
    };
    naScroll();
    window.addEventListener("scroll", naScroll, { passive: true });
  }

  var rok = document.querySelector("[data-rok]");
  if (rok) rok.textContent = new Date().getFullYear();
})();
