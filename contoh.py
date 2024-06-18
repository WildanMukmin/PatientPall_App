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

        # <---------------------- STYLE LABEL ---------------------->

        # <---------------------- STYLE ENTRY ---------------------->

        # <---------------------- STYLE BUTTON ---------------------->

        # <---------------------- STYLE LIST ITEM ---------------------->

        self.login_page()


    def login_page(self):
        self.canvas_login = tk.Canvas(self, bg = "#FFFFFF",height = 1024,width = 1365,bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas_login.place(x = 0, y = 0)
        self.canvas_login.create_rectangle(0.0, 0.0, 1365.0, 1070.0, fill="#4880FF", outline="")
        self.canvas_login.create_rectangle(405.0, 10.0, 1035.0, 698.0, fill="#FFFFFF", outline="")
        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas_login.create_image(720.0, 439.0, image=entry_image_1)
        entry_1 = Entry(bd=0, bg="#F1F4F9", fg="#000716", highlightthickness=0)
        entry_1.place(x=470.0, y=411.0, width=500.0, height=54.0)
        self.canvas_login.create_text(462.0,371.0,anchor="nw",text="Password",fill="#202224",font=("NunitoSans SemiBold", 18 * -1))
        self.canvas_login.create_text(845.0, 371.0, anchor="nw", text="Lupa Password?", fill="#202224", font=("NunitoSans SemiBold", 18 * -1))
        self.canvas_login.create_text(498.0, 291.0, anchor="nw", text="Remember Password", fill="#202224", font=("NunitoSans SemiBold", 18 * -1))
        self.canvas_login.create_text(478.0, 291.0, anchor="nw", text="wildanmukmin26@gmail.com", fill="#A6A6A6", font=("NunitoSans SemiBold", 18 * -1))
        self.canvas_login.create_text(462.0, 235.0, anchor="nw", text="Email:", fill="#202224", font=("NunitoSans SemiBold", 18 * -1))
        self.canvas_login.create_text(679.0, 113.0, anchor="nw", text="Login", fill="#202224", font=("NunitoSans Bold", 32 * -1))
        self.canvas_login.create_text(504.0, 166.0, anchor="nw", text="Mohon Masukan Email Dan Password Dengan Benar!", fill="#202224", font=("NunitoSans SemiBold", 18 * -1))
        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.button_1 = Button(image=self.button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("self.button_1 clicked"), relief="flat")
        self.button_1.place(x=462.0, y=491.0, width=24.0, height=24.0)
        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas_login.create_image(918.8333129882812, 438.5, image=self.image_image_1)
        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas_login.create_image(720.0, 303.0, image=self.entry_image_2)
        self.entry_2 = Entry(bd=0, bg="#F1F4F9", fg="#000716", highlightthickness=0)
        self.entry_2.place(x=470.0, y=275.0, width=500.0, height=54.0)
        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.button_2 = Button(image=self.button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("self.button_2 clicked"), relief="flat")
        self.button_2.place(x=511.0, y=571.0, width=418.0, height=56.0)

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

# <---------------------- Main program ---------------------->
if __name__ == "__main__":
    app = PatientPallApp()
    app.mainloop()
# <---------------------- End Main program ---------------------->
