"""
This file contains embeddings function. 
Converts human text to dnese nermical vectors
Text which has similar meaning gets mapped to vectors that point in a similar direction

Nomic-Embed text
Wants a small label in front of every text telling it what kinda text it is 
for eg:
query_prefix: "search question"
document_prefix: "search document"

WHY?
With Labels, it places questions near the chunks that answer them, so search gets accurate
"""

