const API_BASE_URL = "http://127.0.0.1:8000";

export async function listerSymptomes() {
  const reponse = await fetch(`${API_BASE_URL}/symptomes`);
  if (!reponse.ok) {
    throw new Error("Impossible de récupérer la liste des symptômes.");
  }
  return reponse.json();
}

export async function resoudreSymptome(slug) {
  const reponse = await fetch(`${API_BASE_URL}/solve/${slug}`);
  if (reponse.status === 404) {
    throw new Error("Aucune solution connue pour ce symptôme.");
  }
  if (!reponse.ok) {
    throw new Error("Erreur lors de la résolution du symptôme.");
  }
  return reponse.json();
}