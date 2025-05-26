# app/main.py
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, StreamingResponse
from sentence_transformers import SentenceTransformer, util
# from app.mock_data import MOCK_DATA
import json
from pathlib import Path

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")


DATA_PATH = Path(__file__).parent / "statista_realistic_mock_data.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    MOCK_DATA = json.load(f)


CORPUS_EMBEDDINGS = model.encode(
    [item["description"] for item in MOCK_DATA], convert_to_tensor=True
)


@app.get("/data")
def get_all_mock_data():
    """
    Return all mock data.
    """
    return MOCK_DATA


@app.get("/find")
def find(query: str = Query(...)):
    query_embedding = model.encode(query, convert_to_tensor=True)
    print(query_embedding)
    hits = util.semantic_search(query_embedding, CORPUS_EMBEDDINGS, top_k=5)[0]

    results = [
        {**MOCK_DATA[hit["corpus_id"]], "score": float(hit["score"])} for hit in hits
    ]
    return JSONResponse(content=results)


@app.get("/stream/find")
def stream_find(query: str = Query(...)):
    query_embedding = model.encode(query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, CORPUS_EMBEDDINGS, top_k=10)[0]

    def event_stream():
        for hit in hits:
            item = {**MOCK_DATA[hit["corpus_id"]], "score": float(hit["score"])}
            yield json.dumps(item) + "\n"

    return StreamingResponse(event_stream(), media_type="application/json")
