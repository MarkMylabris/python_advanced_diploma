from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from models.models import Base, Tweet, User, Like, Media  # Абсолютный импорт
from db.database import SessionLocal, engine  # Абсолютный импорт

app = FastAPI()

# Создание всех таблиц при запуске
Base.metadata.create_all(bind=engine)

# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Эндпоинт для создания твита
@app.post("/api/tweets")
def create_tweet(content: str, api_key: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.api_key == api_key).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tweet = Tweet(content=content, author_id=user.id)
    db.add(tweet)
    db.commit()
    return {"result": True, "tweet_id": tweet.id}


# Эндпоинт для удаления твита
@app.delete("/api/tweets/{tweet_id}")
def delete_tweet(tweet_id: int, api_key: str, db: Session = Depends(get_db)):
    tweet = db.query(Tweet).filter(Tweet.id == tweet_id).first()
    user = db.query(User).filter(User.api_key == api_key).first()

    if not tweet or tweet.author_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this tweet")

    db.delete(tweet)
    db.commit()
    return {"result": True}


# Эндпоинт для добавления лайка
@app.post("/api/tweets/{tweet_id}/likes")
def add_like(tweet_id: int, api_key: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.api_key == api_key).first()
    tweet = db.query(Tweet).filter(Tweet.id == tweet_id).first()

    if not user or not tweet:
        raise HTTPException(status_code=404, detail="Tweet or user not found")

    like = Like(tweet_id=tweet.id, user_id=user.id)
    db.add(like)
    db.commit()
    return {"result": True}


# Эндпоинт для удаления лайка
@app.delete("/api/tweets/{tweet_id}/likes")
def remove_like(tweet_id: int, api_key: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.api_key == api_key).first()
    like = db.query(Like).filter(Like.tweet_id == tweet_id, Like.user_id == user.id).first()

    if not like:
        raise HTTPException(status_code=404, detail="Like not found")

    db.delete(like)
    db.commit()
    return {"result": True}


# Эндпоинт для загрузки медиафайлов
@app.post("/api/medias")
async def upload_media(api_key: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.api_key == api_key).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    filename = file.filename
    media = Media(filename=filename)
    db.add(media)
    db.commit()
    return {"result": True, "media_id": media.id}
