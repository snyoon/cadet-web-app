def makeuniformscorelist(uniformScore):
    return_list = []
    for x in range(1, 40):
        atr_string = 'week' + str(x) + 'score'
        return_list.append(getattr(uniformScore, atr_string))
    return return_list


def performance_score_list(peformacescores):
    return_list = []
    for x in range(1, 9):
        atr_string = 'week' + str(x)
        return_list.append(getattr(peformacescores, atr_string))
    return return_list
