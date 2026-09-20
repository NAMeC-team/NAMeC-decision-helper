export function initStatsPanel(container) {
  container.innerHTML = `
    <div class="panel">
      <h2 class="panel__title">Statistiques</h2>
      <p class="panel__subtitle">Données à venir (route /stats).</p>
      <div class="placeholder-box">
        <p class="empty">Nombre de liens parcourus, fréquence, solutions alternatives…</p>
      </div>
    </div>
  `;
}