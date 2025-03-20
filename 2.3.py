from transformers import BertTokenizer

def tokeniser():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    text = "Ceci est un exemple de texte à tokeniser."
    tokens = tokenizer.tokenize(text)
    print(tokens)
