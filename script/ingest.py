# scripts/ingest.py
import argparse
import logging
import sys
from pathlib import Path

# Add the project root to the Python path so the 'src' module can be imported
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.pdf_processor import process_pdf_directory
from src.vector_store import VectorStore

# Configure terminal logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("sourcesleuth.cli")

def main():
    parser = argparse.ArgumentParser(
        description="Ingest PDFs into the SourceSleuth local vector store."
    )
    parser.add_argument(
        "--dir",
        type=str,
        default=str(PROJECT_ROOT / "student_pdfs"),
        help="Directory containing PDF files to ingest (default: student_pdfs/)"
    )
    parser.add_argument(
        "--data-dir",
        type=str,
        default=str(PROJECT_ROOT / "data"),
        help="Directory to store the FAISS index and metadata (default: data/)"
    )
    args = parser.parse_args()

    pdf_dir = Path(args.dir)
    data_dir = Path(args.data_dir)

    if not pdf_dir.exists() or not pdf_dir.is_dir():
        logger.error(f" Error: PDF directory '{pdf_dir}' does not exist.")
        logger.info(f"Please create it or specify a different directory using --dir.")
        sys.exit(1)

    logger.info(f"Scanning '{pdf_dir}' for PDFs...")

    # 1. Process PDFs into text chunks
    chunks = process_pdf_directory(pdf_dir)
    if not chunks:
        logger.warning("No text chunks were extracted. Are there valid PDFs in the directory?")
        sys.exit(0)

    # 2. Initialize VectorStore
    store = VectorStore(data_dir=data_dir)

    # 3. Load existing store if it exists (so we append, not overwrite)
    if store.load():
        logger.info("Restored existing vector store. Appending new documents...")
    else:
        logger.info("Initializing new vector store...")

    # 4. Embed and add chunks
    added = store.add_chunks(chunks)

    # 5. Persist to disk
    store.save()

    logger.info(" Ingestion Complete!")
    logger.info(f"   - New chunks added: {added}")
    logger.info(f"   - Total chunks in database: {store.total_chunks}")
    logger.info("You can now connect Claude Desktop to your SourceSleuth MCP Server!")

if __name__ == "__main__":
    main()