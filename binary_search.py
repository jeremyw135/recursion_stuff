data = [
    (15001, "John", 0.05, 34),
    (30000, "Enping",2.7, 12),
    (28010, "Michael",3.9, 20),
    (17020, "Seikyung", 3.9, 27),
    (34921, "Haleh", 0.02, 8),
    (10002, "Abdul", 3.8, 121),
    (42131, "Paul", 3.9, 3),
    (10001, "Torbin", 3.7, 125),
]

def get_key(student_record):
    return student_record[0]

def binary_search(student_list, id_to_find):
    if len(student_list) <=0:
        None
    middle= len(student_list)//2
    middle_student= student_list[middle]
    if id_to_find == middle_student[0]:
        return middle_student
    if id_to_find < middle_student[0]:
        return binary_search(student_list[:middle],id_to_find)
    return binary_search(student_list[middle+1 w:],id_to_find)

def main():
    data.sort(key= get_key)
    id_to_find= int(input("Enter the Student ID to find: "))
    result= binary_search(data, id_to_find)
    if result :
        print(f"Found {result[1]} with {result[3]} credits and a GPA of {result[2]}")
    else:
        print("No such Student found")

if __name__ == '__main__':
    main()