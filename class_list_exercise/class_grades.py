a = []
b = []
c = []
d = []
f = []

with open("class_grades.txt") as grade_file:
        grade_list = grade_file.readlines()

for grade in grade_list:
    grade = int(grade)
    if grade >= 90:
        a.append(grade)
    elif grade >= 80:
        b.append(grade)
    elif grade >= 70:
        c.append(grade)
    elif grade >= 60:
        d.append(grade)
    else:
        f.append(grade)

print "The A(s) are", a
print "The B(s) are", b
print "The C(s) are", c
print "The D(s) are", d
print "The F(s) are", f