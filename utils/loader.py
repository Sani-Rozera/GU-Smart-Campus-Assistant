import os
from langchain_community.document_loaders import PyPDFLoader


def load_documents():

    documents = []

    data_folder = "data"

    for file in os.listdir(data_folder):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(data_folder, file)

            try:
                print(f"Loading: {file}")

                loader = PyPDFLoader(pdf_path)
                docs = loader.load()

                print(f"Loaded successfully: {file}")

                documents.extend(docs)

            except Exception as e:
                print(f"Failed to load {file}")
                print(e)

    return documents
