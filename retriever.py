from pathlib import Path
from langchain_chroma import Chroma


def get_vectorstore_path():
    return Path(__file__).resolve().parents[1] / "vectorstore"


def get_retriever(embeddings):
    persist_directory = str(get_vectorstore_path())
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 10}
    )

    return retriever