import { listerSymptomes, resoudreSymptome } from "./api.js";

export async function initRequestPanel(container) {
  container.innerHTML = `
    <div class="panel">
      <h1 class="panel__title">Aide au diagnostic NAMeC</h1>
      <p class="panel__subtitle">Sélectionne le symptôme observé sur le robot.</p>

      <div class="field">
        <label for="symptome-select">Symptôme</label>
        <select id="symptome-select">
          <option value="">Chargement…</option>
        </select>
      </div>

      <button id="diagnostiquer-btn" disabled>Diagnostiquer</button>

      <div id="result" class="result" hidden></div>
    </div>
  `;

  const select = container.querySelector("#symptome-select");
  const bouton = container.querySelector("#diagnostiquer-btn");
  const resultEl = container.querySelector("#result");

  try {
    const symptomes = await listerSymptomes();
    select.innerHTML = symptomes
      .map((s) => `<option value="${s.slug}">${s.label}</option>`)
      .join("");
    bouton.disabled = false;
  } catch (err) {
    select.innerHTML = `<option value="">Erreur de chargement</option>`;
    afficherErreur(resultEl, err.message);
  }

  bouton.addEventListener("click", async () => {
    const slug = select.value;
    if (!slug) return;

    bouton.disabled = true;
    bouton.textContent = "Recherche…";

    try {
      const diagnostic = await resoudreSymptome(slug);
      afficherResultat(resultEl, diagnostic);
    } catch (err) {
      afficherErreur(resultEl, err.message);
    } finally {
      bouton.disabled = false;
      bouton.textContent = "Diagnostiquer";
    }
  });
}

function afficherResultat(resultEl, diagnostic) {
  resultEl.hidden = false;

  const composantsHtml = diagnostic.composants_affectes
    .map((c) => `<span class="chip">${c}</span>`)
    .join("");

  const solutionsHtml = diagnostic.solutions.length
    ? diagnostic.solutions
        .map(
          (s) => `
        <div class="solution">
          <div class="solution__cause">${s.cause}</div>
          <div class="solution__action">${s.action}</div>
        </div>
      `
        )
        .join("")
    : `<p class="empty">Aucune solution connue pour ce symptôme pour l'instant.</p>`;

  resultEl.innerHTML = `
    <div class="result__composants">${composantsHtml}</div>
    ${solutionsHtml}
    <p class="result__meta">
      ${diagnostic.nb_solutions_alternatives} solution(s) alternative(s) trouvée(s)
    </p>
  `;
}

function afficherErreur(resultEl, message) {
  resultEl.hidden = false;
  resultEl.innerHTML = `<p class="error">${message}</p>`;
}