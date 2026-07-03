import streamlit as st

from utils.loader import load_documents
from utils.splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vectorstore import create_vectorstore
from utils.retriever import get_retriever
from utils.rag_chain import get_llm, get_prompt



st.set_page_config(
    page_title="Geeta University AI Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Geeta University AI Assistant")
st.write("💬 Ask anything about Geeta University.")



@st.cache_resource
def initialize():

    documents = load_documents()

    chunks = split_documents(documents)

    embeddings = get_embeddings()

    create_vectorstore(chunks, embeddings)

    retriever = get_retriever(embeddings)

    client = get_llm()

    prompt = get_prompt()

    return retriever, client, prompt


retriever, client, prompt = initialize()


# ---------------------- User Input ----------------------

user_query = st.text_input("❓ Enter your question")


if st.button("Ask"):

    if user_query.strip():

        with st.spinner("🤖 Please wait... Generating answer..."):

            st.write("🔄 Searching documents...")

            docs = retriever.invoke(user_query)

            st.write(f"📄 Documents Found : {len(docs)}")

            context = "\n\n".join(
                doc.page_content for doc in docs
            )

            st.write("🤖 Generating answer...")
                  

            formatted_prompt = prompt.format(
                context=context,
                question=user_query
            )

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=formatted_prompt
            )

        st.success("✅ Answer Generated Successfully!")

        st.subheader("📖 Answer")
        st.write(response.text)

        st.subheader("📚 Source Documents")

        shown = set()

        for doc in docs:

            source = doc.metadata.get("source", "Unknown File")

            file_name = source.split("\\")[-1]

            if file_name not in shown:

                st.write("•", file_name)

                shown.add(file_name)

    else:

        st.warning("⚠ Please enter your question.")