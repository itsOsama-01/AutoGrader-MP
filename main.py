from tkinter import *
from customtkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import numpy as np
import os
import subprocess
import os
import re
from tkinter import font  # For custom font


global refrence_file, submission_file, incorrect, code_samples,tf1


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
            message_window, text="OK", command=message_window.destroy
        )
        message_button.pack()

#Utility function to find all the .java files in a particular folder

def find_java_files(path):

  java_files = []
  for root, _, files in os.walk(path):
    for file in files:
      if file.endswith(".java"):
        java_files.append(os.path.join(root, file))
  return java_files

def themeSwitch():
    val = switchTheme.get()
    if val:
        set_appearance_mode("light")
    else:
        set_appearance_mode("dark")


# Rewrite below 2
def uploadReference():
    global refrence_file,tf1
    refrence_file = filedialog.askdirectory(initialdir=".")
    tf1.insert(END,refrence_file)



#needs Edits
def executeSubmission():
    global submission_file, refrence_file, incorrect
    incorrect = []
    text.delete('1.0', END)
    expected = tf3.get()
    print(expected)
    array = expected.split(",")
    parent_file = submission_file
    print(parent_file)
    submissions = os.listdir(submission_file)
    for i in range(len(submissions)):
        if '.class' not in submissions[i]:
            out = subprocess.run('javac '+parent_file+'/'+submissions[i], stderr = subprocess.PIPE, shell=True)
            msg = out.stderr.splitlines()
            if len(msg) == 0:
                exe_name = submissions[i].split(".")
                out = subprocess.check_output('java -classpath '+parent_file+' '+exe_name[0]+' '+array[1]+' '+array[2]+' '+array[3], shell=True)
                output = out.decode().strip("\r\n").strip()
                if output != array[0]:
                    incorrect.append(submissions[i])
                text.insert(END,"Submission file: "+submissions[i]+" Generated Output: "+output+" Expected Output: "+array[0]+"\n\n")

def readFile(file_path):
    data = ""
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip('\n')
            line = line.strip()
            arr = line.split(" ")
            if len(arr) >= 2:
                if arr[0].strip() == 'if' or arr[1].strip() == 'if':
                    data += line+" "
    file.close()
    data = data.strip()
    return data

def calculateDiversePath(reference, submission):
    reference = re.sub('[()=]', '', reference)
    submission = re.sub('[()=]', '', submission)
    arr = submission.split(" ")
    return len(arr)


# Needs edits
def autoGrader():
    global submission_file, refrence_file, code_samples
    code_samples = []
    text.delete('1.0', END)

    reference = readFile(refrence_file+"/Ref1.java")
    code_samples.append(reference)
    submissions = os.listdir(submission_file)
    for i in range(len(submissions)):
        if '.class' not in submissions[i]:
            code = readFile("Submission/"+submissions[i])
            code_samples.append(code)

    for i in range(1,len(code_samples)):
        diverse = calculateDiversePath(code_samples[0],code_samples[i])
        if diverse > 6:
            text.insert(END,submissions[i-1]+" is an Incorrect submission\n\n")
        else:
            text.insert(END,submissions[i-1]+" is a Correct submission\n\n")

def showSubCode():
    file = find_java_files(submission_file)
    for f in file:
        java_file_path = f
        # Create a Toplevel window for each file
        sw = tk.Toplevel()
        JavaCodeViewer(sw, java_file_path)

def uploadAssingment():
    global tf1
    uploadWindow = CTkToplevel(main)
    uploadWindow.title("Upload an Assingment")
    uploadWindow.geometry("1100x600")
    uploadWindow.grab_set()

    tf1 = CTkEntry(master=uploadWindow, width=300)
    tf1.place(x=400, y=150)

    l = CTkLabel(master=uploadWindow, font=("Ariel", 20), text='Title of the Assignment: ')
    l.place(x=150, y=50)

    tf = CTkEntry(master=uploadWindow, width=300)
    tf.place(x=400, y=50)

    l11 = CTkLabel(master=uploadWindow, font=("Ariel", 20), text='Language : ')
    l11.place(x=150, y=100)

    om = CTkOptionMenu(master=uploadWindow, values=["Java", "Python"],
                       width=300)
    om.place(x=400, y=100)

    l1 = CTkLabel(master=uploadWindow, font=("Ariel", 20), text='Upload Reference File: ')
    l1.place(x=150, y=150)

    referenceButton = CTkButton(master=uploadWindow, text="Upload Reference File",
                                command=uploadReference)

    referenceButton.place(x=720, y=150)

    showButton = CTkButton(master=uploadWindow, text="Show Code",
                           command=showRefCode)
    showButton.place(x=870, y=150)

    uploadButton = CTkButton(master=uploadWindow, corner_radius=32, fg_color="#C850C0", hover_color="#4158D0",
                             text="Upload Assignment")
    uploadButton.place(relx=0.5, y=350, anchor="center")
    closeButton = CTkButton(master = uploadWindow,corner_radius=32, fg_color='#C850C0',hover_color="#4158D0", text="Close",
                            command=uploadWindow.destroy)
    closeButton.place(relx=0.85,y=450,anchor="center")
    uploadWindow.mainloop()

def showRefCode():
    file = find_java_files(refrence_file)
    for f in file:
        java_file_path = f  # Replace with your actual path
        root = tk.Tk()
        JavaCodeViewer(root, java_file_path)
        root.mainloop()
def AssignmentProgress(assignmentName):
    #Validate the assignments name with server
    #Grab all the submissions available from server
    #etc
    apWindow = CTkToplevel(main)
    apWindow.geometry("500x500")
    apWindow.grab_set()
    apWindow.title(assignmentName+"'s Submission Status")

    label = CTkLabel(apWindow,font=("Ariel",30),text="Show Progress Here!")
    label.place(relx=0.5,rely=0.5,anchor="center")

############################----UI----################################

main = CTk()  # create CTk window
main.geometry("1100x500")
main.title("AutoGrader: Professor's Interface")
set_appearance_mode("dark")

# Upload window defination


switchTheme = CTkSwitch(main,text = "Light Mode",onvalue=1,offvalue=0,command=themeSwitch)
switchTheme.pack(pady=20)

label1 = CTkLabel(main,text="Existing Assignments: ",font=("Ariel",30))
label1.place(x=100,y=100)

assigmentButton1 = CTkButton(main,text="Check Progress of 'Dummy Asingment 1'",command =lambda:AssignmentProgress("Dummy Asingment"),width=1000)
assigmentButton1.place(relx=0.5,y= 170,anchor="center")
assigmentButton2 = CTkButton(main,text="Check Progress of 'Dummy Asingment 2'",command =lambda:AssignmentProgress("Dummy Asingment1"),width=1000)
assigmentButton2.place(relx=0.5,y= 200,anchor="center")
assigmentButton3 = CTkButton(main,text="Check Progress of 'Dummy Asingment 3'",command =lambda:AssignmentProgress("Dummy Asingment2"),width=1000)
assigmentButton3.place(relx=0.5,y= 230,anchor="center")

uploadNew_Button = CTkButton(main,text="Upload new Assignment",command=uploadAssingment)
uploadNew_Button.place(relx=0.5,y=310,anchor="center")


main.mainloop()
