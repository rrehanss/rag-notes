from src.embeddings import embed_text

a = embed_text("Kanye released Graduation Graduation")
b = embed_text("Kanye released Graduation")
c = embed_text("An apple a day keeps the doctor away")

# print((a == b).all())   # True: same text, same vector
print(a[:4])
print(b[:3])
print(c[:3])            # totally different numbers