##HERE IT'S STARTED
Framing your project around the Model Context Protocol (MCP) is a brilliant move. MCP is essentially the "USB-C standard" for AI—an open protocol that standardizes how LLMs (like Claude or local models) connect to external tools and data sources.

Instead of building a standalone web app with a custom frontend, we will architect SourceSleuth as a modular MCP Server. This means students can use their existing AI interfaces (like Claude Desktop or Cursor) to directly query their local PDFs.

Here is how the SourceSleuth problem statement and architecture translate into strict MCP terms, aligning perfectly with your open-source hackathon guidelines.

1. The Architecture in MCP Terms
In the MCP ecosystem, the system is broken down into three components. Emphasis should be placed on modular architecture, so that contributors can improve individual components without needing to understand the entire codebase.

The MCP Host (The Frontend): The student's AI application (e.g., Claude Desktop, Windsurf, or an IDE). We don't build this; we integrate with it.

The MCP Client: The built-in protocol handler within the Host that formats the student's requests.

The MCP Server (Our Hackathon Project): A local, lightweight Python server that manages the PDF embeddings and exposes them to the Host securely.

2. The Core MCP Capabilities
An MCP Server communicates with the Host by exposing three specific types of capabilities. Here is what SourceSleuth will expose:

Resources (Context): MCP Resources expose static or dynamic data. Our server will expose file://student_pdfs/{filename} as a resource, allowing the AI model to read the raw text of any specific academic paper on the student's hard drive if it needs deeper context.

Tools (Actions): Tools are executable functions the AI can trigger. We will expose find_orphaned_quote(quote_text). When the student asks the AI, "Where did I get this quote?", the AI autonomously triggers this tool, which runs our local SentenceTransformer model to perform the vector search.

Prompts (Workflows): We will expose a predefined prompt called cite_recovered_source. This tells the LLM exactly how to format the recovered text into a strict APA or MLA citation, saving the user from writing complex prompts.

3. Aligning with Hackathon AI/ML Requirements
Building an MCP server doesn't exempt us from the scientific rigor of the AI/ML track. The data used, model choices, and training methodology must all be documented for a project to be reproducible the sine qua non of scientific open source work.

Dataset & Preprocessing: The README.md must document how the local PDFs are chunked (e.g., 500-token chunks with 50-token overlap) before embedding.

Model Architecture Documentation: We must document the reasoning behind choosing a lightweight model like all-MiniLM-L6-v2—specifically, that it runs efficiently on a student's CPU, keeping the MCP Server fast and entirely local for privacy.

4. Code Blueprint: The MCP Server (v1.0)
Using modern Python MCP SDKs (like FastMCP), building the server is highly declarative. This is the code contributors will interact with.

Python

# src/mcp_server.py
from mcp.server.fastmcp import FastMCP
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the MCP Server
mcp = FastMCP("SourceSleuth")

# Load our local embedding model (Documented in README per hackathon rules)
model = SentenceTransformer('all-MiniLM-L6-v2')
document_embeddings = [] # Loaded from local vector store in a real app
document_metadata = []

@mcp.tool()
def find_orphaned_quote(quote: str, top_k: int = 3) -> str:
    """
    Tool for the LLM to find the original academic source for an orphaned quote.
    
    Args:
        quote (str): The text or paraphrase the student wrote.
        top_k (int): The number of matches to return.
    """
    if not document_embeddings:
        return "Error: No PDFs have been ingested into the vector store yet."

    # 1. Embed the student's orphaned quote
    quote_embedding = model.encode([quote])
    
    # 2. Calculate cosine similarity against all PDF chunks
    similarities = cosine_similarity(quote_embedding, document_embeddings)[0]
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    
    # 3. Format the response for the LLM to read and present to the user
    response = "Found the following potential sources:\n\n"
    for idx in top_indices:
        meta = document_metadata[idx]
        score = round(float(similarities[idx]), 4)
        response += f"- Document: {meta['filename']}, Page {meta['page']} (Confidence: {score})\n"
        response += f"  Context: \"{meta['text']}\"\n\n"
        
    return response

if __name__ == "__main__":
    # Runs the server over standard input/output (stdio), which is how 
    # MCP Hosts like Claude Desktop communicate with local servers.
    mcp.run()
By framing the project this way, you are solving a highly specific student crisis while utilizing the absolute cutting-edge of AI interoperability standards.
