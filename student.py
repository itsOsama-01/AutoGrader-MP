from tkinter import *
import tkinter as tk
from customtkinter import *
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import font

global submission_file


#MAke this a utility calss
class JavaCodeViewer:
    def __init__(self, master, java_file_path):
        self.master = master
        self.master.title("Java Code Viewer")
        self.master.geometry("800x600")

        # Create code display area
        self.code_text = tk.Text(
            master,
            wrap=tk.WORD,  # Wrap long lines
            font=font.Font(family="Monospace", size=12),  # Monospace font for code
            background="#f5f5f5",  # Light background
            highlightthickness=0,  # Remove text selection border
        )
        self.code_text.pack(fill=tk.BOTH, expand=True)

        # Open the specified Java file
        self.open_file(java_file_path)

    def open_file(self, file_path):
        try:
            with open(file_path, "r") as f:
                text = f.read()
            self.code_text.delete("1.0", tk.END)  # Clear previous content
            self.code_text.insert("1.0", text)
        except FileNotFoundError:
            message = f"Error: File not found: {file_path}"
            self.show_message(message)
        except Exception as e:
            message = f"Error: An unexpected error occurred: {str(e)}"
            self.show_message(message)

    def show_message(self, message):
        message_window = tk.Toplevel(self.master)
        message_window.title("Error")
        message_label = tk.Label(message_window, text=message)
        message_label.pack()
        message_button = tk.Button(
            message_window, text="OK", command=message_window.destroy and self.master.destroy
        )
        message_button.pack()
# def assignmentsView():
#     assignmentWindow = tkinter.Toplevel(main)
#     assignmentWindow.title("Available Assignmetns")
#     assignmentWindow.geometry("600x600")
#     assignmentWindow.grab_set()
#
#     table = ttk.Treeview(assignmentWindow,columns=("Title","Language","Submission Status"),show='headings')
#     table.heading('Title',text="Title")
#     table.heading('Language',text="Language")
#     table.heading('Submission Status',text="Submission Status")
#     table.pack()
def uploadSubmission(uploadPath):
    global submission_file
    filetypes = (('Java files', '*.java'),('Python files','*.py'), ('All files', '*.*'))
    file = filedialog.askopenfile(filetypes=filetypes,initialdir=".")
    # print(file.read()
    submission_file = file
    uploadPath.insert(END,submission_file)

def attemptAssignment(event):

    mssg= CTkMessagebox(main,title="Alert!",message="Attempt the Assignment?",option_1="Yes",option_2="No")
    if mssg.get() == "Yes":
        submissionWindow = CTkToplevel(main)
        submissionWindow.title("Submit")
        submissionWindow.geometry("1000x400")
        submissionWindow.grab_set()

        label = CTkLabel(submissionWindow,font=("Arial",20),text="Upload Submission file")
        label.place(rely=0.3,relx =0.15,anchor = "center")

        uploadPath = CTkEntry(submissionWindow,width=350)
        uploadPath.place(rely=0.3,relx=0.45,anchor="center")

        uploadButton = CTkButton(submissionWindow,text="Upload",command=lambda uploadPath=uploadPath: uploadSubmission(uploadPath))
        uploadButton.place(rely=0.3,relx=0.75,anchor="center")

        showCode = CTkButton(submissionWindow,text="Show Code",command = showCodefn)
        showCode.place(rely=0.3,relx=0.9,anchor='center')

        #ADD SUBMIT EVENTTT
        submitButton = CTkButton(submissionWindow,corner_radius=32, fg_color="#C850C0", hover_color="#4158D0",text="Submit")
        submitButton.place(rely=0.55,relx=0.5,anchor="center")


        cancelButton1 = CTkButton(submissionWindow,text="Cancel",command=submissionWindow.destroy)
        cancelButton1.place(relx = 0.8,rely=0.9,anchor="center")


    elif mssg.get() == "No":
        return
# def find_java_files(path):
#
#   java_files = []
#   for root, _, files in os.walk(path):
#     for file in files:
#       if file.endswith(".java"):
#         java_files.append(os.path.join(root, file))
#   return java_files
def showCodefn():
    # Replace with your actual path
    # root = tk.Tk()
    # JavaCodeViewer(root, submission_file)
    # root.mainloop()
    usWindow = tk.Toplevel()
    usWindow.geometry("800x600")
    usWindow.title("Code Viewer")
    usWindow.grab_set()
    code_text = tk.Text(
        usWindow,
        wrap=tk.WORD
    )

    text = submission_file.read()
    print(text)
    code_text.delete("1.0", tk.END)  # Clear previous content
    code_text.insert("1.0", text)


def loginStudent():
    if username.get() == "Osama" and password.get() == "786":
        CTkMessagebox(message="Login successful!",
                      title="Welcome!",
                      icon="check",
                      option_1="OK")
        main.deiconify()
        loginWindow.destroy()
    else:
       CTkMessagebox(loginWindow,title="Error",icon="cancel",message="Invalid credentials!")
def closeWindow():
    loginWindow.destroy()
    main.destroy()

#Main Window

main = CTk()
main.geometry("1100x600")
main.title("AutoGrader: Student's Interface")

treeStyle = ttk.Style()
treeStyle.configure("Treeview.Heading", font=("Arial", 20))
# treeStyle.configure("Treeview.content",font=("Arial",16))
table = ttk.Treeview(main,columns=("Title","Language","Problem Statement","Submission Status"),show='headings')
table.heading('Title',text="Title")
table.heading('Language',text="Language")
table.heading('Problem Statement',text="Problem Statement")
table.heading('Submission Status',text="Submission Status")
table.bind("<Double-1>",attemptAssignment)
table.pack(fill=BOTH,expand=True)

dummyTitles = ["Add 2 numbers","Find the prime number","Find factorial of a number"]
dummyLangueages = ["Python","Java","Java",]
dummyProblemStatements = ["Take two integers as input and find their sum","Find the prime number from the input array","Find the factorial of the given input integer"]
dummySubmissionStatus = ["Not Submitted Yet","Submitted","Submitted"]
# showAssignments = CTkButton(main,text="Show available Assignments",command=assignmentsView)
# showAssignments.place(relx=0.5,rely=0.5,anchor="center")

for data in zip(dummyTitles,dummyLangueages,dummyProblemStatements,dummySubmissionStatus):
    table.insert(parent="",index=0,values=data)



#Login window
loginWindow = CTkToplevel()
loginWindow.geometry("550x400")
loginWindow.title("Login")
set_appearance_mode("light")

usernameLabel = CTkLabel(loginWindow,font=("Ariel",20),text = "Username :")
usernameLabel.place(y=85,relx=0.18)

passwordLabel = CTkLabel(loginWindow,font=("Ariel",20),text = "Password :")
passwordLabel.place(y=185,relx=0.18)

username = CTkEntry(loginWindow,width=250)
username.place(rely= 0.25,relx=0.6,anchor="center")

password = CTkEntry(loginWindow,width=250)
password.place(rely=0.5,relx=0.6,anchor="center")

loginButton = CTkButton(loginWindow,text="Login",command=loginStudent)
loginButton.place(relx = 0.5,rely=0.9,anchor="center")

cancelButton = CTkButton(loginWindow,text="Cancel",command = closeWindow)
cancelButton.place(relx=0.7,rely=0.65)

main.withdraw()
main.mainloop()

