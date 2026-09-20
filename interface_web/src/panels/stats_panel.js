export function initStatsPanel(container) {
  container.innerHTML = `
    <div class="stats-drawer" data-state="collapsed">
      <div class="stats-drawer__handle" role="button" tabindex="0"
           aria-label="Afficher ou masquer les statistiques">
        <span class="stats-drawer__grip"></span>
      </div>
      <div class="stats-drawer__content">
        <div class="panel">
          <h2 class="panel__title">Statistiques</h2>
          <p class="panel__subtitle">Données à venir (route /stats).</p>
          <div class="placeholder-box">
            <p class="empty">Nombre de liens parcourus, fréquence, solutions alternatives…</p>
          </div>
        </div>
      </div>
    </div>
  `;

  const drawer = container.querySelector(".stats-drawer");
  const handle = container.querySelector(".stats-drawer__handle");

  let dragging = false;
  let startX = 0;
  let startTranslate = 0;
  let maxOffset = 0;

  const decalageFerme = () => drawer.offsetWidth - handle.offsetWidth;

  function appliquerEtat(ouvert, animer = true) {
    drawer.dataset.state = ouvert ? "open" : "collapsed";
    drawer.style.transition = animer ? "transform 0.25s ease" : "none";
    drawer.style.transform = ouvert
      ? "translateX(0)"
      : `translateX(${decalageFerme()}px)`;
  }

  appliquerEtat(false, false);

  function onPointerDown(e) {
    dragging = true;
    startX = e.clientX;
    maxOffset = decalageFerme();
    startTranslate = drawer.dataset.state === "open" ? 0 : maxOffset;
    drawer.style.transition = "none";
    handle.setPointerCapture(e.pointerId);
  }

  function onPointerMove(e) {
    if (!dragging) return;
    const delta = e.clientX - startX;
    const translate = Math.min(Math.max(startTranslate + delta, 0), maxOffset);
    drawer.style.transform = `translateX(${translate}px)`;
  }

  function onPointerUp() {
    if (!dragging) return;
    dragging = false;
    const translate = new DOMMatrixReadOnly(getComputedStyle(drawer).transform).m41;
    const ouvert = translate < maxOffset * 0.6;
    appliquerEtat(ouvert);
  }

  handle.addEventListener("pointerdown", onPointerDown);
  handle.addEventListener("pointermove", onPointerMove);
  handle.addEventListener("pointerup", onPointerUp);
  handle.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") {
      appliquerEtat(drawer.dataset.state !== "open");
    }
  });

  window.addEventListener("resize", () => {
    appliquerEtat(drawer.dataset.state === "open", false);
  });
}