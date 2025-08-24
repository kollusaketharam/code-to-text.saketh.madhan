from pydantic import BaseModel, Field
from typing import List, Optional, Literal

SupportedLanguage = Literal["python", "javascript", "java"]

class ExplainRequest(BaseModel):
    code: str = Field(min_length=1, description="Source code to explain")
    language: SupportedLanguage

class ExplainResponse(BaseModel):
    language: SupportedLanguage
    explanation: List[str]
    complexity: str
    flowchart_mermaid: Optional[str] = None
