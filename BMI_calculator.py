import customtkinter

root = customtkinter.CTk()
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
root.geometry("450x360")

def calculat():
    weight = float(weight_ent.get())
    height = float(height_ent.get())

    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)
    print("random shit")
    if bmi < 19.0:
        final_result.configure(text_color='blue', text=f'your BMI is {bmi}.\n you need to gian more weight')
    elif bmi < 24.5:
        final_result.configure(text_color='green', text=f"your BMI is {bmi}.\n you don't need to change your weight")
    else:
        final_result.configure(text_color='orange', text=f"your BMI is {bmi}.\n you need to loose weight")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="login system")
label.pack(pady=12, padx=10)

weight_ent = customtkinter.CTkEntry(master=frame, placeholder_text="weight entry:")
weight_ent.pack(pady=12, padx=10)

height_ent = customtkinter.CTkEntry(master=frame, placeholder_text="hight entry:")
height_ent.pack(pady=12, padx=10)

calculat_button = customtkinter.CTkButton(master=frame, text="calculat", command=calculat)
calculat_button.pack(pady=12, padx=10)

final_result = customtkinter.CTkLabel(master=frame,text_color="green", text="")
final_result.pack(pady=12, padx=10)
root.mainloop()