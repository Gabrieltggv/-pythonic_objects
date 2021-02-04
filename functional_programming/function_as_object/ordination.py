puplis = [('Gabriel', 0), ('Glauco', 6), ('Vinicius', 8), ('Theo', 10)]

puplis.sort(key=lambda student: student[1])

print(puplis)


def by_name(student):
    return student[0]


print(sorted(puplis, key=by_name))
