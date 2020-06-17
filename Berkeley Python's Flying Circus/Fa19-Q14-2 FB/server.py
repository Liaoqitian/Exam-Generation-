import prairielearn as pl
import random, copy, math

def generate(data):

    # Sample a list of random length between 3 and 5. 
    length = random.randint(3, 6)

    # Sample random elements in (0, 1000) to fill the list. 
    A = [0] * length
    copy = [0] * length
    copy = random.sample(range(0, 1000), length)
    for i in range(length):   
        A[i] = str(copy[i])

    # Set up the question. 
    index = random.randint(1, len(A) - 2)
    adder = str(random.randint(1, 5))
    
    # Compute the correct solution.
    solution = A[index] + adder
    solution = str([solution]).replace("[","").replace("]","").replace("'",'"')
    
    # Store the parameters.
    A = str(A).replace("'", '"')
    data['params']['A'] = A
    data['params']['index'] = index
    data['params']['adder'] = adder 
    data['correct_answers']['solution'] = solution
