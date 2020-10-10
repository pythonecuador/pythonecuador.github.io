import nox


@nox.session
def tests(session):
    session.install('-r', 'requirements.txt')
    session.run('nikola', 'build', '--strict')
    session.run('nikola', 'check', '--check-links', '--check-files')


@nox.session
def lint(session):
    session.install('rstcheck')
    session.run('rstcheck', '-r', '.')
