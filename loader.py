import os
from langchain_community.document_loaders import PyPDFLoader


def load_documents():

    documents = []

    data_folder = "data"

    for file in os.listdir(data_folder):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(data_folder, file)

            loader = PyPDFLoader(pdf_path)

            documents.extend(loader.load())

    return documents