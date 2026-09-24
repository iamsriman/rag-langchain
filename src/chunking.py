from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf_loader import docs
def chunks(docs,chunkSize=1000, chunkOverlap=200):

    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunkSize,
        chunk_overlap=chunkOverlap
    )
    texts=text_splitter.split_documents(docs)
    return texts

chunks_texts=chunks(docs,1000,200)
