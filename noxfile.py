import nox


@nox.session
def tests(session):
    session.install("-r", "requirements.txt")
    session.run("nikola", "build", "--strict")
    session.run("nikola", "check", "--check-links", "--check-files")


@nox.session
def lint_rst(session):
    session.install("rstcheck")
    session.run("rstcheck", "-r", ".")


@nox.session
def lint_yaml(session):
    session.install("yamllint")
    session.run("yamllint", "-s", "data")


@nox.session
def lint_python(session):
    session.install("black")
    session.run("black", "--check", ".")


@nox.session
def format_python(session):
    session.install("black")
    session.run("black", ".")
