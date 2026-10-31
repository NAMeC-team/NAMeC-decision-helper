export function solutionCard({ cause, action, description }) {
  return `
    <div class="solution">
      <div class="solution__cause">${cause}</div>
      <div class="solution__action">${action}</div>
      ${description ? `<p class="solution__description">${description}</p>` : ""}
    </div>
  `;
}