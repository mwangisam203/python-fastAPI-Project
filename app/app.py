from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "Cool test post"},
    2: {"title": "Learning FastAPI", "content": "FastAPI makes building APIs in Python very fast."},
    3: {"title": "Python Tips", "content": "Use virtual environments to manage dependencies."},
    4: {"title": "Morning Thoughts", "content": "Consistency beats motivation every time."},
    5: {"title": "Tech Journey", "content": "Started learning backend development with FastAPI."},
    6: {"title": "Coding Practice", "content": "Practicing coding every day improves problem solving."},
    7: {"title": "Debugging Skills", "content": "Reading error messages carefully saves time."},
    8: {"title": "API Design", "content": "Good API design focuses on simplicity and clarity."},
    9: {"title": "Open Source", "content": "Contributing to open source helps you learn faster."},
    10: {"title": "Productivity", "content": "Break large problems into smaller manageable pieces."},
    11: {"title": "Data Structures", "content": "Understanding data structures improves algorithm efficiency."},
    12: {"title": "Learning Curve", "content": "Every developer struggles at the beginning."},
    13: {"title": "Backend Development", "content": "Backend systems power the logic behind applications."},
    14: {"title": "System Design", "content": "Scaling applications requires thoughtful architecture."},
    15: {"title": "Future Goals", "content": "Working towards mastering AI and machine learning."}
              }

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post Cannot be Found")

    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content" : post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post

