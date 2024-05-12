import os
import tkinter as tk
import ctypes
from tkinter import filedialog

def open_file():
    file = filedialog.askdirectory()
    folder_path.set(file)

def rename_file():
    try:
        files = [f for f in os.listdir(folder_path.get()) if os.path.isfile(os.path.join(folder_path.get(), f))]
        pre = name_index_title_entry.get()
        for i, filename in enumerate(files):
            file_extension = os.path.splitext(filename)[1]
            new_name = pre + str(i + 1) + file_extension
            os.rename(os.path.join(folder_path.get(), filename), os.path.join(folder_path.get(), new_name))
    except Exception as e:
        print("its fine")

def add_file():
    for filename in os.listdir(folder_path.get()):
        if filename.endswith(".png"):  
            name_without_extension = os.path.splitext(filename)[0]
            txt_filename = f"{name_without_extension}.txt"
            txt_path = os.path.join(folder_path.get(), txt_filename)
        else:
            continue

def add_tag():
    mode = mode_select_menu_str.get()
    try:
        upper = int(range_select_upper.get())
    except Exception as e:
        print("its fine")
    lower = int(range_select_lower.get())
    msg = add_content_entry.get()
    if mode == "Range":
        for filename in os.listdir(folder_path.get()):
            if filename.endswith(".txt") and int(filename.split('.')[0]) >= lower and int(filename.split('.')[0]) <= upper:
                file = os.path.join(folder_path.get(),filename) 
                with open(file, 'a') as f:
                    f.write(msg + ",")
    elif mode == "One":
        for filename in os.listdir(folder_path.get()):
            if filename.endswith(".txt") and int(filename.split('.')[0]) == lower:  
                file = os.path.join(folder_path.get(),filename) 
                with open(file, 'a') as f:
                    f.write(msg + ",")
    else:
        for filename in os.listdir(folder_path.get()):
            if filename.endswith(".txt"):  
                file = os.path.join(folder_path.get(),filename) 
                with open(file, 'a') as f:
                    f.write(msg + ",")

window = tk.Tk()
window.title('Lora Train Tool')
window.geometry('1000x400')
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
window.tk.call('tk', 'scaling', ScaleFactor/75)

folder_path = tk.StringVar()
folder_path_text = tk.Label(window, text="Folder Path:")
folder_path_text.grid(row=0,column=0)
folder_path_button = tk.Button(window, text="Get",command=open_file)
folder_path_button.grid(row=0,column=1)
folder_path_label = tk.Label(window, textvariable=folder_path)  # 使用 textvariable 顯示路徑
folder_path_label.grid(row=0, column=2)

name_index_title_text = tk.Label(window, text="File Name (empty is ok):")
name_index_title_text.grid(row=1,column=0)
name_index_title_entry = tk.Entry(window)
name_index_title_entry.grid(row=1,column=1)

name_index_process_button = tk.Button(window, text="Rename the file(.png)", command=rename_file)
name_index_process_button.grid(row=1,column=2)

txt_file_add_text = tk.Label(window, text="Add .txt file")
txt_file_add_text.grid(row=2,column=0)
txt_file_add_button = tk.Button(window, text="Add", command=add_file)
txt_file_add_button.grid(row=2,column=1)

mode_select_text = tk.Label(window, text="choose mode:")
mode_select_text.grid(row=3,column=0)

mode_select_menu_str = tk.StringVar()
mode_select_menu = tk.OptionMenu(window,mode_select_menu_str, "All","Range","One")        
mode_select_menu.grid(row=3, column=1)

range_select_text = tk.Label(window,text="Lower and Upper bound:")
range_select_text.grid(row=4,column=0)
range_select_lower = tk.Entry(window)
range_select_lower.grid(row=4,column=1)
range_select_upper = tk.Entry(window)
range_select_upper.grid(row=4,column=2)

add_content_text = tk.Label(window,text="Add content:")
add_content_text.grid(row=5,column=0)
add_content_entry = tk.Entry(window)
add_content_entry.grid(row=5,column=1)
add_content_button = tk.Button(window,text="Add",command=add_tag)
add_content_button.grid(row=5,column=2)

window.mainloop()