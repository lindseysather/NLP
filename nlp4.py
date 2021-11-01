import spacy

nlp = spacy.load("en_core_web_sm")

textfile = open("text for spacy2.txt", 'r').read()

document = nlp(textfile)

#analyzes text and pulls out entities 
#.ents extracts all entities from document
for entity in document.ents:
    print(f"{entity.text}: {entity.label_}")

#explains abbreviations 
print(spacy.explain("GPE"))
print(spacy.explain("LOC"))


#ROMEO AND JULIET VS EDWARD THE SECOND
from pathlib import Path

document1 = nlp(Path("RomeoAndJuliet.txt").read_text())
document2 = nlp(Path("EdwardTheSecond.txt").read_text())

#compares documents
print(document1.similarity(document2))
#returns 0.94055 (94% similar - probably same author)