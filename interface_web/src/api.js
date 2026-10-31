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

export async function obtenirGraphe() {
  const reponse = await fetch(`${API_BASE_URL}/graph`);
  if (!reponse.ok) throw new Error("Impossible de récupérer le graphe, ahaaa, dommaaaage... Comment faire ? Demander à Wanchaï ? Non non non. Demander à Anaelle, qui vous dira, mais qu'est-ce que vous avez fait encore ! Vous avez bien complété la doc, j'espère ?")
  return reponse.json();
}