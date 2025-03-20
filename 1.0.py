from transformers import pipeline

classifier = pipeline("sentiment-analysis")

results = classifier(
    [
        "J'aime les bananes !",
        "Je déteste les poires..."
    ]
)

labels = [result['label'] for result in results]
