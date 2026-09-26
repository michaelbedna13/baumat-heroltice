(function () {
  /* Texty podle jazyka stránky (html lang="cs" nebo "en") ------------ */
  var EN = document.documentElement.lang === "en";
  var T = EN
    ? { prohlizec: "Photo viewer", zavrit: "Close photos", zpet: "Previous photo", vpred: "Next photo", z: " of ",
        mesice: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        dny: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        stavy: { obsazeno: "booked", castecne: "partially booked", volno: "available" }, locale: "en-GB" }
    : { prohlizec: "Prohlížeč fotek", zavrit: "Zavřít fotky", zpet: "Předchozí fotka", vpred: "Další fotka", z: " z ",
        mesice: ["leden", "únor", "březen", "duben", "květen", "červen", "červenec", "srpen", "září", "říjen", "listopad", "prosinec"],
        dny: ["po", "út", "st", "čt", "pá", "so", "ne"],
        stavy: { obsazeno: "obsazeno", castecne: "částečně obsazeno", volno: "volno" }, locale: "cs-CZ" };

  /* Fotky, které se nenačtou, se skryjí a zůstane jen plocha rámu ---- */
  document.querySelectorAll(".ram img, .karta img, .hero__foto img").forEach(function (img) {
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

  /* Vybavení v kartách ubytování: na desktopu vždy rozbalené, na mobilu sbalené */
  var vybaveni = document.querySelectorAll(".detail__vybaveni");
  if (vybaveni.length) {
    var desktop = window.matchMedia("(min-width: 960px)");
    var nastavVybaveni = function () {
      vybaveni.forEach(function (d) { d.open = desktop.matches; });
    };
    nastavVybaveni();
    desktop.addEventListener("change", nastavVybaveni);
    vybaveni.forEach(function (d) {
      d.querySelector("summary").addEventListener("click", function (e) {
        if (desktop.matches) e.preventDefault();
      });
    });
  }

  /* Kolotoč recenzí ---------------------------------------------- */
  var kolotoc = document.querySelector("[data-kolotoc]");
  if (kolotoc) {
    var pas = kolotoc.querySelector(".kolotoc__pas");
    var zpetK = kolotoc.querySelector("[data-kolotoc-zpet]");
    var vpredK = kolotoc.querySelector("[data-kolotoc-vpred]");
    var puvodni = [].slice.call(pas.children);
    var pocet = puvodni.length;

    // Nekonečná smyčka: kopie všech karet před i za originály. Když se dojede do kopií,
    // posun se nepozorovaně vrátí o jednu celou sadu zpět.
    var kopie = function (el) {
      var k = el.cloneNode(true);
      k.setAttribute("aria-hidden", "true");
      k.setAttribute("inert", "");
      k.classList.add("recenze__karta--kopie");
      return k;
    };
    if (pocet > 1) {
      puvodni.slice().reverse().forEach(function (el) { pas.insertBefore(kopie(el), pas.firstChild); });
      puvodni.forEach(function (el) { pas.appendChild(kopie(el)); });
    }
    var odsazeni = function () { return parseFloat(getComputedStyle(pas).paddingLeft) || 0; };
    var zacatekSady = function () { return puvodni[0].offsetLeft - odsazeni(); };
    var sirkaSady = function () { return pocet > 1 ? pas.children[pocet * 2].offsetLeft - puvodni[0].offsetLeft : 0; };
    var krok = function () {
      var mezera = parseFloat(getComputedStyle(pas).columnGap) || 0;
      return puvodni[0].getBoundingClientRect().width + mezera;
    };
    var skok = function (x) {
      pas.classList.add("kolotoc__pas--bez-snapu");
      pas.scrollLeft = x;
      requestAnimationFrame(function () { pas.classList.remove("kolotoc__pas--bez-snapu"); });
    };
    var hlidatKonce = function () {
      if (pocet < 2 || tah) return;
      var z = zacatekSady(), w = sirkaSady();
      if (pas.scrollLeft < z - w / 2) skok(pas.scrollLeft + w);
      else if (pas.scrollLeft > z + w * 1.5) skok(pas.scrollLeft - w);
    };
    var casovac;
    pas.addEventListener("scroll", function () {
      clearTimeout(casovac);
      casovac = setTimeout(hlidatKonce, 140);
    }, { passive: true });
    var naZacatek = function () { skok(zacatekSady()); };
    naZacatek();
    window.addEventListener("resize", naZacatek);

    var posunK = function (smer) { pas.scrollBy({ left: smer * krok(), behavior: "smooth" }); };
    zpetK.addEventListener("click", function () { posunK(-1); });
    vpredK.addEventListener("click", function () { posunK(1); });

    // tahání myší (prst a touchpad posouvají nativně)
    var tah = null;
    var blokovatKlik = false;
    pas.addEventListener("pointerdown", function (e) {
      if (e.pointerType !== "mouse" || e.button !== 0) return;
      tah = { x: e.clientX, start: pas.scrollLeft, pohyb: false, id: e.pointerId };
    });
    pas.addEventListener("pointermove", function (e) {
      if (!tah) return;
      var dx = e.clientX - tah.x;
      if (!tah.pohyb && Math.abs(dx) > 5) {
        tah.pohyb = true;
        pas.classList.add("kolotoc__pas--tah");
        pas.setPointerCapture(tah.id);
      }
      if (tah.pohyb) pas.scrollLeft = tah.start - dx;
    });
    var konecTahu = function () {
      if (!tah) return;
      var pohyb = tah.pohyb;
      tah = null;
      if (!pohyb) return;
      blokovatKlik = true;
      var k = krok(), z = pas.children[0].offsetLeft - odsazeni();
      var cil = z + Math.round((pas.scrollLeft - z) / k) * k;
      pas.classList.remove("kolotoc__pas--tah");
      pas.classList.add("kolotoc__pas--bez-snapu");
      pas.scrollTo({ left: cil, behavior: "smooth" });
      setTimeout(function () { pas.classList.remove("kolotoc__pas--bez-snapu"); hlidatKonce(); }, 450);
    };
    pas.addEventListener("pointerup", konecTahu);
    pas.addEventListener("pointercancel", konecTahu);
    pas.addEventListener("click", function (e) {
      if (blokovatKlik) { e.preventDefault(); e.stopPropagation(); blokovatKlik = false; }
    }, true);
    pas.addEventListener("dragstart", function (e) { e.preventDefault(); });

    // pomalé automatické posouvání, zastaví se pod myší, při fokusu a po dotyku
    var klid = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var pauza = false;
    ["mouseenter", "focusin", "touchstart"].forEach(function (ev) { kolotoc.addEventListener(ev, function () { pauza = true; }, { passive: true }); });
    kolotoc.addEventListener("mouseleave", function () { pauza = false; });
    if (!klid && pocet > 1) setInterval(function () { if (!pauza && !document.hidden) posunK(1); }, 7000);

    kolotoc.querySelectorAll(".recenze__vice").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var karta = btn.closest(".recenze__karta");
        var otevrit = !karta.classList.contains("recenze__karta--cela");
        karta.classList.toggle("recenze__karta--cela", otevrit);
        btn.setAttribute("aria-expanded", otevrit ? "true" : "false");
        btn.textContent = otevrit ? btn.dataset.mene : btn.dataset.vice;
        pauza = true;
      });
    });
  }

  var rok = document.querySelector("[data-rok]");
  if (rok) rok.textContent = new Date().getFullYear();

  /* Počet fotek na štítku galerie (počítá i fotky schované pro prohlížeč) */
  document.querySelectorAll("[data-galerie]").forEach(function (blok) {
    var stitek = blok.querySelector(".lupa");
    if (!stitek) return;
    var n = blok.querySelectorAll("img").length;
    var text = EN ? (n > 1 ? n + " photos" : "Enlarge")
                  : (n === 1 ? "Zvětšit" : n < 5 ? n + " fotky" : n + " fotek");
    var uzel = stitek.lastChild;
    if (uzel && uzel.nodeType === 3) uzel.textContent = text;
  });

  /* Prohlížeč fotek --------------------------------------------- */
  var galerie = document.querySelectorAll("[data-galerie]");
  if (galerie.length && window.HTMLDialogElement) {
    var dialog = document.createElement("dialog");
    dialog.className = "lightbox";
    dialog.setAttribute("aria-label", T.prohlizec);
    dialog.innerHTML =
      '<div class="lightbox__plocha">' +
      '  <div class="lightbox__horni">' +
      "    <span data-lb-nazev></span>" +
      '    <button class="lightbox__tlacitko" type="button" data-lb-zavrit aria-label="' + T.zavrit + '">' +
      '      <svg class="i" aria-hidden="true"><use href="#i-x"/></svg></button>' +
      "  </div>" +
      '  <div class="lightbox__obraz"><img alt="" data-lb-obraz></div>' +
      '  <div class="lightbox__spodni">' +
      '    <button class="lightbox__tlacitko" type="button" data-lb-zpet aria-label="' + T.zpet + '">' +
      '      <svg class="i" aria-hidden="true" style="transform:rotate(180deg)"><use href="#i-arrow-right"/></svg></button>' +
      '    <p class="lightbox__popisek"><span data-lb-popis></span><br><span data-lb-pocet></span></p>' +
      '    <button class="lightbox__tlacitko" type="button" data-lb-vpred aria-label="' + T.vpred + '">' +
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
      pocetEl.textContent = index + 1 + T.z + fotky.length;
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
    var MESICE = T.mesice;
    var DNY = T.dny;
    var STAVY = T.stavy;

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
        var slovy = datum.toLocaleDateString(T.locale, { day: "numeric", month: "long", year: "numeric" });
        bunka.setAttribute("aria-label", slovy + ", " + (STAVY[stav] || STAVY.volno));
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
        var aktual = document.querySelector("[data-kalendar-aktualizace]");
        if (aktual && data.aktualizovano) {
          var d = new Date(data.aktualizovano + "T12:00:00");
          aktual.textContent = (EN ? "Last updated " : "Aktualizováno ") + d.toLocaleDateString(T.locale, { day: "numeric", month: "numeric", year: "numeric" });
          aktual.hidden = false;
        }
        vykresliMesic();
      })
      .catch(function () { /* bez dat zůstanou všechny dny volné */ });
  }
})();
