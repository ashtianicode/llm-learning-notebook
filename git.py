import os
from llama_index import download_loader
from llama_hub.github_repo import GithubRepositoryReader, GithubClient
download_loader("GithubRepositoryReader")

github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
loader = GithubRepositoryReader(
    github_client,
    owner =                  "ashtianicode",
    repo =                   "llm-learning-notebook",
    verbose =                True,
    concurrent_requests =    10,
)

docs = loader.load_data(branch="main")

for doc in docs:
    print(doc.extra_info)

from llama_index import download_loader, GPTVectorStoreIndex
index = GPTVectorStoreIndex.from_documents(docs)

query_engine = index.as_query_engine()
response = query_engine.query("Summarize the poems class?")
print(response)