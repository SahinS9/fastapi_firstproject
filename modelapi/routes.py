from modelapi import app, database, models, crud

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def main():
    return {'main':'modelapi'}

@app.get('/user/{user_id}')
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get('/task/{task_id}')
def task(task_id:int):


@app.get('/tasks')
def tasks():




