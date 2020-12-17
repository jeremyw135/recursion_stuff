list_of_students=[

]

def binary_search(student_list, id_to_find):
    if len(student_list) <=0:
        None
    middle= len(student_list)//2
    middle_student= student_list[middle]
    if id_to_find == middle_student[0]:
        return middle_student
    if id_to_find < middle_student[0]:
        return binary_search(student_list[:middle],id_to_find)
    return binary_search(student_list[middle+1:],id_to_find)

def main():
    id_to_find= int(input("Enter the Student ID to find: "))
    result= binary_search(list_of_students, id_to_find)
    if result :
        print(f"Found {result[1]} with {result[2]} credits and a GPA of {result[3]}")
    else:
        print("No such Student found")

main()