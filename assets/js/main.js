(function () {
  /* Fotky, které se nenačtou, se skryjí a zůstane jen plocha rámu ---- */
  document.querySelectorAll(".ram img, .karta img").forEach(function (img) {
    function skryj() { img.classList.add("nenacteno"); }
    if (img.complete && img.naturalWidth === 0 && img.getAttribute("src")) skryj();
    else img.addEventListener("error", skryj);
  });

  /* Mobilní menu ------------------------------------------------ */
  var tlacitko = document.querySelector(".menu-btn");
  var menu = document.getElementById("menu");

  function nastavMenu(otevrit) {
    if (!tlacitko || !menu) return;
    tlacitko.setAttribute("aria-expanded", otevrit ? "true" : "false");
    tlacitko.querySelector("span").textContent = otevrit ? tlacitko.dataset.zavrit : tlacitko.dataset.otevrit;
    tlacitko.querySelector("use").setAttribute("href", otevrit ? "#i-x" : "#i-menu-2");
    menu.classList.toggle("je-otevrene", otevrit);
  }

  if (tlacitko && menu) {
    tlacitko.addEventListener("click", function () {
      nastavMenu(tlacitko.getAttribute("aria-expanded") !== "true");
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) nastavMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && tlacitko.getAttribute("aria-expanded") === "true") {
        nastavMenu(false);
        tlacitko.focus();
      }
    });
    window.matchMedia("(min-width: 960px)").addEventListener("change", function (mq) {
      if (mq.matches) nastavMenu(false);
    });
  }

  /* Lišta se po odscrollování přilepí nahoru jako olivová pilulka ---- */
  var lista = document.querySelector("[data-lista]");
  if (lista) {
    var misto = document.createElement("div");
    lista.parentNode.insertBefore(misto, lista);
    var naScroll = function () {
      var lepi = lista.classList.contains("lista-obal--lepi");
      var hranice = misto.getBoundingClientRect().top + window.scrollY + 400;
      var maLepit = window.scrollY > hranice;
      if (maLepit === lepi) return;
      if (maLepit) misto.style.height = lista.offsetHeight + "px";
      else misto.style.height = "";
      lista.classList.toggle("lista-obal--lepi", maLepit);
    };
    naScroll();
    window.addEventListener("scroll", naScroll, { passive: true });
    window.addEventListener("resize", naScroll);
  }

  var rok = document.querySelector("[data-rok]");
  if (rok) rok.textContent = new Date().getFullYear();

  /* Poptávka: sestaví e-mail s vyplněnými údaji ------------------ */
  var CIL = "drahosova@baumat-brno.cz";
  document.querySelectorAll("[data-poptavka]").forEach(function (form) {
    var prijezd = form.elements.prijezd;
    var odjezd = form.elements.odjezd;
    var dnes = new Date();
    var dnesKlic = dnes.getFullYear() + "-" + String(dnes.getMonth() + 1).padStart(2, "0") + "-" + String(dnes.getDate()).padStart(2, "0");
    prijezd.min = dnesKlic;
    odjezd.min = dnesKlic;
    prijezd.addEventListener("change", function () {
      odjezd.min = prijezd.value || dnesKlic;
      if (odjezd.value && odjezd.value < prijezd.value) odjezd.value = "";
    });

    function cesky(d) {
      if (!d) return "";
      var p = d.split("-");
      return +p[2] + ". " + +p[1] + ". " + p[0];
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var typ = form.elements.typ.value;
      var predmet = "Poptávka: " + typ + ", " + cesky(prijezd.value) + " až " + cesky(odjezd.value);
      var telo =
        "Dobrý den,\n\nposílám poptávku termínu v areálu Baumat Heroltice.\n\n" +
        "Typ akce: " + typ + "\n" +
        "Příjezd: " + cesky(prijezd.value) + "\n" +
        "Odjezd: " + cesky(odjezd.value) + "\n" +
        "Počet osob: " + form.elements.osob.value + "\n\n" +
        "Děkuji\n";
      window.location.href = "mailto:" + CIL + "?subject=" + encodeURIComponent(predmet) + "&body=" + encodeURIComponent(telo);
    });
  });

  /* Prohlížeč fotek --------------------------------------------- */
  var galerie = document.querySelectorAll("[data-galerie]");
  if (galerie.length && window.HTMLDialogElement) {
    var dialog = document.createElement("dialog");
    dialog.className = "lightbox";
    dialog.setAttribute("aria-label", "Prohlížeč fotek");
    dialog.innerHTML =
      '<div class="lightbox__plocha">' +
      '  <div class="lightbox__horni">' +
      "    <span data-lb-nazev></span>" +
      '    <button class="lightbox__tlacitko" type="button" data-lb-zavrit aria-label="Zavřít fotky">' +
      '      <svg class="i" aria-hidden="true"><use href="#i-x"/></svg></button>' +
      "  </div>" +
      '  <div class="lightbox__obraz"><img alt="" data-lb-obraz></div>' +
      '  <div class="lightbox__spodni">' +
      '    <button class="lightbox__tlacitko" type="button" data-lb-zpet aria-label="Předchozí fotka">' +
      '      <svg class="i" aria-hidden="true" style="transform:rotate(180deg)"><use href="#i-arrow-right"/></svg></button>' +
      '    <p class="lightbox__popisek"><span data-lb-popis></span><br><span data-lb-pocet></span></p>' +
      '    <button class="lightbox__tlacitko" type="button" data-lb-vpred aria-label="Další fotka">' +
      '      <svg class="i" aria-hidden="true"><use href="#i-arrow-right"/></svg></button>' +
      "  </div>" +
      "</div>";
    document.body.appendChild(dialog);

    var obraz = dialog.querySelector("[data-lb-obraz]");
    var nazevEl = dialog.querySelector("[data-lb-nazev]");
    var popisEl = dialog.querySelector("[data-lb-popis]");
    var pocetEl = dialog.querySelector("[data-lb-pocet]");
    var fotky = [];
    var index = 0;
    var nazev = "";

    function vykresli() {
      var f = fotky[index];
      obraz.src = f.src;
      obraz.alt = f.alt;
      nazevEl.textContent = nazev;
      popisEl.textContent = f.alt;
      pocetEl.textContent = index + 1 + " z " + fotky.length;
      var vice = fotky.length > 1;
      dialog.querySelector("[data-lb-zpet]").hidden = !vice;
      dialog.querySelector("[data-lb-vpred]").hidden = !vice;
    }

    function posun(o) {
      index = (index + o + fotky.length) % fotky.length;
      vykresli();
    }

    galerie.forEach(function (blok) {
      var obrazky = [].map.call(blok.querySelectorAll("img"), function (img) {
        return { src: img.currentSrc || img.src, alt: img.alt };
      });
      blok.querySelectorAll(".foto-btn").forEach(function (btn, i) {
        btn.addEventListener("click", function () {
          fotky = obrazky;
          index = i;
          nazev = blok.dataset.galerie || "";
          vykresli();
          dialog.showModal();
        });
      });
    });

    dialog.querySelector("[data-lb-zavrit]").addEventListener("click", function () { dialog.close(); });
    dialog.querySelector("[data-lb-zpet]").addEventListener("click", function () { posun(-1); });
    dialog.querySelector("[data-lb-vpred]").addEventListener("click", function () { posun(1); });
    dialog.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { e.preventDefault(); posun(1); }
      if (e.key === "ArrowLeft") { e.preventDefault(); posun(-1); }
    });
    dialog.addEventListener("click", function (e) {
      if (e.target === dialog || e.target.classList.contains("lightbox__obraz")) dialog.close();
    });
  }

  /* Kalendář obsazenosti ---------------------------------------- */
  var kalendar = document.querySelector("[data-kalendar]");
  if (kalendar) {
    var MESICE = ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"];
    var DNY = ["po", "út", "st", "čt", "pá", "so", "ne"];
    var STAVY = { obsazeno: "obsazeno", castecne: "částečně obsazeno", volno: "volno" };

    var mrizka = kalendar.querySelector("[data-kalendar-mrizka]");
    var popisek = kalendar.querySelector("[data-kalendar-mesic]");
    var zpet = kalendar.querySelector("[data-kalendar-zpet]");
    var vpred = kalendar.querySelector("[data-kalendar-vpred]");
    var den0 = new Date();
    den0.setHours(0, 0, 0, 0);
    var zobrazeny = new Date(den0.getFullYear(), den0.getMonth(), 1);
    var obsazenost = {};

    function klic(d) {
      return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
    }

    function vykresliMesic() {
      popisek.textContent = MESICE[zobrazeny.getMonth()] + " " + zobrazeny.getFullYear();
      mrizka.innerHTML = "";

      DNY.forEach(function (d) {
        var h = document.createElement("div");
        h.className = "kalendar__den-nazev";
        h.setAttribute("aria-hidden", "true");
        h.textContent = d;
        mrizka.appendChild(h);
      });

      var prvni = new Date(zobrazeny.getFullYear(), zobrazeny.getMonth(), 1);
      var posunDne = (prvni.getDay() + 6) % 7;
      var pocetDnu = new Date(zobrazeny.getFullYear(), zobrazeny.getMonth() + 1, 0).getDate();

      for (var i = 0; i < posunDne; i++) {
        var prazdno = document.createElement("div");
        prazdno.className = "kalendar__den kalendar__den--prazdny";
        mrizka.appendChild(prazdno);
      }

      for (var den = 1; den <= pocetDnu; den++) {
        var datum = new Date(zobrazeny.getFullYear(), zobrazeny.getMonth(), den);
        var stav = obsazenost[klic(datum)] || "volno";
        var bunka = document.createElement("div");
        bunka.className = "kalendar__den kalendar__den--" + stav;
        if (datum < den0) bunka.classList.add("kalendar__den--minuly");
        if (datum.getTime() === den0.getTime()) bunka.classList.add("kalendar__den--dnes");
        bunka.innerHTML = "<span>" + den + "</span>";
        var slovy = datum.toLocaleDateString("cs-CZ", { day: "numeric", month: "long", year: "numeric" });
        bunka.setAttribute("aria-label", slovy + ", " + (STAVY[stav] || "volno"));
        mrizka.appendChild(bunka);
      }

      zpet.disabled = zobrazeny <= new Date(den0.getFullYear(), den0.getMonth(), 1);
    }

    zpet.addEventListener("click", function () {
      zobrazeny = new Date(zobrazeny.getFullYear(), zobrazeny.getMonth() - 1, 1);
      vykresliMesic();
    });
    vpred.addEventListener("click", function () {
      zobrazeny = new Date(zobrazeny.getFullYear(), zobrazeny.getMonth() + 1, 1);
      vykresliMesic();
    });

    vykresliMesic();

    // Obsazenost se čte z assets/data/obsazenost.json.
    // Ten je zatím ruční; po napojení Google Calendar API ho bude generovat export.
    fetch(kalendar.dataset.kalendar)
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (data) {
        if (!data || !data.terminy) return;
        obsazenost = data.terminy;
        vykresliMesic();
      })
      .catch(function () { /* bez dat zůstanou všechny dny volné */ });
  }
})();
