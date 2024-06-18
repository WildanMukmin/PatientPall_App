import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import Canvas, Entry, Button, PhotoImage

# Define dimensions
w = 1365
h = 700

# Output path
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Hp\Desktop\PatientPall_App\assets\frame_login_admin")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class PatientPallApp(tk.Tk):
    global ASSETS_PATH
    def __init__(self):
        super().__init__()
        self.title("Admin PatientPall App")
        self.geometry("1365x700")
        # self.attributes('-fullscreen', True)
        # self.resizable(False, False)
        

        # <---------------------- ALL STYLE CONFIGURE ---------------------->
        self.style = ttk.Style(self)

        # <---------------------- STYLE FRAME ---------------------->
        self.style.configure("background_login_frame.TFrame", background = "#4880FF")
        self.style.configure("login_frame.TFrame", background = "white")
        self.style.configure("frame_form_email.TFrame", background = "white")
        self.style.configure("frame_form_password.TFrame", background = "white")
        
        # <---------------------- STYLE LABEL ---------------------->
        self.style.configure("label_login.TLabel", background = "white", font=("NunitoSans", 28, "bold"))
        self.style.configure("label_bawah_login.TLabel", background = "white", font=("NunitoSans", 10, ))
        self.style.configure("label_email.TLabel", background = "white", font=("NunitoSans", 10, ))
        self.style.configure("label_password.TLabel", background = "white", font=("NunitoSans", 10, ))
        self.style.configure("label_remember_password.TLabel", background = "white", font=("NunitoSans", 10, ))

        # <---------------------- STYLE ENTRY ---------------------->
        self.style.configure("email_entry.TEntry", background = "#D8D8D8", font=("NunitoSans", 20, ))
        self.style.configure("password_entry.TEntry", background = "#D8D8D8", font=("NunitoSans", 20, ))

        # <---------------------- STYLE BUTTON ---------------------->
        self.style.configure("button_login.TButton", background = "#D8D8D8", font=("NunitoSans", 10, "bold"))

        # <---------------------- STYLE LIST ITEM ---------------------->

        self.window = ttk.Frame(self)
        self.window.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.login_page()


    def login_page(self):
        # <-------------- BACKGROUND -------------->
        self.background_login_frame = ttk.Frame(self.window, style="background_login_frame.TFrame")
        self.background_login_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # <-------------- INPUT -------------->
        self.login_frame = ttk.Frame(self.background_login_frame, style="login_frame.TFrame")
        self.login_frame.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.8, anchor=tk.CENTER)
        
        # <-------------- HEADER -------------->
        self.label_login = ttk.Label(self.login_frame, style="label_login.TLabel", text="Login")
        self.label_login.place(anchor=tk.CENTER, relx=0.5 , y= 80)
        
        self.label_bawah_login = ttk.Label(self.login_frame, style="label_bawah_login.TLabel", text="Mohon Masukan Email Dan Password Dengan Benar!")
        self.label_bawah_login.place(anchor=tk.CENTER, relx=0.5 , y= 120)
    
        # <-------------- FORM EMAIL -------------->
        self.frame_form_email = ttk.Frame(self.login_frame, style="frame_form_email.TFrame")
        self.frame_form_email.place(relx=0.5, y=200, width=340, height=70, anchor=tk.CENTER)
        
        self.label_email = ttk.Label(self.frame_form_email, style="label_email.TLabel", text="Email:")
        self.label_email.place(anchor=tk.CENTER, relx=0.1 , y= 10)
        
        self.email_entry = ttk.Entry(self.frame_form_email, style="email_entry.TEntry")
        self.email_entry.place(anchor=tk.CENTER, relx=0.5 , y= 40, relwidth=0.9, relheight=0.5)
        
        # <-------------- FORM PASSWORD -------------->
        self.frame_form_password = ttk.Frame(self.login_frame, style="frame_form_password.TFrame")
        self.frame_form_password.place(relx=0.5, y=320, width=340, height=120, anchor=tk.CENTER)
        
        self.label_password = ttk.Label(self.frame_form_password, style="label_password.TLabel", text="Password:")
        self.label_password.place(anchor=tk.CENTER, relx=0.135 , y= 10)
        
        self.password_entry = ttk.Entry(self.frame_form_password, style="password_entry.TEntry")
        self.password_entry.place(anchor=tk.CENTER, relx=0.5 , y= 40, relwidth=0.9, relheight=0.3)
        
        self.label_remember_password = ttk.Label(self.frame_form_password, style="label_remember_password.TLabel", text="Remember Password")
        self.label_remember_password.place(anchor=tk.CENTER, relx=0.23 , y= 80)
        
        # <-------------- BUTTON LOGIN -------------->
        self.button_login = ttk.Button(self.login_frame, text="Login", command=lambda e: print("button login is press") , style='button_login.TButton')
        self.button_login.place(relx=0.5, y=440, anchor=tk.CENTER, relwidth=0.7, height=40)

        
        
    
    def clear_content_frame(self):
        for widget in self.window.winfo_children():
            widget.destroy()

# <---------------------- Main program ---------------------->
if __name__ == "__main__":
    app = PatientPallApp()
    app.mainloop()
# <---------------------- End Main program ---------------------->
