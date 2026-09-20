export function solutionCard({ cause, action }) {
  return `
    <div class="solution">
      <div class="solution__cause">${cause}</div>
      <div class="solution__action">${action}</div>
    </div>
  `;
}