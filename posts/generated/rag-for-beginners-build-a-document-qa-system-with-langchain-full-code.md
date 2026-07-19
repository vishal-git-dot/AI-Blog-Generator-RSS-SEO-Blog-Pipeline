---
title: "RAG for Beginners: Build a Document Q&A System with LangChain (Full Code)"
slug: "rag-for-beginners-build-a-document-qa-system-with-langchain-full-code"
author: "Piyush Kumar Soni"
source: "devto_ai"
published: "Sun, 19 Jul 2026 08:11:29 +0000"
description: "RAG for Beginners: Build a Document Q&A System with LangChain (Full Code) Tags: #ai #langchain #python #tutorial LLMs don't know your private documents. Chat..."
keywords: "you, chunks, your, langchain, llm, documents, retrieval, import"
generated: "2026-07-19T08:26:32.161175"
---

# RAG for Beginners: Build a Document Q&A System with LangChain (Full Code)

## Overview

RAG for Beginners: Build a Document Q&A System with LangChain (Full Code) Tags: #ai #langchain #python #tutorial LLMs don't know your private documents. ChatGPT can write you an essay about quantum computing, but it has zero idea what's in your company's internal wiki, your client reports, or that PDF you saved last Tuesday — unless you paste it in yourself, every single time. RAG (Retrieval-Augmented Generation) fixes this. This post walks through the concept and a full working code example you can run today. The Architecture Your Documents → Split into chunks → Convert to embeddings → Stored in a vector database ↓ User's Question → Convert to embedding → Find closest matching chunks → Send question + chunks to LLM → Answer Two steps, really: retrieval (find the relevant pieces of your data) and generation (let the LLM answer using those pieces instead of guessing from training data alone). Setup pip install langchain langchain-community langchain-openai faiss-cpu You'll also need an OPENAI_API_KEY environment variable set: export OPENAI_API_KEY = "your-key-here" Full Working Example — Text Document from langchain_community.document_loaders import TextLoader from langchain.text_splitter import RecursiveCharacterTextSplitter from langchain_community.vectorstores import FAISS from langchain_openai import OpenAIEmbeddings , ChatOpenAI from langchain.chains import RetrievalQA # 1. Load your document loader = TextLoader ( " client_seo_report.txt " ) documents = loader . load () # 2. Split into chunks — LLMs work better with focused chunks than walls of text splitter = RecursiveCharacterTextSplitter ( chunk_size = 500 , chunk_overlap = 50 # overlap prevents cutting a key sentence in half ) chunks = splitter . split_documents ( documents ) # 3. Convert chunks into embeddings and store them in a local vector index embeddings = OpenAIEmbeddings () vector_store = FAISS . from_documents ( chunks , embeddings ) # 4. Wire up retrieval + generation llm = ChatOpenAI ( model = " gpt-4o-mini " , temperature = 0 ) qa_chain = RetrievalQA . from_chain_type ( llm = llm , retriever = vector_store . as_retriever ( search_kwargs = { " k " : 4 }) # top 4 matching chunks ) # 5. Ask a question about YOUR document answer = qa_chain . invoke ( " What was the biggest traffic change this month? " ) print ( answer [ " result " ]) That's a complete, runnable RAG pipeline in about 20 lines. Swapping in a PDF Instead of Plain Text Most real documents aren't .txt files. Swapping the loader is the only change needed: from langchain_community.document_loaders import PyPDFLoader loader = PyPDFLoader ( " client_seo_report.pdf " ) documents = loader . load () # everything else in the pipeline stays exactly the same LangChain has loaders for most formats you'll actually run into — Docx2txtLoader for Word docs, CSVLoader for spreadsheets, WebBaseLoader for scraping a URL directly. Same downstream pipeline every time. Why chunk_size and chunk_overlap Matter More Than They Look Like They Should This trips up almost everyone the first time: Chunk size too large → retrieval pulls back a lot of irrelevant surrounding text along with the useful part, and the LLM's answer gets muddier. Chunk size too small → you lose context; a chunk might not contain enough surrounding information to be useful on its own. No overlap → you can accidentally split a sentence's meaning exactly at the point where the important information was. There's no universal "correct" number — 500 characters with 50 overlap is a reasonable starting point for report-style text, but experiment for your actual documents. Common Mistakes (Beyond Chunking) Expecting perfect retrieval on the first try. Sometimes the "closest match" by embedding similarity isn't actually the most relevant chunk for the question. This is normal — tuning retrieval quality is where most of the real engineering effort goes, well past this example. Not filtering by metadata. If you're indexing documents from multiple clients or time periods, tag your chunks with metadata ( client_name , date ) so you can filter the search instead of searching everything every time: vector_store . as_retriever ( search_kwargs = { " k " : 4 , " filter " : { " client_name " : " acme_corp " }} ) Using the wrong k value. Too few retrieved chunks ( k=1 or 2 ) and the LLM might not have enough context. Too many ( k=10+ ) and you're paying for tokens the model doesn't need and diluting the relevant signal. k=3 to k=5 is a reasonable starting range. Where This Goes Next Once this basic pattern works, natural next steps: Try a production-grade vector store ( Pinecone , Chroma , or Weaviate ) instead of local FAISS once you need this to scale or persist across sessions Add metadata filtering as shown above once you're indexing more than one source Experiment with hybrid search (combining keyword search with embedding similarity) — pure embedding search sometimes misses exact-match terms like product names or codes I'm covering agents next — giving an LLM the ability to actually take actions instead of just answering questions. RAG is the foundation a lot of that builds on, so if this made sense, you're already most of the way there. If you build this and hit a snag, drop a comment — happy to help debug. I'm Piyush Kumar Soni, an AI Developer and LLM Integration Expert with 15+ years running digital agency operations. I write about practical AI tools for SEO and digital marketing. 🔗 LinkedIn · 💻 GitHub · 📰 Substack

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/piyush_kumar_soni/rag-for-beginners-build-a-document-qa-system-with-langchain-full-code-5772

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
