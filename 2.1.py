from datasets import load_dataset

dataset = load_dataset("TheFusion21/PokemonCards")
print(dataset['train'][0])

points_de_vie = [carte['hp'] for carte in dataset['train']]
print(points_de_vie)

pokemon_feu = [carte['name'] for carte in dataset['train'] if 'Fire' in carte['caption']]
print(pokemon_feu)

pokemon_stage_1 = [carte['name'] for carte in dataset['train'] if carte['caption'] == 'Stage 1']
print(pokemon_stage_1)