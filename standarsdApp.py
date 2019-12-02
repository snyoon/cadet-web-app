from app import app, db
from app.models import User, UniformScores, PerformanceCheckScores

jy = User.query.get(1)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'UniformScores': UniformScores, 'PerformanceCheckScores': PerformanceCheckScores}

