# 🔴 pokemon-api

API REST de bibliothèque Pokémon développée avec **FastAPI**. Elle expose les 151 Pokémon de la première génération (statistiques, types, évolutions) et permet d'effectuer des opérations CRUD complètes.

## Fonctionnalités

- Liste complète des Pokémon
- Recherche d'un Pokémon par son identifiant
- Création, modification et suppression d'un Pokémon
- Liste de tous les types disponibles
- Validation automatique des données
- Documentation interactive générée automatiquement (Swagger UI)

## Stack technique

- Python 3.10+
- FastAPI
- Uvicorn

## Installation

```bash
git clone https://github.com/BALOUMAkahna/pokemon-api.git
cd pokemon-api
python -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate
pip install fastapi uvicorn
```

## Lancer l'API

```bash
uvicorn main:app --reload
```

L'API est disponible sur `http://127.0.0.1:8000`.
Documentation interactive : `http://127.0.0.1:8000/docs`

## Endpoints

| Méthode | Route             | Description                    |
|---------|-------------------|--------------------------------|
| GET     | `/total_pokemons` | Nombre total de Pokémon        |
| GET     | `/pokemons`       | Liste de tous les Pokémon      |
| GET     | `/pokemons/{id}`  | Détail d'un Pokémon par son id |
| POST    | `/pokemon/`       | Créer un Pokémon               |
| PUT     | `/pokemon/{id}`   | Modifier un Pokémon            |
| DELETE  | `/pokemon/{id}`   | Supprimer un Pokémon           |
| GET     | `/types`          | Liste des types (triés)        |

## Modèle de données

```json
{
  "id": 1,
  "name": "Bulbasaur",
  "types": ["Grass", "Poison"],
  "total": 318,
  "hp": 45,
  "attack": 49,
  "defense": 49,
  "attack_special": 65,
  "defense_special": 65,
  "speed": 45,
  "evolution_id": 2
}
```

`evolution_id` est optionnel : il est absent (`null`) si le Pokémon n'a pas d'évolution.

> Certaines valeurs de `evolution_id` (169, 208, 230, 242, 462 à 467, 979) pointent vers des Pokémon des générations suivantes, qui ne sont pas présents dans cette base.

## Structure du projet

```
pokemon-api/
├── main.py          # Application FastAPI
├── pokemons.json    # Données des Pokémon
├── .gitignore
└── README.md
```

## Remarque

Les données sont chargées en mémoire au démarrage depuis `pokemons.json`. Les modifications effectuées via POST, PUT et DELETE ne sont donc **pas conservées** après un redémarrage du serveur.

## Pistes d'amélioration

- Persistance des données (SQLite / PostgreSQL)
- Filtres par type et pagination
- Recherche par nom
- Tests unitaires avec `pytest`

## Auteur

[BALOUMAkahna](https://github.com/BALOUMAkahna)
