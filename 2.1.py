from datasets import load_dataset

dataset = load_dataset("TheFusion21/PokemonCards")
print(dataset['train'][0])

print("-----------------------------------------------------------------------------------------")

points_de_vie = [carte['hp'] for carte in dataset['train']]
print(points_de_vie)

print("-----------------------------------------------------------------------------------------")

pokemon_feu = [carte['name'] for carte in dataset['train'] if 'Fire' in carte['caption']]
print(pokemon_feu)

print("-----------------------------------------------------------------------------------------")

pokemon_stage_1 = [carte['name'] for carte in dataset['train'] if 'Stage 1' in carte['caption']]
print(pokemon_stage_1)

print("-----------------------------------------------------------------------------------------")

pokemon_stage_2 = [carte['name'] for carte in dataset['train'] if 'Stage 2' in carte['caption']]
print(pokemon_stage_2)

print("-----------------------------------------------------------------------------------------")
