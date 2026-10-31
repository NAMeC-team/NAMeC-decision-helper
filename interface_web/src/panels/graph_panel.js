import cytoscape from "cytoscape";
import { obtenirGraphe } from "../api.js";
import { errorMessage } from "../components/message.js";

// Couleurs en dur : Cytoscape ne lit pas les variables CSS (à garder alignées avec main.scss).
const STYLE = [
  {
    selector: "node",
    style: {
      "background-color": "#accef0",
      width: 14,
      height: 14,
      label: "data(label)",
      "font-family": "Varela Round, sans-serif",
      "font-size": 10,
      color: "#16334e",
      "text-valign": "bottom",
      "text-margin-y": 4,
    },
  },
  {
    // Liens nommés (affecte, a_pour_cause...) : flèche, nom écrit au-dessus du trait
    selector: "edge",
    style: {
      width: 1.5,
      "line-color": "#707b88",
      "target-arrow-color": "#707b88",
      "target-arrow-shape": "triangle",
      "curve-style": "bezier",
      label: "data(label)",
      "font-family": "Varela Round, sans-serif",
      "font-size": 8,
      color: "#707b88",
      "text-rotation": "autorotate",
      "text-margin-y": -8,
    },
  },
  {
    // Arborescence des dossiers : trait fin, sans flèche ni nom
    selector: "edge.hierarchie",
    style: {
      width: 1,
      "line-color": "#accef0",
      "target-arrow-shape": "none",
      label: "",
    },
  },
];

export async function initGraphPanel(container) {
  container.innerHTML = `
    <div class="panel">
      <h2 class="panel__title">Graphe des connaissances</h2>
      <div class="graph-canvas"></div>
    </div>
  `;
  const canvas = container.querySelector(".graph-canvas");

  try {
    const { nodes, edges } = await obtenirGraphe();

    cytoscape({
      container: canvas,
      elements: [
        ...nodes.map((n) => ({ data: { id: n.id, label: n.nom } })),
        ...edges.map((e) => ({
          data: { source: e.source, target: e.target, label: e.label.replaceAll("_", " ") },
          classes: e.type,
        })),
      ],
      layout: { name: "cose", animate: false },
      style: STYLE,
    });
  } catch (err) {
    canvas.innerHTML = errorMessage(err.message);
  }
}