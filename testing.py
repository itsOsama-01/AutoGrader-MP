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


main = CTk()  # create CTk window like you do with the Tk window
main.geometry("1100x500")

set_appearance_mode("dark")

global refrence_file, submission_file, incorrect, code_samples

def uploadReference():
    global refrence_file
    text.delete('1.0', END)
    refrence_file = filedialog.askdirectory(initialdir=".")
    text.insert(END,refrence_file+" loaded\n\n")
    tf1.insert(END,refrence_file)

def uploadSubmission():
    global submission_file
    submission_file = filedialog.askdirectory(initialdir=".")
    text.insert(END,submission_file+" loaded\n\n")
    tf2.insert(END,submission_file)

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

r = tk.Tk()
r.withdraw()
def showSubCode():
    file = find_java_files(submission_file)
    for f in file:
        java_file_path = f
        # Create a Toplevel window for each file
        sw = tk.Toplevel()
        JavaCodeViewer(sw, java_file_path)

def showRefCode():
    file = find_java_files(refrence_file)
    for f in file:
        java_file_path = f  # Replace with your actual path
        root = tk.Tk()
        JavaCodeViewer(root, java_file_path)
        root.mainloop()



#UI code (OLD STABLE)
l1 = CTkLabel(master = main,font=("Ariel",20), text='Upload Reference File: ')
l1.place(x=290,y=100,anchor="center")

tf1 = CTkEntry(main,width=350)
tf1.place(x=650,y=100,anchor="center")

referenceButton = CTkButton(master=main, text="Upload Reference File", command=uploadReference)
referenceButton.place(x=920,y=100,anchor = "center")

showButton = CTkButton(master= main,text = "Show Code",command = showRefCode)
showButton.place(x=1070,y=100,anchor="center")


#row2
l2 = CTkLabel(master = main,font=("Ariel",20), text='Upload Submission File:')
l2.place(x=290,y=150,anchor="center")

tf2 = CTkEntry(main,width=350)
tf2.place(x=650,y=150,anchor="center")

submissionButton = CTkButton(master = main, text="Upload Submission File", command=uploadSubmission)
submissionButton.place(x=920,y=150,anchor = "center")

showButton = CTkButton(master= main,text = "Show Code",command = showSubCode)
showButton.place(x=1070,y=150,anchor="center")

#row3
l3 = CTkLabel(master = main,font=("Ariel",20), text='Expected Output & Input Values')
l3.place(x=290,y=200,anchor="center")

tf3 = CTkEntry(master = main,width=350)
tf3.place(x=650,y=200,anchor = "center")


#Buttons
executeButton = CTkButton(master = main,corner_radius = 32,fg_color = "#C850C0",hover_color = "#4158D0", text="Execute Submission", command=executeSubmission)
executeButton.place(x=250,y=250,anchor= "center")

autoButton = CTkButton(master = main,corner_radius = 32,fg_color = "#C850C0",hover_color = "#4158D0", text="Run AutoGrader", command=autoGrader)
autoButton.place(x=480,y=250,anchor= "center")

text=CTkTextbox(master = main,height=500,width=1000,corner_radius = 16)
text.place(x=200,y=300)


# main.config(bg='chocolate1')
main.mainloop()
