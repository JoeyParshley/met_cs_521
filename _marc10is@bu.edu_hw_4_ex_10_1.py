'''
* Marc Lowenthal
* MET CS 521
* Date
* Homework Problems 10_1
* Write a program that reads a list of scores and then assigns grades based
* on the highest score as best.

Example:
Enter student scores as integers separated by a space: 10 12 16 20 30 35 TT 40 45 50
TT is not an integer and no score will be calculated.
-----------------------------------------------------
The max score is: 50
Student  1 score is  10 and grade is D
Student  2 score is  12 and grade is D
Student  3 score is  16 and grade is D
Student  4 score is  20 and grade is C
Student  5 score is  30 and grade is B
Student  6 score is  35 and grade is B
Student  7 score is  TT and grade is n/c
Student  8 score is  40 and grade is A
Student  9 score is  45 and grade is A
Student 10 score is  50 and grade is A
'''
import sys

# Grade Ranges
GRADES = (('A',10),('B',20),('C',30),('D',40),('F'))

def find_grade(score, best):
    '''
    This function will calculate the letter grade associated with a number grade.
    A grade < 0 is not calculated.

    Parameters:
    score : The integer grade of the student
    best : The top integer score among all students, used to curve
           individual scores
    '''

    for g in GRADES:
        if score < 0:
            return 'n/c'
        elif g[0]=='F' or score >= best-g[1]:
            return g[0]


if __name__ == '__main__':
    # ask and read the scores of students
    scores = (input("Enter student scores as integers separated by a space: "))

    # split the scores and convert to integer
    # This needs to be done first so that max score can be calculated
    lst = []
    scores = scores.split()
    msg = '{} is not an integer and no score will be calculated.'
    for i in scores:
        # convert scores to int
        try:
            lst.append(int(i))
        except:
            lst.append(-1)
            print(msg.format(i))

    # Make sure that there is at least 1 valid score
    if len(lst) == 0:
        print('There are no valid scores.')
        sys.exit()

    # Get the max score
    max_score = max(lst)
    print('-'*len(msg))
    print('The max score is: {}'.format(max_score))

    # Print the individual grades
    for cntr, i in enumerate(lst):
        # call the find_grades() function to calculate individual letter grades
        print("Student {0:2} score is {1:>3} and grade is {2}".format(
            cntr+1,
            i if i >= 0 else scores[cntr],
            find_grade(i, max_score) if i >= 0 else 'n/c'))

