## Clean repeated headers/footers from PDF pages

Problem: Lecture slides repeat the same header on every page (e.g. "COMP1521 26T2",
sometimes twice), plus slide numbers. This text ends up in every chunk.

Why it matters: Every chunk starts with the same words, so chunks look more similar
to each other than they really are. This adds noise to search and wastes characters in each chunk.

Possible fix: Before chunking, find lines that appear on most pages of the same PDF
(e.g. on 80%+ of pages) and remove them. Also strip lines that are just a page number.

Where: In `document_loader.py` (after extracting all pages of a PDF) or as a cleaning
step before `chunk_documents`.


