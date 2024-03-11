from modelapi import app
from modelapi import database
from modelapi import models
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
def user(user_id: int):
    user = models.User.get_or_404(id = user_id)
    return {'user':user}

@app.get('/task/{task_id}')
def task(task_id:int):
    task = models.Task.query.filter(id = task_id).first()

    if task is None:
        task = HTTPException(status_code=404, detail="Task not found")
        return {'data': {'task':task}}

    owner = task.owner

    return {'data': {'user':owner,'task':task}}

@app.get('/tasks')
def tasks():
    tasks = models.Task.query.all()
    return {'tasks':tasks}




# from modelapi import app
# from modelapi.models import Task
# from fastapi import Query

# @app.get('/tasks')
# def tasks(page: int = Query(1, gt=0), per_page: int = Query(10, gt=0)):
#     """
#     Retrieve a paginated list of tasks.

#     :param page: Page number (default: 1)
#     :param per_page: Number of items per page (default: 10)
#     """
#     tasks = Task.query.paginate(page=page, per_page=per_page, error_out=False)
    
#     if not tasks.items:
#         return {'message': 'No tasks found.'}

#     paginated_tasks = [
#         {
#             'id': task.id,
#             'name': task.name,
#             'description': task.description,
#             'deadline': task.deadline,
#             'user_id': task.user_id,
#         }
#         for task in tasks.items
#     ]

#     return {'tasks': paginated_tasks, 'total_pages': tasks.pages, 'current_page': tasks.page}
