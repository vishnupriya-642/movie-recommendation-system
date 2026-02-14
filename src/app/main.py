from fastapi import FastAPI, HTTPException
from app.schemas import RecommendationRequest, RecommendationResponse
from app.recommender import recommend_movies

app = FastAPI(
    title="Movie Recommendation API",
    version="1.0.0",
    description="Content-Based Movie Recommendation System"
)


@app.get("/")
def root():
    return {"message": "Movie Recommendation API is running"}


@app.post("/recommend", response_model=RecommendationResponse)
def get_recommendations(request: RecommendationRequest):
    try:
        results = recommend_movies(
            movie_title=request.movie_title,
            top_n=request.top_n
        )
        return {"recommendations": results}

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
