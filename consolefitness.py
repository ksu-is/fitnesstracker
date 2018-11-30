'''
grade tracking program - think through the goal up front- what is the task and design?
needs to enable several basic functions for teachers
needs to have login to protect the student data
'''
#import libraries first
import statistics as s

#add constants next
admins = {'Faculty1':'abc123','Faculty2':'ABC123'}

students = {'Alex':[87,88,98],
            'Sally':[88,67,93],
            'Nboke':[90,88,78]}

#now define functions
def enterGrades():
    nameToEnter = input('Student name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in students:
        print('Adding grade for'+nameToEnter)
        students[nameToEnter].append(float(gradeToEnter)) #float will have a .0
        print(str(nameToEnter)+' now has these grades:')
        print(students[nameToEnter])
    else:
        print('Student not found. Please check your spelling or go back and add if new.')

def removeStudent():
    nameToRemove = input('Who do you want to remove? ')
    if nameToRemove in students:
        print('Removing '+nameToRemove)
        del students[nameToRemove]
        print(students)
    else:
        print('Student not found.')

def averageStudents():
    for student in students:
        grades = students[student]
        average = s.mean(grades)
        print(student,' average ',average)

def main():
    print("User: " + login)
    print("""
    Welcome to the Grade Tracker

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Averages
    [4] - Exit
    """)

    action = input('What would you like to do? (Enter a number) ')

    if action == '1':
        #print('1 selected')
        enterGrades()
    elif action == '2':
        #print('2 selected')
        removeStudent()
    elif action == '3':
        #print('3 selected')
        averageStudents()
    elif action == '4':
        #print('4 selected')
        exit()
    else:
        print('Valid option not selected.') #need to cause it to reprompt

login = input('User: ')
password = input('Password: ')

if login in admins:
    if admins[login] == password:
        print('Welcome,',login)
        #now run the code
        while True:
            main()
    else:
        print('Invalid password.')
else:
    print('Invalid user.')


