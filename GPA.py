import tkinter as tk
from tkinter import messagebox


def calculate_gpa():
    try:
        num_courses = int(entry_courses.get())
        total_points = 0
        total_credits = 0

        for i in range(num_courses):
            credits = float(entries_credits[i].get())
            grade = float(entries_scores[i].get())

            # Map grades to grade points
            if grade >= 90:
                grade_points = 4.00
            elif 86 <= grade <= 89:
                grade_points = 3.0
            elif 82 <= grade <= 85:
                grade_points = 3.70
            elif 79 <= grade <= 81:
                grade_points = 3.00
            elif 75 <= grade <= 78:
                grade_points = 2.70
            elif 71 <= grade <= 74:
                grade_points = 2.30
            elif 68 <= grade <= 70:
                grade_points = 2.00
            elif 64 <= grade <= 67:
                grade_points = 1.70
            elif 60 <= grade <= 63:
                grade_points = 1.30
            elif grade < 60:
                grade_points = 0.00
            else:
                print("Invalid grade entered. Please try again.")
                continue

            total_points += grade_points * credits
            total_credits += credits

        if total_credits == 0:
            messagebox.showinfo("Result", "No credits entered. GPA cannot be calculated.")
        else:
            gpa = total_points / total_credits
            messagebox.showinfo("Result", f"Your GPA is: {gpa:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")


def create_entries():
    try:
        num_courses = int(entry_courses.get())
        for widget in course_frame.winfo_children():
            widget.destroy()

        global entries_credits, entries_scores
        entries_credits = []
        entries_scores = []

        for i in range(num_courses):
            tk.Label(course_frame, text=f"Course {i + 1} Credits:").grid(row=i, column=0)
            credit_entry = tk.Entry(course_frame)
            credit_entry.grid(row=i, column=1)
            entries_credits.append(credit_entry)

            tk.Label(course_frame, text=f"Course {i + 1} Score (0-100):").grid(row=i, column=2)
            score_entry = tk.Entry(course_frame)
            score_entry.grid(row=i, column=3)
            entries_scores.append(score_entry)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number of courses.")


# Create the main window
root = tk.Tk()
root.title("GPA Calculator")

# Create input fields for the number of courses
tk.Label(root, text="Number of Courses:").grid(row=0, column=0)
entry_courses = tk.Entry(root)
entry_courses.grid(row=0, column=1)

# Button to generate course input fields
tk.Button(root, text="Enter Courses", command=create_entries).grid(row=0, column=2)

# Frame to hold course entries
course_frame = tk.Frame(root)
course_frame.grid(row=1, column=0, columnspan=4)

# Button to calculate GPA
tk.Button(root, text="Calculate GPA", command=calculate_gpa).grid(row=2, column=1)

root.mainloop()
