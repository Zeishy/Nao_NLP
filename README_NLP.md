# Workshop - Natural Language Processing

Bienvenue dans cet atelier sur les NLP ! [Mais qu'est ce qu'un NLP ?](https://letmegooglethat.com/?q=mais+Nao%2C+qu%27est+ce+qu%27un+NLP+%3F)

## 0.1 Environnement Python
Flemme de casser votre système d'exploitation et votre python ? Je vous comprends. Mon Arch Linux a hurlé, sachez-le.
Apprenez dans un premier temps à **créer un environnement python**. Appellez-moi avant de passer à l'étape suivante pour la vérification.


## 0.2 Installation

On va voir si Florian vous a bien fait votre workshop...
```
pip install transformers
pip install torch
pip install tensorflow
pip install nltk
```
Oh d'ailleurs, aurais-je oublié de vous dire que vous avez besoin d'espace dans votre pc ?

## 1.0 Test d'un modèle

Testons tout ce qu'on viens d'installer. 
- Utilisez la fonction `pipeline()` avec comme algorithme `sentiment-analysis`.
- Cette fonction une chaine de caractère, et renvoie un `Transformer`. Stockez-la dans une variable.
- Une fois ce `Transformer` stocké, utilisez ce dernier pour y mettre des phrases.
Exemple : 
```python
classifier(
    [
        "J'aime les bananes !",
        "Je déteste les poires..."
    ]
)
```
- A l'aide de toutes les étapes, vous obtenez un tableau d'objets. Faites en sorte d'obtenir uniquement un tableau de label. Ce tableau doit avoir les labels POSITIVE, NEGATIVE, POSITIVE. Arrangez vous avec les phrases que vous voulez :D

## 2.0 Fine-tuning et dataset

### 2.1 Dataset

Voici un exemple de comment charger un dataset en général avec l'API de la pipeline.
```python
from datasets import load_dataset

# Charger un jeu de données
dataset = load_dataset("imdb")
print(dataset)
```
Maintenant, utilisez cette connaissance pour charger le dataset de `TheFusion21/PokemonCards`. Afficher la première carte
du dataset.

### 2.1.1 Les caractéristiques du dataset
- Faites en sorte d'obtenir dans un tableau tous les points de vie de toutes les cartes du dataset.
- Faites en sorte d'obtenir tous les noms des Pokémon qui sont de type Feu.
- Faites en sorte d'obtenir tous les noms des Pokémon ayant évolué au moins une fois
  (c'est à dire qu'ils sont dit "Stage 1").

### 2.2 Suppression du bruit
- Faites une fonction `clean_text()`
- Cette fonction convertit un text en minuscule.
- Cette fonction enlève toute balise HTML dans le texte.
- Cette fonction enlève les caractères spéciaux inutiles.
- N'hésitez pas à utiliser les regex.

### 2.3 Tokenisation des données

Tokenisez les données nécessaires afin de nourrir le futur nouveau modèle.
Pour cela, vous utiliserez `BertTokenizer`.
```python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
```
- Prenez un texte du dataset, et tokenisez-le. Affichez le.

### 2.4 Augmentation du modèle
Pour un meilleur entrainement du modèle, trouver des synonymes de mots
peut être intéressant.
- Utilisez le code suivant afin de générer un synonyme
```python
from nltk.corpus import wordnet
# remarque : faites nltk.download(wordnet)
synonyms = wordnet.synsets(string)
```
- Faites une fonction qui génère une nouvelle phrase en parcourant chaque mots,
et en proposant un synonyme possible. Attention, la fonction peut échouer
  (vous trouvez un synonyme à Pikachu vous ?)



### 2.5 Fine-tuning d'un modèle sur classification de cartes Pokémon

Utilisez le modèle `distilbert-base-uncased` et utilisez le `Trainer` afin d'entrainer le modèle. Faites dans un premier temps avec le dataset du 2.3, 
et éventuellement faites par la suite avec votre dataset ?. N'hésitez pas à fouiller dans tous les sens.
- Modifiez vos hyper-paramètres afin d'obtenir un modèle plus précis.
- Essayez d'autres configurations
- Faites un `json` vous permettant de changer facilement de configuration. Le programme doit pouvoir lire ce dernier et utiliser ses données.
- Si déjà vous êtes là bah sincèrement, gg vous avez passé toute l'installation et les exercices tordues !

