class Student:
    # Static variables for storing semester-wise toppers
    topper_list_sem1 = {}
    topper_list_sem2 = {}
    topper_list_sem3 = {}

    def __init__(self, name, student_id, semester, cgpa):
        """Initialize a student with name, ID, semester, and CGPA."""
        self.name = name
        self.student_id = student_id
        self.semester = semester
        self.cgpa = cgpa

    def get_details(self):
        """Return student details as a dictionary."""
        return {
            "Name": self.name,
            "ID": self.student_id,
            "Semester": self.semester,
            "CGPA": self.cgpa,
        }

    def display_details(self):
        """Display student details."""
        details = self.get_details()
        print(f"Name: {details['Name']}")
        print(f"ID: {details['ID']}")
        print(f"Semester: {details['Semester']}")
        print(f"CGPA: {details['CGPA']}")

    @staticmethod
    def update_topper_list(student, merit_position):
        """Update the topper list based on the student's semester."""
        if student.semester == 1:
            Student.topper_list_sem1[merit_position] = student.get_details()
        elif student.semester == 2:
            Student.topper_list_sem2[merit_position] = student.get_details()
        elif student.semester == 3:
            Student.topper_list_sem3[merit_position] = student.get_details()

    @staticmethod
    def display_topper_list(semester):
        """Display the topper list for a given semester."""
        if semester == 1:
            toppers = Student.topper_list_sem1
        elif semester == 2:
            toppers = Student.topper_list_sem2
        elif semester == 3:
            toppers = Student.topper_list_sem3
        else:
            print(f"Invalid semester: {semester}")
            return

        print(f"\nTopper List for Semester {semester}:")
        for position, details in toppers.items():
            print(f"Merit Position {position}: {details}")


# Example Usage
if __name__ == "__main__":
    # Create students
    student1 = Student("Manav", "0901AI231034", 1, 9.8)
    student2 = Student("Ashutosh", "0901AI231017", 1, 9.5)
    student3 = Student("Aditya", "0901AI231003", 2, 9.7)

    # Display student details
    student1.display_details()
    student2.display_details()
    student3.display_details()

    # Update topper lists
    Student.update_topper_list(student1, 1)  # Merit position 1
    Student.update_topper_list(student2, 2)  # Merit position 2
    Student.update_topper_list(student3, 1)  # Merit position 1 for semester 2

    # Display topper lists
    Student.display_topper_list(1)
    Student.display_topper_list(2)
    Student.display_topper_list(3)