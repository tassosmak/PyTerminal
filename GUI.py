import customtkinter
from UserHandler import init
from launcher import boot

def button_callback():
    init()
    while True:
        boot()

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("780x480")
app.title("PyTerminal-GUI Alpha")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)


button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, corner_radius=10, text='PyTerminal')
button_1.pack(pady=110, padx=10)




##########################
switch_1 = customtkinter.CTkSwitch(master=frame_1, command=lambda: print('Enable'), text='testing')
switch_1.pack(pady=10, padx=10)



app.mainloop()