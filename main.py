def get_students():
    pass
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