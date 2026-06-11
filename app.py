import streamlit as st

st.title("Week 1 Python Foundation Project")

menu = st.sidebar.selectbox(
    "Choose a program",
    [
        "Calculator",
        "Even/Odd Checker",
        "Factorial",
        "Fibonacci",
        "Marks Average",
        "Login System",
        "Student Management"
    ]
)

# ---------------- CALCULATOR ----------------
if menu == "Calculator":
    st.header("Simple Calculator")

    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")

    op = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate"):
        if op == "Add":
            st.success(a + b)
        elif op == "Subtract":
            st.success(a - b)
        elif op == "Multiply":
            st.success(a * b)
        elif op == "Divide":
            if b != 0:
                st.success(a / b)
            else:
                st.error("Cannot divide by zero")

# ---------------- EVEN ODD ----------------
elif menu == "Even/Odd Checker":
    num = st.number_input("Enter a number")

    if st.button("Check"):
        if num % 2 == 0:
            st.success("Even Number")
        else:
            st.success("Odd Number")

# ---------------- FACTORIAL ----------------
elif menu == "Factorial":
    n = st.number_input("Enter number", step=1)

    if st.button("Find Factorial"):
        fact = 1
        for i in range(1, int(n)+1):
            fact *= i
        st.success(fact)

# ---------------- FIBONACCI ----------------
elif menu == "Fibonacci":
    n = st.number_input("How many terms?", step=1)

    if st.button("Generate"):
        a, b = 0, 1
        series = []
        for i in range(int(n)):
            series.append(a)
            a, b = b, a + b
        st.success(series)

# ---------------- MARKS AVERAGE ----------------
elif menu == "Marks Average":
    marks = st.text_input("Enter marks separated by commas")

    if st.button("Calculate"):
        lst = list(map(int, marks.split(",")))
        avg = sum(lst) / len(lst)
        st.success(avg)

# ---------------- LOGIN SYSTEM ----------------
elif menu == "Login System":
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.success("Login Successful")
        else:
            st.error("Invalid credentials")

# ---------------- STUDENT MANAGEMENT ----------------
elif menu == "Student Management":
    st.header("Student Management System")

    if "students" not in st.session_state:
        st.session_state.students = []

    name = st.text_input("Name")
    sid = st.text_input("ID")

    if st.button("Add Student"):
        st.session_state.students.append({"id": sid, "name": name})
        st.success("Student Added")

    st.write("All Students:")
    st.write(st.session_state.students)