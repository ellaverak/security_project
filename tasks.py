from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/manage.py runserver", pty=True)

@task
def migrate(ctx):
    ctx.run("python src/manage.py makemigrations", pty=True)
    ctx.run("python3 src/manage.py migrate", pty=True)
