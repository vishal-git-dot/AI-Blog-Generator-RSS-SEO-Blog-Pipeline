---
title: "Building a Transformer from Scratch: Part 1 — The Embedding Layer"
slug: "building-a-transformer-from-scratch-part-1-the-embedding-layer"
author: "Dhruv"
source: "devto_python"
published: "Wed, 14 Oct 2026 16:45:46 +0000"
description: "Before the attention mechanism computes a single dot product in an autoregressive Transformer like GPT, the model faces a fundamental problem: neural network..."
keywords: "shape, self, embeddings, dropout, torch, embedding, layer, token"
generated: "2026-10-14T16:54:47.638709"
---

# Building a Transformer from Scratch: Part 1 — The Embedding Layer

## Overview

Before the attention mechanism computes a single dot product in an autoregressive Transformer like GPT, the model faces a fundamental problem: neural networks do not understand text, and feeding them raw token IDs introduces false mathematical assumptions. If the tokenizer maps "cat" to index 200 and "dog" to 201 , a linear layer treats "dog" as having a higher numerical value than "cat" . Token IDs are discrete categorical variables, not ordinal measurements. The embedding layer bridges this gap. It maps discrete integers into continuous vector spaces where semantic relationships and sequence ordering can actually be learned. Here is how the embedding layer works under the hood, along with a production-grade PyTorch implementation. The Two Problems Embeddings Must Solve 1. Semantic Representation (Token Embeddings) A tokenizer splits raw text into tokens and assigns each one an integer ID. To eliminate arbitrary numerical ordering, we map each ID to a learned vector of dimension d_model via a token lookup matrix W_e of shape (vocab_size, d_model) . Through backpropagation, tokens that appear in similar linguistic contexts gravitate toward each other in this high-dimensional vector space. 2. Sequence Order (Positional Embeddings) Unlike Recurrent Neural Networks (RNNs), which process tokens step-by-step from left to right, Transformers process the entire sequence in parallel. Because self-attention is permutation-equivariant, the model would process "dog bites man" and "man bites dog" identically without an explicit position signal. To fix this, we map each sequence position 0, 1, ..., seq_len - 1 to a positional embedding vector of dimension d_model . PyTorch Implementation This module combines token embeddings with learned absolute positional embeddings and dropout regularization, matching the architectural setup used in GPT-2. python import torch import torch.nn as nn class TransformerEmbeddings(nn.Module): def __init__(self, vocab_size: int, d_model: int, max_seq_len: int, dropout: float = 0.1): super().__init__() self.d_model = d_model # Token lookup matrix: shape (vocab_size, d_model) self.token_embeddings = nn.Embedding(vocab_size, d_model) # Position lookup matrix: shape (max_seq_len, d_model) self.position_embeddings = nn.Embedding(max_seq_len, d_model) # Regularization: applies dropout across the summed embeddings self.dropout = nn.Dropout(p=dropout) def forward(self, input_ids: torch.Tensor) -> torch.Tensor: # Expected input shape: (batch_size, seq_len) batch_size, seq_len = input_ids.shape # Guard clause: prevent context window overflows if seq_len > self.position_embeddings.num_embeddings: raise ValueError( f"Sequence length ({seq_len}) exceeds maximum context window " f"({self.position_embeddings.num_embeddings})" ) # Generate positional indices [0, 1, ..., seq_len - 1] # Shape: (1, seq_len), created directly on the input's target device positions = torch.arange(0, seq_len, device=input_ids.device).unsqueeze(0) # Retrieve vectors tok_emb = self.token_embeddings(input_ids) # (batch_size, seq_len, d_model) pos_emb = self.position_embeddings(positions) # (1, seq_len, d_model) # Combine via broadcasting: (batch_size, seq_len, d_model) embeddings = tok_emb + pos_emb return self.dropout(embeddings) # Sanity check execution block if __name__ == "__main__": vocab_size, d_model, max_len = 50257, 768, 1024 layer = TransformerEmbeddings(vocab_size, d_model, max_len, dropout=0.1) # Dummy batch of 2 sequences, each 8 tokens long dummy_input = torch.randint(0, vocab_size, (2, 8)) output = layer(dummy_input) print(f"Input shape: {dummy_input.shape}") # torch.Size([2, 8]) print(f"Output shape: {output.shape}") # torch.Size([2, 8, 768]) assert output.shape == (2, 8, d_model), "Shape mismatch!" print("Embedding module ran successfully.")

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/heywinterbell/building-a-transformer-from-scratch-part-1-the-embedding-layer-172g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
