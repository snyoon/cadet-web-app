from app.models import User, PerformanceCheckScores, UniformScores


def make_uniform_score_list(uniformscore):
    # gotta select the correct db to use.
    # just have it as the first one for now

    recent_scores = uniformscore[0]
    return_list = []
    for x in range(1, 40):
        atr_string = 'week' + str(x) + 'score'
        print(atr_string)
        return_list.append(getattr(recent_scores, atr_string))
    return return_list


def performance_score_list(performance_score):
    selected_year = performance_score[0]
    return_list = []
    for x in range(1, 9):
        atr_string = 'score' + str(x)
        return_list.append(getattr(selected_year, atr_string))
    return return_list
