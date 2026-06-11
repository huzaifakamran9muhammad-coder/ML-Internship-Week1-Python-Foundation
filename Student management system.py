students = {}

while True:

    print("\n1.Add")
    print("2.View")
    print("3.Search")
    print("4.Update")
    print("5.Delete")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        sid = input("Student ID: ")
        name = input("Name: ")
        marks = input("Marks: ")

        students[sid] = {"name": name, "marks": marks}

    elif choice == "2":

        for sid, data in students.items():
            print(sid, data)

    elif choice == "3":

        sid = input("Enter ID: ")

        if sid in students:
            print(students[sid])
        else:
            print("Not found")

    elif choice == "4":

        sid = input("Enter ID: ")

        if sid in students:
            students[sid]["name"] = input("New name: ")
            students[sid]["marks"] = input("New marks: ")
        else:
            print("Student not found")

    elif choice == "5":

        sid = input("Enter ID: ")

        if sid in students:
            del students[sid]

    elif choice == "6":
        break

    else:
        print("Invalid Choice")
