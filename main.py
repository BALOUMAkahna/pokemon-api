#===== structure de donnees  : Dictionnaire indexe par pokemon id =====#
from dataclasses import dataclass ,asdict
import json
from typing import Union
from unicodedata import name
from fastapi import FastAPI ,Path ,HTTPException

with open("pokemons.json","r") as f:
    pokemons_list = json.load(f)

list_pokemons = {k+1:v for k,v in enumerate(pokemons_list)}
#========================================================
@dataclass
class Pokemon():
    id : int
    name : str
    types : list[str]
    total : int
    hp : int
    attack : int
    defense : int 
    attack_special : int
    defense_special : int
    speed : int
    evolution_id  : Union[int, None] = None

    
#========================================================

app = FastAPI()

@app.get("/total_pokemons")
def get_total_pokemons() -> dict:
    return {"total":len(list_pokemons )}

@app.get("/pokemons")
def get_all_pokemons() -> list[Pokemon]:
    res = []
    for id in list_pokemons:
        res.append(Pokemon(**list_pokemons[id]))
    return res 
@app.get("/pokemons/{id}")
def get_pokemon_by_id(id:int = Path(ge=1)) -> Pokemon:
    if id not in list_pokemons:
        raise  HTTPException(status_code=404, detail="Pokemon not found")
    return Pokemon(**list_pokemons[id] )

@app.post("/pokemon/")
def create_pokemon(pokemon : Pokemon) -> Pokemon:
    if pokemon.id in list_pokemons :
        raise HTTPException(status_code=404, detail="Pokemon {pokemon.id} existe deja")
    list_pokemons[pokemon.id] = asdict(pokemon)
    return pokemon
@app.put("/pokemon/{id}")
def update_pokemon(id:int, pokemon : Pokemon) -> Pokemon :
    if id not in list_pokemons :
        raise HTTPException(status_code=404, detail="Pokemon {id} not found")
    list_pokemons[id] = asdict(pokemon)
    return pokemon
 
@app.delete("/pokemon/{id}")
def delete_popkemon(id : int = Path(ge=1)) -> Pokemon:
    if id not in list_pokemons:
        raise HTTPException(status_code=404, detail="Pokemon {id} not found")
    deleted_pokemon = Pokemon(**list_pokemons[id])
    del list_pokemons[id]
    return deleted_pokemon 

@app.get("/types")
def get_all_types() -> list[str]:
    types = []
    for pokemon in list_pokemons:
        for type in list_pokemons[pokemon]["types"]:
            if type not in types:
                types.append(type)
    types.sort()
    return types

