# SourceSleuth Roadmap

SourceSleuth aims to become the definitive local, privacy-first context engine for students and researchers. This roadmap outlines our current capabilities and our vision for the future.

## Current State: v1.0 (Hackathon Release)
Currently, SourceSleuth provides the core foundational features needed to solve the "orphaned quote" crisis:
* **Local Ingestion Script:** Python-based CLI tool to parse `.pdf` files using `PyPDF2` and chunk text.
* **Semantic Search Engine:** In-memory vector matching using HuggingFace's `all-MiniLM-L6-v2` embedding model and scikit-learn cosine similarity.
* **MCP Integration:** A fully functional `FastMCP` server exposing the `find_orphaned_quote` tool to compatible hosts like Claude Desktop.

## Planned Features (v1.1 - v2.0)
We are actively planning the following features and tracking them via GitHub Issues and Milestones:

1. **OCR Support for Scanned Documents (v1.1):** Integrate `Tesseract OCR` to allow the ingestion of scanned textbook images and older, non-selectable PDFs.
2. **Persistent Vector Database (v1.2):** Replace the in-memory numpy array with a lightweight, persistent local vector database like `ChromaDB` or `FAISS` to prevent re-embedding on every server restart.
3. **Automated BibTeX Generation (v1.5):** Expose a new MCP prompt/tool that takes a recovered source and automatically formats it into a valid BibTeX or APA citation.
4. **Desktop GUI App / One-Click Installer (v2.0):** Wrap the Python server in an Electron or Tauri app with an intuitive UI for managing ingested documents, making it accessible to non-technical students.

## Known Technical Debt & Limitations
To build this over a hackathon weekend, we made some trade-offs that we intend to fix:
* **PDF Parsing Quality:** Currently, two-column academic papers sometimes chunk out of order. We need to implement a more robust layout-aware parser (e.g., `pdfplumber`).
* **Math Formulas:** The current embedding model struggles with complex LaTeX/math formulas found in STEM papers. 
* **Hardcoded Chunk Sizes:** Text chunking is currently hardcoded to 300 words. This needs to become configurable via a `.env` file.

## Call to Contributors
We cannot build this alone! Here is where we need your help the most:
* **Frontend Developers:** We need help conceptualizing the v2.0 Desktop GUI.
* **Machine Learning Enthusiasts:** We are looking for contributors to test and benchmark alternative, lightweight embedding models.
* **Quality Assurance (QA):** If you are a student, we need you to test SourceSleuth on your actual semester folders and report bugs! Check out the `good first issue` label on our issue tracker.