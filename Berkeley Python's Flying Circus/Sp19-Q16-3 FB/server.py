import prairielearn as pl
import random, copy, math, string

def generate(data):
    # Randomly create start_index string of length 5.This will be the solution
    def id_generator(size=5, chars = string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    solution = id_generator()

    # Sample the starting and ending point
    start_index = random.randint(1, 3)
    end_index = start_index + 2

    # Compute the solution. 
    output = solution[start_index:end_index]

    # Store the parameters 
    data["correct_answers"]['solution'] = solution
    data['params']['start_index'] = start_index
    data['params']['end_index'] = end_index
    data['params']['output'] = output

def grade(data):
    if data["submitted_answers"]["solution"] not in data["format_errors"]: # check we don't already have a format error
        if len(data["submitted_answers"]["solution"]) != 5:
            data["format_errors"]["solution"] = "Only a 5-character string is allowed."
            data["feedback"]["solution"] = "Only a 5-character string is allowed."
            return
        if len(set(data["submitted_answers"]["solution"])) != 5: 
            data["format_errors"]["solution"] = "Unique characters must be used."
            data["feedback"]["solution"] = "Only strings with unique characters are allowed."
            return
    if data['score'] == 0: 
        if data["submitted_answers"]["solution"][data['params']['start_index']:data['params']['end_index']] == data['params']['output']:
            data["partial_scores"]["score"] = 1
            data['score'] = 1
            data["feedback"]["solution"] = "you got this correct!"
        else:
            # data["partial_scores"]["solution"] = 0
            data["feedback"]["solution"] = "you got this wrong, sorry"