from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/server.py")

@task
def testing(ctx):
    ctx.run("python3 src/server.py test")

@task
def test(ctx):
    ctx.run("pytest src/tests", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)


@task(coverage)
def coveragereport(ctx):
    ctx.run("coverage html", pty=True)

@task
def gunicorn(ctx):
    ctx.run('cd src && gunicorn -w 4 server:app --bind 0.0.0.0:8000')