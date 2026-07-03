from pathlib import Path
from langchain_chroma import Chroma

def get_vectorstore_path():
    return Path(__file__).resolve().parents[1] / "vectorstore"


def create_vectorstore(chunks, embeddings):
    persist_directory = str(get_vectorstore_path())
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    return vectorstore