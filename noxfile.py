import nox


locations = "src", "tests", "noxfile.py"

nox.options.sessions = "lint", "tests"


@nox.session(python=["3.9", "3.10", "3.11"])
def tests(session):
    session.run("pytest", "--cov")


@nox.session(python=["3.9", "3.10", "3.11"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python="3.9")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
