def get_students():
    students = {}
    for i in range(10):
        name = input("Enter student name: ")
        marks  = input("Enter student marks: ")
        final = input("Enter final marks: ")
        students[name] = {'marks': marks, 'final': final}
    return students

def academ_integrity(students:dict):
    result = {}
    for name, marks in students.items():
        if -2<marks['marks'] - marks['final'] < 2:
            result[name] = 'good'
        else:
            result[name] = 'bad'
    return result


def program():
    pass