# Azure AI Search — Python-based content vectorization and enrichment

This tutorial project provides a code-first workflow to chunk, enrich, and vectorize content, then index it into Azure AI Search. It’s designed to be simple to extend so you can try different content preparation approaches for chat over your data.

## Azure services used
- Azure AI Search
- Azure OpenAI
- Azure Document Intelligence
- Azure Blob Storage

## Prerequisites and setup
1) Install Python dependencies:
   - python -m pip install -r requirements.txt

2) Configure environment variables:
   - Copy .env_sample to .env and fill in your values.
   - The notebooks read environment variables (via python-dotenv). Common variables include:
     - SEARCH_SERVICE_NAME, SEARCH_ADMIN_KEY, SEARCH_INDEX_NAME, SEARCH_INDEX_SCHEMA_FILE, SEARCH_API_VERSION
     - OPENAI_API_BASE, OPENAI_API_KEY, OPENAI_API_VERSION, OPENAI_EMBEDDING_MODEL, OPENAI_GPT_MODEL
     - BLOB_SERVICE_NAME, BLOB_CONTAINER, BLOB_KEY
     - DOC_INTELLIGENCE_ENDPOINT, DOC_INTELLIGENCE_APIM_KEY
     - MODEL_DEPLOYMENT_NAME, PROJECT_ENDPOINT (for the agent notebook)

3) Update the index schema (schema.json):
   - If you’re using integrated vectorization, set your Azure OpenAI details in the vectorizer section:
     - resourceUri: https://[OPENAI_SERVICE].openai.azure.com
     - deploymentId: [your-embeddings-deployment]
     - apiKey: [your-azure-openai-key]

Linux notes: If you need to process file types other than PDF, install converters:
- sudo apt-get update
- sudo apt-get install wkhtmltopdf
- sudo apt-get install libreoffice

## Quickstart
1) Create the index
   - Open 01-create-index.ipynb and run all cells.
   - Confirms the index is created in your Azure AI Search service.

2) Process documents
   - Upload your source files to the configured Blob container.
   - Open 02-process-content.ipynb and run all cells.
   - Outputs JSON files to the data/ folder.

3) Index the processed data
   - Open 03-index-data.ipynb and run all cells.
   - Confirms documents are added to your index.

4) Test queries
   - Open 04-test-query.ipynb and run the sample vector, hybrid, and semantic queries.

5) Try the agent
   - Open 05-ai-agent-search.ipynb, ensure MODEL_DEPLOYMENT_NAME and PROJECT_ENDPOINT are set, and run the notebook.

## Notebooks (run in this order)
1) 01-create-index.ipynb — Create an Azure AI Search index using schema.json, enabling vector search and integrated vectorization where configured.
   Link: ./01-create-index.ipynb

2) 02-process-content.ipynb — Ingest documents from Azure Blob Storage, extract content with Azure Document Intelligence, chunk, and embed using Azure OpenAI. Outputs JSON files under data/ for indexing.
   Link: ./02-process-content.ipynb

3) 03-index-data.ipynb — Load the processed JSON files and index them into Azure AI Search. Optionally, you can upload the JSON to Blob and use an Azure AI Search indexer instead.
   Link: ./03-index-data.ipynb

4) 04-test-query.ipynb — Run vector, hybrid, and semantic queries directly against your index to validate scoring and relevance.
   Link: ./04-test-query.ipynb

5) 05-ai-agent-search.ipynb — Use an Azure AI Project (agents) to call Azure AI Search as a tool and generate answers grounded in your index.
   Link: ./05-ai-agent-search.ipynb

## Future goals
1) Create Azure Functions to automatically process and index new or updated content in Blob Storage
2) Experiment with different chunking strategies (including GPT-based approaches)