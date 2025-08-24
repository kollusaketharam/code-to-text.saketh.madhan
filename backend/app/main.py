from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import ExplainRequest, ExplainResponse
from .explain import explain_code
from .complexity import estimate_complexity
from .flowchart import to_mermaid_flowchart

app = FastAPI(title="Code-to-Text Teaching Assistant", version="1.0.0")

# CORS so your Vite app can call the API
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Backend is running. POST /explain to get explanations."}

@app.post("/explain", response_model=ExplainResponse)
def explain(req: ExplainRequest):
    code = (req.code or "").strip()
    if not code:
        raise HTTPException(status_code=400, detail="Code cannot be empty.")
    if req.language not in ("python", "javascript", "java"):
        raise HTTPException(status_code=400, detail="Unsupported language.")

    # Generate explanations (rule-based)
    explanation = explain_code(code, req.language)

    # Very simple difficulty estimate
    difficulty = estimate_complexity(code, req.language)

    # Optional tiny Mermaid flowchart
    mermaid = to_mermaid_flowchart(code, req.language)

    return ExplainResponse(
        language=req.language,
        explanation=explanation,
        complexity=difficulty,
        flowchart_mermaid=mermaid,
    )
