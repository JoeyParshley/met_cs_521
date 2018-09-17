"""
   Joey Parshley
   MET CS 521 O2
   3 APR 2018
   hw_4_11_3
   Description: Rewrite Listing 11.2, GradeExam.py, to display the students in
   increasing order of the number of correct answers.

"""
def getListOfStudents(m,count,i):
    """
    Description: creates a list of list of the students each sublist 
        is a list consisting of the students correctCount and the students
        identification.
        :input m     : List - list of students to be created
        :input count : int - amount of corret answers
        :input i     : int - the index of the student to be added to list
    """
    m.append( [count, "Student {}".format(i) ] )

def displaySortedStudents(m):
    """
    Description: Sorts the student list in increasing order of correct answers
        and prints out the results
        :input m     : List - list of students to be created
        :input count : int - amount of corret answers
        :input i     : int - the index of the student to be added to list
    """
    m.sort()
    for student in range(len(m)):
        print("Student {0}'s correct count is {1}".format(student,m[student][0]))

def main():
    # Students' answers to the questions
    answers = [ 
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

    # Key to the questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D'] 
    students = []
    # Grade all answers
    for i in range(len(answers)):
        # Grade one student
        correctCount = 0
        for j in range(len(answers[i])): 
            if answers[i][j] == keys[j]:
                correctCount += 1
        # create a list of the list with each sublist 
        # being the student and thier correct count
        studentList = getListOfStudents(students,correctCount,i)

    # display the results
    displaySortedStudents(students)

main() # Call the main function
