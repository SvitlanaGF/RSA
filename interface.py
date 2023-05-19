import tkinter
from rsa import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("800x550")
root.title("RSA")
frame = customtkinter.CTkScrollableFrame(master=root, width=650, height=800)
frame.pack(pady=10, padx=40)

# Write p and q
label2 = customtkinter.CTkLabel(master=frame, text='Write p and q to generate keys:'
                                , font=('Roboto', 14))
label2.pack(pady=5, padx=10)
for_key = customtkinter.CTkEntry(master=frame, placeholder_text='p,q', width=250, height=30)
for_key.pack(pady=7, padx=5)


def gen_keys():
    inf = for_key.get().replace(' ', '')
    p = inf.split(',')
    print(generate_keys(int(p[0]), int(p[1])))


button1 = customtkinter.CTkButton(frame, text="Generate", command=gen_keys)
button1.pack(padx=20, pady=10)

# Choose you want to encrypt or decrypt the text
label1 = customtkinter.CTkLabel(master=frame, text='Do you want to encrypt or decrypt your text?'
                                , font=('Roboto', 14))
label1.pack(pady=12, padx=10)
choose_ciph = tkinter.IntVar()


def ciph_or_deciph():
    print('Encrypt the text') if choose_ciph.get() == 1 else print('Decrypt the text')


encr = customtkinter.CTkRadioButton(master=frame, text="Encrypt"
                                    , command=ciph_or_deciph, variable=choose_ciph, value=1)
decr = customtkinter.CTkRadioButton(master=frame, text="Decrypt"
                                    , command=ciph_or_deciph, variable=choose_ciph, value=2)
encr.pack(padx=20, pady=10)
decr.pack(padx=20, pady=10)

# Write key
label = customtkinter.CTkLabel(master=frame, text='Write key:'
                                , font=('Roboto', 14))
label.pack(pady=5, padx=10)
w_key = customtkinter.CTkEntry(master=frame, placeholder_text='key, n', width=250, height=30)
w_key.pack(pady=7, padx=5)
# Write file path
label3 = customtkinter.CTkLabel(master=frame, text='Files'
                                , font=('Roboto', 14))
label3.pack(pady=5, padx=10)
r_file = customtkinter.CTkEntry(master=frame, placeholder_text='Text', width=250, height=100)
w_file = customtkinter.CTkEntry(master=frame, placeholder_text='File to write', width=250, height=30)
r_file.pack(pady=7, padx=5)
w_file.pack(pady=7, padx=5)

# Button


def save_information():
    StartAlgorithm(information=r_file.get(), r_file=w_file.get(), key=w_key.get(), encrypt=choose_ciph.get()).work()


button = customtkinter.CTkButton(master=frame, text="Ok", command=save_information)
button.pack(padx=20, pady=10)


root.mainloop()

