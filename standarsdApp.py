from app import app, db
from app.models import User, UniformScore, PerformanceCheckScores
from app.helper import makeuniformscorelist

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'UniformScore': UniformScore, 'PerformanceCheckSCores': PerformanceCheckScores}

