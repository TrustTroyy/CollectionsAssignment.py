def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    student_name = input("Enter the student's name: ")

    grade1 = float(input("Enter grade 1: "))
    grade2 = float(input("Enter grade 2: "))
    grade3 = float(input("Enter grade 3: "))
    grade4 = float(input("Enter grade 4: "))
    grade5 = float(input("Enter grade 5: "))

    grades = [grade1, grade2, grade3, grade4, grade5]
    average = sum(grades) / len(grades)

    letter_grade = get_letter_grade(average)

    print(f"\n{student_name}\nAverage: {average:.1f}\nLetter Grade: {letter_grade}")

if __name__ == "__main__":
    main()