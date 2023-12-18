import tkinter as tk
import subprocess
from tkinter import PhotoImage


def Case_1():

    scenario1= 'scenario1.py'
    subprocess.run(['/usr/bin/python3', scenario1])
    print("Button clicked")

def Case_2():

    scenario2= 'scenario2.py'
    subprocess.run(['/usr/bin/python3', scenario2])


def Case_3():

    scenario3= 'scenario3.py'
    subprocess.run(['/usr/bin/python3', scenario3])


window=tk.Tk()
window.title("Different cases")  
window.geometry("5000x5000") 
frame = tk.Frame(window, padx=20, pady=20, borderwidth=5, relief="solid")
frame.pack(pady=50)
title = tk.Label(frame, text="Different cases according \n GIEC reports", font=("Times", 40))
title.pack()


image1_path = "Initial.png"
output1_path = "resized1_image.png"
subprocess.run(["convert", image1_path, "-resize", "500x500", output1_path])
resized1_image = tk.PhotoImage(file=output1_path)
image_label1 = tk.Label(window, image=resized1_image)
image_label1.place(x=170, y=50) 
text_label1 = tk.Label(window, text="Lengend of the initial state", font=('Times', 15))
text_label1.place(relx=0.12, rely=0.37)


image2_path = "Final.png"
output2_path = "resized2_image.png"
subprocess.run(["convert", image2_path, "-resize", "600x600", output2_path])
resized2_image = tk.PhotoImage(file=output2_path)
image_label2 = tk.Label(window, image=resized2_image)
image_label2.place(x=1800, y=50) 
text_label2 = tk.Label(window, text="Lengend of the final state", font=('Times', 15))
text_label2.place(relx=0.81, rely=0.4)




button_style = {
    'borderwidth': 10,
    'relief': tk.GROOVE,
    'padx': 30,
    'pady': 50,
    'font': ('Times', 15),
    'width': 50,  
    'height': 20,
   
}


Case1=tk.Button(window, text='Choose scenario 1', command=Case_1,**button_style,bg='#17a589')
Case1.pack(side='left',padx=(100, 0), pady=(500, 0))
label_above_button1 = tk.Label(window, text="Corresponds to the best scenario possible according to the GIEC reports", font=('Times', 14))
label_above_button1.place(relx=0.05, rely=0.52)


Case2=tk.Button(window, text='Choose scenario 2', command=Case_2,**button_style,bg='#f7dc6f')
Case2.pack(side='left', padx=(270, 0), pady=(500, 0))
label_above_button2 = tk.Label(window, text="Corresponds to the intermediate scenario possible according to the GIEC reports", font=('Times', 14))
label_above_button2.place(relx=0.39, rely=0.52)


Case3=tk.Button(window, text='Choose scenario 3', command=Case_3,**button_style,bg='#e74c3c')
Case3.pack(side='left',padx=(300, 0), pady=(500, 0))
label_above_button3 = tk.Label(window, text="Corresponds to the worst scenario possible according to the GIEC reports", font=('Times', 14))
label_above_button3.place(relx=0.75, rely=0.52)


window.mainloop()
