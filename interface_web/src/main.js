import "./styles/main.scss";
import { initRequestPanel } from "./request_panel.js";
import { initGraphPanel } from "./graph_panel.js";
import { initStatsPanel } from "./stats_panel.js";

const app = document.getElementById("app");

app.innerHTML = `
  <div class="layout">
    <section class="layout__column layout__column--request"></section>
    <section class="layout__column layout__column--graph"></section>
    <section class="layout__column layout__column--stats"></section>
  </div>
`;

initRequestPanel(app.querySelector(".layout__column--request"));
initGraphPanel(app.querySelector(".layout__column--graph"));
initStatsPanel(app.querySelector(".layout__column--stats"));