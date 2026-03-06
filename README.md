<div align="center">
  <svg width="400" height="100" xmlns="http://www.w3.org/2000/svg">
    <rect width="400" height="100" rx="15" fill="#1e1e1e"/>
    <circle cx="50" cy="50" r="30" fill="#4CAF50" />
    <path d="M50 30 L65 60 L35 60 Z" fill="#ffffff" />
    <text x="100" y="60" font-family="Arial, sans-serif" font-size="32" font-weight="bold" fill="#ffffff">SourceSleuth</text>
    <text x="100" y="80" font-family="Arial, sans-serif" font-size="14" fill="#aaaaaa">Local MCP Context Engine</text>
  </svg>

  <br>

  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.10+-yellow.svg" alt="Python"></a>
  <a href="https://modelcontextprotocol.io/"><img src="https://img.shields.io/badge/MCP-Enabled-brightgreen.svg" alt="MCP"></a>
</div>

---

## What is this project?
SourceSleuth is a local-first Model Context Protocol (MCP) server that connects your favorite AI assistants (like Claude Desktop) directly to your local academic PDFs. 

## Why should I care?
College students frequently encounter the "orphaned quote" crisis: having a perfectly paraphrased concept in their draft but losing the original source document and page number. SourceSleuth solves this by using local semantic search to instantly locate the exact document, page, and surrounding paragraph of any orphaned text, eliminating hours of manual re-reading.

##  Architecture Diagram
*How the MCP integration works under the hood:*

<div align="center">
  <svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect x="10" y="50" width="120" height="100" rx="10" fill="#2d3748"/>
    <text x="70" y="100" fill="#fff" font-family="Arial" font-size="14" text-anchor="middle" font-weight="bold">Claude Desktop</text>
    <text x="70" y="120" fill="#cbd5e0" font-family="Arial" font-size="12" text-anchor="middle">(MCP Host)</text>
    <path d="M130 100 L230 100" stroke="#4a5568" stroke-width="3" marker-end="url(#arrowhead)"/>
    <text x="175" y="85" fill="#a0aec0" font-family="Arial" font-size="12" text-anchor="middle">JSON-RPC</text>
    <rect x="230" y="50" width="140" height="100" rx="10" fill="#2b6cb0"/>
    <text x="300" y="95" fill="#fff" font-family="Arial" font-size="14" text-anchor="middle" font-weight="bold">SourceSleuth</text>
    <text x="300" y="115" fill="#e2e8f0" font-family="Arial" font-size="12" text-anchor="middle">(MCP Server)</text>
    <path d="M370 100 L470 100" stroke="#4a5568" stroke-width="3" marker-end="url(#arrowhead)"/>
    <rect x="470" y="50" width="120" height="100" rx="10" fill="#2f855a"/>
    <text x="530" y="95" fill="#fff" font-family="Arial" font-size="14" text-anchor="middle" font-weight="bold">Local Vector DB</text>
    <text x="530" y="115" fill="#c6f6d5" font-family="Arial" font-size="12" text-anchor="middle">(MiniLM Embeddings)</text>
    <defs>
      <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
        <polygon points="0 0, 10 3.5, 0 7" fill="#4a5568"/>
      </marker>
    </defs>
  </svg>
</div>

## Features
* **Zero-API-Cost Semantic Search:** Runs entirely locally using HuggingFace's `sentence-transformers`.
* **MCP Tool Integration:** Exposes the `find_orphaned_quote` tool directly to your AI client.
* **Privacy-First:** Your unpublished thesis and copyrighted textbooks never leave your hard drive.

##  How do I get it running?
*Installation in under 5 minutes.*

1. **Clone & Install Dependencies:**
   ```bash
   git clone [https://github.com/yourusername/sourcesleuth.git](https://github.com/yourusername/sourcesleuth.git)
   cd sourcesleuth
   pip install -r requirements.txt