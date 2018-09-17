"""
   Joey Parshley
   MET CS 521 O2
   3 APR 2018
   hw_4_10_1
   Description: Write a program that reads a list of scores and then assigns 
                grades based on the following scheme:

            The grade is A if score is >= best – 10.

            The grade is B if score is >= best – 20.

            The grade is C if score is >= best – 30.

            The grade is D if score is >= best – 40.

            The grade is F otherwise
    sample output:
    Student 0 score is 49 and grade is C
    Student 1 score is 73 and grade is A
"""
invalid_entry = True
ERROR_MESSAGE = "\nYour entry '{0}' is not a number. Please try again."

def getGrade(s,b):
    """
    Description: Calculate the letter grades for a list of given numeric scores
                 based on the max score in the list.
        :input s : int - score to be used to calculate letter grade
        :input b : best score used to determine grade 
        :return grade : String - letter grade for given score 
    """
    if s >= b - 10:
        grade = 'A'
    elif s >= b - 20:
        grade = 'B'
    elif s >= b - 30:
        grade = 'C'
    elif s >= b - 40:
        grade = 'D'
    else:
        grade = 'F'

    return grade

def display_score_and_grade(scores):
    """
    Description: Display the students score and grades
        : input : scores - the score the students received
    """
    # convert the scores from type string to type int
    s = [ eval(score) for score in scores]

    # determine best score in the list
    best = max(s)

    for idx, score in enumerate(s):
        print("Student {0:d} score is {1:d} and grade is {2}".
            format(idx, score, getGrade(score,best)))    

# prompt user for scores
while invalid_entry:
    # prompt user for the scores
    scores = input( "Enter the students' scores separated"\
        " by spaces on one line: ").split()
    for val in scores:
        try:
            # make sure each score is an integer
            val = int(val)
            invalid_entry = False
        except ValueError:
            print(ERROR_MESSAGE.format(val))
            invalid_entry = True


# output the score and grade for each student
display_score_and_grade(scores)
