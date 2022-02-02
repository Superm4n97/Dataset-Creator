import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import execution
import load_objects

root = tk.Tk()
root.geometry("600x400")
root.title("Dataset Creator")

def runDetection():
    if objectChoosen.current() == 0:
        error_txt.set('Choose a valid object')
        return
    elif input_path.get() == '':
        error_txt.set('No video file selected')
        return
    elif output_path.get() == '':
        error_txt.set('No output folder selected')
        return
    else:
        error_txt.set('')

    execution.createDataset(input_path.get(),output_path.get(),objectChoosen['value'][objectChoosen.current()])
    
#file dialog for video input
def getVideoPath():
    path = filedialog.askopenfilename(filetypes=[("Video","*.mp4")])
    if path:
        input_path.set(path)
        if error_txt.get() == 'No video file selected':
            error_txt.set('')

#file dialog for output folder
def getOutputFolder():
    path = filedialog.askdirectory()
    if path:
        output_path.set(path)
        if error_txt.get() == 'No output folder selected':
            error_txt.set('')

#changable global strings
error_txt = tk.StringVar(root)
input_path = tk.StringVar(root)
output_path = tk.StringVar(root)
error_txt.set('')
input_path.set('')
output_path.set('')
error_lb = tk.Label(root, textvariable=error_txt,fg='red').place(x=200,y=250)

#input file section
input_text = tk.Label(root, text='Input From: ').place(x=40 , y=35)
input_file_lb = tk.Label(root,textvariable=input_path).place(x=170,y=32)
browse_input_btn = tk.Button(root, text='Browse',bd=3,command=getVideoPath).place(x=110,y=30)

#output folder section
output_folder_lb = tk.Label(root,textvariable=output_path).place(x=180,y=83)
output_text = tk.Label(root, text='Output Folder: ').place(x=40 , y=85)
browse_output_btn = tk.Button(root, text='Browse',bd=3,command=getOutputFolder).place(x=125,y=80)

v = tk.StringVar()
objectChoosen = ttk.Combobox(root, width=20, textvariable=v)
objectChoosen['value'] = load_objects.load_classes()

objectChoosen.grid(column=1, row=15)
objectChoosen.current(0)
objectChoosen.place(x=50,y=150)

run_btn = tk.Button(root, text='RUN', bg='light green', bd=3 , command=runDetection).place(x=250,y=320)
exit_btn = tk.Button(root, text='EXIT',bg='red', bd=3 , command=root.destroy).place(x=350,y=320)

root.mainloop()