
# Modern Graphical User Interfaces in Python - NeuralNine
# https://www.youtube.com/watch?v=iM3kjbbKHQU

import customtkinter

customtkinter.set_appearance_mode('dark') # system, light, dark
customtkinter.set_default_color_theme('dark-blue') # dark-blue, blue, green

root = customtkinter.CTk()
root.geometry('500x350') # window size
root.title("Login")

def login(user : str, password : str) -> None:
	print(user, password)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System")#, text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*") # show password as *s
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=lambda : login(entry1.get(), entry2.get()))
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me?")
checkbox.pack(pady=12, padx=10)

root.mainloop()
