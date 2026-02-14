from pydantic import BaseModel, Field
from typing import List


class RecommendationRequest(BaseModel):
    movie_title: str = Field(..., example="Toy Story (1995)")
    top_n: int = Field(default=5, ge=1, le=20)


class MovieResponse(BaseModel):
    title: str
    genres: str


class RecommendationResponse(BaseModel):
    recommendations: List[MovieResponse]
