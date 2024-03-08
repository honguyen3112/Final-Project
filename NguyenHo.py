import tkinter as tk  # Import the tkinter module as tk for easy access
from tkinter import ttk  # Import the themed tkinter module
from tkinter import messagebox  # Import the messagebox module for displaying messages

  # Define the Student class to represent student objects
class Student:
      def __init__(self, full_name, username, password, class_name, email, phone_number):
          self.full_name = full_name  # Store the full name of the student
          self.username = username  # Store the username of the student
          self.password = password  # Store the password of the student
          self.class_name = class_name  # Store the class name of the student
          self.email = email  # Store the email of the student
          self.phone_number = phone_number  # Store the phone number of the student

  # Define the Teacher class to represent teacher objects
class Teacher:
      def __init__(self, full_name, username, password, subject_taught, email, phone_number):
          self.full_name = full_name  # Store the full name of the teacher
          self.username = username  # Store the username of the teacher
          self.password = password  # Store the password of the teacher
          self.subject_taught = subject_taught  # Store the subject taught by the teacher
          self.email = email  # Store the email of the teacher
          self.phone_number = phone_number  # Store the phone number of the teacher

  # Define the ManagementSystem class to manage students and teachers
class ManagementSystem:
      def __init__(self, master):
          self.master = master  # Store the root window
          self.master.title("Student and Teacher Management")  # Set the title of the root window

          self.student_list = []  # Initialize an empty list to store student objects
          self.teacher_list = []  # Initialize an empty list to store teacher objects

          self.create_widgets()  # Call the method to create GUI widgets

      # Method to create GUI widgets
      def create_widgets(self):
          self.style = ttk.Style()  # Create a ttk style object
          self.style.configure('TFrame', background='#f0f0f0')  # Configure style for frames
          self.style.configure('TButton', background='#0078d4', font=('Arial', 11))  # Configure style for buttons
          self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 11))  # Configure style for labels
          self.style.configure('TEntry', font=('Arial', 11))  # Configure style for entry fields

          # Create and pack the title label
          self.label_title = ttk.Label(self.master, text="Student and Teacher Management", font=("Helvetica", 18, "bold"))
          self.label_title.pack(pady=20)

          # Create a frame to hold buttons and pack it
          self.frame_buttons = ttk.Frame(self.master)
          self.frame_buttons.pack(pady=10)

          # Create and grid the button for student management
          self.button_students = ttk.Button(self.frame_buttons, text="Student Management", command=self.open_student_window)
          self.button_students.grid(row=0, column=0, padx=10)

          # Create and grid the button for teacher management
          self.button_teachers = ttk.Button(self.frame_buttons, text="Teacher Management", command=self.open_teacher_window)
          self.button_teachers.grid(row=0, column=1, padx=10)

      # Method to open the student management window
      def open_student_window(self):
          # Create a new Toplevel window for student management
          self.student_window = tk.Toplevel(self.master)
          self.student_window.title("Student Management")  # Set the title of the window

          # Create and pack the label for student list
          self.label_student_title = ttk.Label(self.student_window, text="Student List", font=("Helvetica", 14, "bold"))
          self.label_student_title.pack(pady=10)

          # Create a frame for student input fields and pack it
          self.frame_student_input = ttk.Frame(self.student_window)
          self.frame_student_input.pack(pady=10)

          # Create labels and entry fields for student information
          labels = ['Full Name:', 'Username:', 'Password:', 'Class Name:', 'Email:', 'Phone Number:']
          for i, label_text in enumerate(labels):
              label = ttk.Label(self.frame_student_input, text=label_text)
              label.grid(row=i, column=0, pady=5, padx=5, sticky='w')

          self.entry_student_full_name = ttk.Entry(self.frame_student_input)  # Entry field for full name
          self.entry_student_full_name.grid(row=0, column=1, pady=5, padx=5)

          self.entry_student_username = ttk.Entry(self.frame_student_input)  # Entry field for username
          self.entry_student_username.grid(row=1, column=1, pady=5, padx=5)

          self.entry_student_password = ttk.Entry(self.frame_student_input, show="*")  # Entry field for password
          self.entry_student_password.grid(row=2, column=1, pady=5, padx=5)

          self.entry_student_class_name = ttk.Entry(self.frame_student_input)  # Entry field for class name
          self.entry_student_class_name.grid(row=3, column=1, pady=5, padx=5)

          self.entry_student_email = ttk.Entry(self.frame_student_input)  # Entry field for email
          self.entry_student_email.grid(row=4, column=1, pady=5, padx=5)

          self.entry_student_phone_number = ttk.Entry(self.frame_student_input)  # Entry field for phone numberNguyeNNgngNg
          self.entry_student_phone_number.grid(row=5, column=1, pady=5, padx=5)

          # Create a button to add a student and pack it
          self.button_add_student = ttk.Button(self.student_window, text="Add Student", command=self.add_student)
          self.button_add_student.pack(pady=10)

          # Create a listbox to display students and pack it
          self.listbox_students = tk.Listbox(self.student_window, width=40, height=10)
          self.listbox_students.pack(pady=10)

      # Method to open the teacher management window
      def open_teacher_window(self):
          # Create a new Toplevel window for teacher management
          self.teacher_window = tk.Toplevel(self.master)
          self.teacher_window.title("Teacher Management")  # Set the title of the window

          # Create and pack the label for teacher list
          self.label_teacher_title = ttk.Label(self.teacher_window, text="Teacher List", font=("Helvetica", 14, "bold"))
          self.label_teacher_title.pack(pady=10)

          # Create a frame for teacher input fields and pack it
          self.frame_teacher_input = ttk.Frame(self.teacher_window)
          self.frame_teacher_input.pack(pady=10)

          # Create labels and entry fields for teacher information
          labels = ['Full Name:', 'Username:', 'Password:', 'Subject Taught:', 'Email:', 'Phone Number:']
          for i, label_text in enumerate(labels):
              label = ttk.Label(self.frame_teacher_input, text=label_text)
              label.grid(row=i, column=0, pady=5, padx=5, sticky='w')

          self.entry_teacher_full_name = ttk.Entry(self.frame_teacher_input)  # Entry field for full name
          self.entry_teacher_full_name.grid(row=0, column=1, pady=5, padx=5)

          self.entry_teacher_username = ttk.Entry(self.frame_teacher_input)  # Entry field for username
          self.entry_teacher_username.grid(row=1, column=1, pady=5, padx=5)

          self.entry_teacher_password = ttk.Entry(self.frame_teacher_input, show="*")  # Entry field for password
          self.entry_teacher_password.grid(row=2, column=1, pady=5, padx=5)

          self.entry_teacher_subject_taught = ttk.Entry(self.frame_teacher_input)  # Entry field for subject taught
          self.entry_teacher_subject_taught.grid(row=3, column=1, pady=5, padx=5)

          self.entry_teacher_email = ttk.Entry(self.frame_teacher_input)  # Entry field for email
          self.entry_teacher_email.grid(row=4, column=1, pady=5, padx=5)

          self.entry_teacher_phone_number = ttk.Entry(self.frame_teacher_input)  # Entry field for phone number
          self.entry_teacher_phone_number.grid(row=5, column=1, pady=5, padx=5)

          # Create a button to add a teacher and pack it
          self.button_add_teacher = ttk.Button(self.teacher_window, text="Add Teacher", command=self.add_teacher)
          self.button_add_teacher.pack(pady=10)

          # Create a listbox to display teachers and pack it
          self.listbox_teachers = tk.Listbox(self.teacher_window, width=40, height=10)
          self.listbox_teachers.pack(pady=10)

      # Method to add a student
      def add_student(self):
          # Get student information from entry fields
          full_name = self.entry_student_full_name.get()
          username = self.entry_student_username.get()
          password = self.entry_student_password.get()
          class_name = self.entry_student_class_name.get()
          email = self.entry_student_email.get()
          phone_number = self.entry_student_phone_number.get()

          # Check if all information is provided
          if full_name and username and password and class_name and email and phone_number:
              # Create a student object
              student = Student(full_name, username, password, class_name, email, phone_number)
              # Append the student object to the student list
              self.student_list.append(student)
              # Insert the student information into the listbox
              self.listbox_students.insert(tk.END, f"{student.full_name} - {student.username} - {student.password} - {student.class_name} - {student.email} - {student.phone_number}")
              # Show a success message
              messagebox.showinfo("Notification", "Student added successfully!")
          else:
              # Show a warning message if any information is missing
              messagebox.showwarning("Warning", "Please enter all student information.")

      # Method to add a teacher
      def add_teacher(self):
          # Get teacher information from entry fields
          full_name = self.entry_teacher_full_name.get()
          username = self.entry_teacher_username.get()
          password = self.entry_teacher_password.get()
          subject_taught = self.entry_teacher_subject_taught.get()
          email = self.entry_teacher_email.get()
          phone_number = self.entry_teacher_phone_number.get()

          # Check if all information is provided
          if full_name and username and password and subject_taught and email and phone_number:
              # Create a teacher object
              teacher = Teacher(full_name, username, password, subject_taught, email, phone_number)
              # Append the teacher object to the teacher list
              self.teacher_list.append(teacher)
              # Insert the teacher information into the listbox
              self.listbox_teachers.insert(tk.END, f"{teacher.full_name} - {teacher.username} - {teacher.password} - {teacher.subject_taught} - {teacher.email} - {teacher.phone_number}")
              # Show a success message
              messagebox.showinfo("Notification", "Teacher added successfully!")
          else:
              # Show a warning message if any information is missing
              messagebox.showwarning("Warning", "Please enter all teacher information.")

  # Main function to create the root window and start the application
def main():
      root = tk.Tk()  # Create the root window
      app = ManagementSystem(root)  # Create an instance of the ManagementSystem class
      root.mainloop()  # Start the tkinter event loop

  # Check if the script is being run directly
if __name__ == "__main__":
      main()  # Call the main function to start the application