from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader(
    "data/2024-wttc-introduction-to-ai.pdf"
)

docs=loader.load()


