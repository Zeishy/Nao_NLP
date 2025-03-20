from transformers import pipeline

classifier = pipeline("sentiment-analysis")

results = classifier(
    [
        "j'aime les bananes",
        "je déteste les poires...",
        "j'aime les jeux vidéos",
        "je n'aime pas les gorilles",
    ]
)

labels = [result['label'] for result in results]

print (labels)