import pandas as pd

students = {
    "id":[1,2,3,4,5,6],
    "name":["Alice","Bob","charlie","david","eva","frank"],
            "age": [20,21,19,22,20,23],
}
marks = {
    "id":[1,2,3,4,5,6],
    "student_id":[1,2,3,10,11,12],
    "math":[85,90,78,88,92,80],
    "science":[88,92,80,85,87,90],
    "English":[97,86,89,91,93,88]
}
studnetsdf = pd.DataFrame(students)
marksdf = pd.DataFrame(marks)
# print(studnets)
# print(marks)
# mergeds = pd.merge(
#     studnetsdf,
#     marksdf,
#     left_on='id',
#     right_on='student_id',
#     how='right'
# )
# print(mergeds)


concatinat = pd.concat([studnetsdf,marksdf],axis=1)
print(concatinat)