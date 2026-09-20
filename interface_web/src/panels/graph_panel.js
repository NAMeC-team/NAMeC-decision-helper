import { emptyMessage } from "../components/message.js";

export function initGraphPanel(container) {
  container.innerHTML = `
    <div class="panel">
      <h2 class="panel__title">Graphe des connaissances</h2>
      <p class="panel__subtitle">Visualisation à venir (Cytoscape.js).</p>
      <div class="placeholder-box">
        ${emptyMessage("Le graphe s'affichera ici une fois la route /graph créée.")}
      </div>
    </div>
  `;
}