import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define a list of garden path sentences
gardenpathSentences = [
    "The horse raced past the barn fell.",
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "The rat the cat the dog chased killed ate.",
    "I convinced her children are noisy."
]

# Iterate through the garden path sentences and print the entities in each sentence
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    print(sentence)
    for token in doc.ents:
        print(token.text, token.label_)
    print("\n")
