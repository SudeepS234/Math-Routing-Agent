from langchain.docstore.document import Document
from knowledge_base.vector_store import qdrant
import os
import re

KB_FILE = "knowledge_base/math_kb.txt"

def load_math_kb_entries(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match format: question \n Answer: ... \n Explanation: ...
    pattern = re.compile(r"(.*?)\s*Answer:\s*(.*?)\s*Explanation:\s*(.*?)(?=\n\S|\Z)", re.DOTALL)
    matches = pattern.findall(content)

    entries = []
    for match in matches:
        question, answer, explanation = [s.strip() for s in match]
        if question and answer and explanation:
            entries.append((question, answer, explanation))
    return entries

def main():
    entries = load_math_kb_entries(KB_FILE)

    if not entries:
        print("\u274c No valid question-answer pairs loaded.")
        return

    docs = [
        Document(
            page_content=explanation,
            metadata={"question": question, "answer": answer}
        ) for question, answer, explanation in entries
    ]

    qdrant.add_documents(documents=docs)
    print(f"\u2705 Vector store indexed successfully with {len(docs)} entries.")

if __name__ == "__main__":
    main()