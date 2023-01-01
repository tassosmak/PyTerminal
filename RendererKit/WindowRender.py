import customtkinter
from src import settings


DONE = False
def button_callback():
    global DONE
    DONE = True
    
    
num=1
def switch_callback():
    if (int(num) % 2) == 0:
        settings.EnableGUI=True
    num =+ 1
            
def opener():
    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

    app = customtkinter.CTk()
    app.geometry("780x480")
    app.title("PyTerminal-GUI Alpha")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=20, fill="both", expand=True)


    button_1 = customtkinter.CTkButton(master=frame_1, command=app.destroy, corner_radius=10, text='PyTerminal')
    button_1.pack(pady=110, padx=10)



    switch_1 = customtkinter.CTkSwitch(master=frame_1, command=switch_callback, text='Enable-GUI')
    switch_1.pack(pady=10, padx=10)




    app.mainloop()
    
if __name__ == "__main__":
    opener()