from celery import task

@task(name="task.add")
def add(x, y):
    return x + y