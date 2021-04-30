import tkinter as tk
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.ttk
import tkinter.font
from tkinter import messagebox
from PIL import ImageTk, Image
import json

import importlib
import StateCourt


#----------------------------------------------------------------------------#

# Welcome Frame
def create_widgets_in_welcome_frame():

    global new_apbi
    global new_mmbi
    global new_qbi

    # Sets font styles
    welcome_font = tkinter.font.Font(size=24, weight="bold")
    welcome_desc_font = tkinter.font.Font(size=12)
    welcome_frame_button_font = tkinter.font.Font(size=12)

    # Create the label for the frame
    welcome = ttk.Label(first_frame, text ="Welcome to the Magic Motion Maker.", font = welcome_font, foreground="#000000")
    welcome_desc = ttk.Label(first_frame, text="Save time by saving signature blocks, "
                    "legal motion templates, and auto formatting motions.", font=welcome_desc_font)

    # Positions the labels
    welcome.grid(column=0, row=0, sticky="ew")
    welcome_desc.grid(column=0, row=1, pady=10, sticky="ew")

    # Configures the labels
    welcome.config(anchor="center")
    welcome_desc.config(anchor="center")

    # Create the button for the frame
    # Attorney Profile Button
    ap_button_img = Image.open("C:/Users/Jeffrey/PycharmProjects/MotionMaker/GUI/Buttons/APButton.png")
    apb_resized = ap_button_img.resize((50, 50), Image.ANTIALIAS)

    new_apbi = ImageTk.PhotoImage(apb_resized)

    attorney_profiles_button = tk.Button(first_frame, text="                                                          "
                                         "     Manage Attorney Profile", image=new_apbi, width=300,
                                         borderwidth=0, fg="#FFFFFF", bg="#3A4B64", activebackground="#3A4B64",
                                         activeforeground="#FFFFFF", command=call_second_frame_on_top, anchor="w",
                                         font=welcome_frame_button_font, compound=LEFT)

    attorney_profiles_button.grid(column=0, row=2, pady=10, sticky="ew")

    # Make Motion Button
    mm_button_img = Image.open("C:/Users/Jeffrey/PycharmProjects/MotionMaker/GUI/Buttons/CheckButton.png")
    mmb_resized = mm_button_img.resize((50, 50), Image.ANTIALIAS)

    new_mmbi = ImageTk.PhotoImage(mmb_resized)

    make_motion_button = tk.Button(first_frame, text="                                                          "
                                         "            Make a Motion", image=new_mmbi, width=300,
                                         borderwidth=0, fg="#FFFFFF", bg="#3A4B64", activebackground="#3A4B64",
                                         activeforeground="#FFFFFF", command=call_third_frame_on_top, anchor="w",
                                         font=welcome_frame_button_font, compound=LEFT)

    make_motion_button.grid(column=0, row=3, pady=10, sticky="ew")

    # Quit Button

    quit_button_img = Image.open("C:/Users/Jeffrey/PycharmProjects/MotionMaker/GUI/Buttons/QuitButton.png")
    qbi_resized = quit_button_img.resize((50, 50), Image.ANTIALIAS)

    new_qbi = ImageTk.PhotoImage(qbi_resized)

    welcome_quit_button = tk.Button(first_frame, text="                        Quit", image=new_qbi, width=300,
                                         borderwidth=0, fg="#FFFFFF", bg="#3A4B64", activebackground="#3A4B64",
                                         activeforeground="#FFFFFF", command=root.quit, anchor="w",
                                         font=welcome_frame_button_font, compound=LEFT)
    welcome_quit_button.grid(column=0, row=6, pady=10)

#----------------------------------------------------------------------------#

# Attorney Profile Forms
def current_ap():
    # Form Fonts
    form_font = tkinter.font.Font(size=12)
    form_font_bold = tkinter.font.Font(weight="bold", size=14)
    form_font_bold_ul = tkinter.font.Font(weight="bold", size=14, underline=True)

    with open('ap.json', 'r') as infile:
        data = json.load(infile)

    for items in data['attorney']:
        # Current Profile Lables
        curr_profile = ttk.Label(form_frame, text="Current Profile", font=form_font_bold_ul, foreground="#000000")
        name_c = ttk.Label(form_frame, text="Name:", font=form_font)
        firm_name_c = ttk.Label(form_frame, text="Firm Name:", font=form_font)
        bar_number_c = ttk.Label(form_frame, text="Bar Number:", font=form_font)
        address_c = ttk.Label(form_frame, text="Address:", font=form_font)
        phone_c = ttk.Label(form_frame, text="Phone:", font=form_font)
        fax_c = ttk.Label(form_frame, text="Fax:", font=form_font)

        curr_profile.grid(row=2, column=0)
        name_c.grid(row=3, column=0, sticky="w")
        firm_name_c.grid(row=4, column=0, sticky="w")
        bar_number_c.grid(row=5, column=0, sticky="w")
        address_c.grid(row=6, column=0, sticky="w")
        phone_c.grid(row=8, column=0, sticky="w")
        fax_c.grid(row=9, column=0, sticky="w")


        global curr_name_entry, curr_firm_entry, curr_bar_entry, curr_address_1_entry, curr_address_2_entry,\
            curr_phone_entry, curr_fax_entry
        # Current Profile Strings
        curr_name_entry = ttk.Label(form_frame, text=items['name'],  wraplength=100, padding=(8,0,12,0))
        curr_firm_entry = ttk.Label(form_frame, text=items['firm'],  wraplength=100, padding=(8,0,12,0))
        curr_bar_entry = ttk.Label(form_frame, text=items['bar'],  wraplength=100, padding=(8,0,12,0))
        curr_address_1_entry = ttk.Label(form_frame, text=items['address_1'], wraplength=100, padding=(8,0,12,0),
                                                                                                    justify="left")
        curr_address_2_entry = ttk.Label(form_frame, text=items['address_2'], wraplength=100, padding=(8, 0, 12, 0),
                                         justify="left")
        curr_phone_entry = ttk.Label(form_frame, text=items['phone'], padding=(8,0,8,0), wraplength=100)
        curr_fax_entry = ttk.Label(form_frame, text=items['fax'], wraplength=100, padding=(8,0,12,0))

        curr_name_entry.grid(row=3, column=1, sticky="w")
        curr_firm_entry.grid(row=4, column=1, sticky="w")
        curr_bar_entry.grid(row=5, column=1, sticky="w")
        curr_address_1_entry.grid(row=6, column=1, sticky="w")
        curr_address_2_entry.grid(row=7, column=1, sticky="w")
        curr_phone_entry.grid(row=8, column=1, sticky="w")
        curr_fax_entry.grid(row=9, column=1, sticky="w")


def update_current_ap():

    with open('ap.json', 'r') as infile:
        data = json.load(infile)

    for items in data['attorney']:

        curr_name_entry.configure(text=items['name'])
        curr_firm_entry.configure(text=items['firm'])
        curr_bar_entry.configure(text=items['bar'])
        curr_address_1_entry.configure(text=items['address_1'])
        curr_address_2_entry.configure(text=items['address_2'])
        curr_phone_entry.configure(text=items['phone'])
        curr_fax_entry.configure(text=items['fax'])


def ap_form():

    # Form Fonts
    form_font = tkinter.font.Font(size=12)
    form_font_bold_ul = tkinter.font.Font(weight="bold", size=14, underline=True)

    current_ap()

    # New Profile Labels
    new_profile = ttk.Label(form_frame, text="New Profile", font=form_font_bold_ul, foreground="#000000")
    name = ttk.Label(form_frame, text="Name", font=form_font)
    firm_name = ttk.Label(form_frame, text="Firm Name", font=form_font)
    bar_number = ttk.Label(form_frame, text="Bar Number", font=form_font)
    address = ttk.Label(form_frame, text="Address", font=form_font)
    phone = ttk.Label(form_frame, text="Phone", font=form_font)
    fax = ttk.Label(form_frame, text="Fax", font=form_font)


    new_profile.grid(row=2, column=2)
    name.grid(row=3, column=2, sticky="w")
    firm_name.grid(row=4, column=2, sticky="w")
    bar_number.grid(row=5, column=2, sticky="w")
    address.grid(row=6, column=2, sticky="w")
    phone.grid(row=8, column=2, sticky="w")
    fax.grid(row=9, column=2, sticky="w")

    global name_entry, firm_entry, bar_entry, address_1_entry, address_2_entry, phone_entry, fax_entry

    # New Profile Entry Blocks
    name_entry = ttk.Entry(form_frame,  width=30, font=form_font)
    firm_entry = ttk.Entry(form_frame, width=30, font=form_font)
    bar_entry = ttk.Entry(form_frame,  width=30, font=form_font)
    address_1_entry = ttk.Entry(form_frame, width=30, font=form_font)
    address_2_entry = ttk.Entry(form_frame, width=30, font=form_font)
    phone_entry = ttk.Entry(form_frame,  width=30, font=form_font)
    fax_entry = ttk.Entry(form_frame,  width=30, font=form_font)


    name_entry.grid(row=3, column=3, ipady=2, pady=5)
    firm_entry.grid(row=4, column=3, ipady=2, pady=5)
    bar_entry.grid(row=5, column=3, ipady=2, pady=5)
    address_1_entry.grid(row=6, column=3, ipady=2, pady=5)
    address_2_entry.grid(row=7, column=3, ipady=2, pady=5)
    phone_entry.grid(row=8, column=3, ipady=2, pady=5)
    fax_entry.grid(row=9, column=3, ipady=2, pady=5)


def get_entries():

    global attorney_info

    name_get = name_entry.get()
    firm_get = firm_entry.get()
    bar_get = bar_entry.get()
    address_1_get = address_1_entry.get()
    address_2_get = address_2_entry.get()
    phone_get = phone_entry.get()
    fax_get = fax_entry.get()

    return {"attorney": [{'name': name_get,
                              'firm': firm_get,
                             'bar': bar_get,
                          'address_1': address_1_get,
                          'address_2': address_2_get,
                          'phone': phone_get,
                          'fax': fax_get}]}

def save_to_json():

    with open('ap.json', 'w') as outfile:
        json.dump(get_entries(), outfile, indent=2)

    messagebox.showinfo("Success", "Attorney information updated.")

    update_current_ap()

# Attorney Profile Frame
def create_widgets_in_ap_frame():

    # Sets font styles
    title_font = tkinter.font.Font(size=24, weight="bold")
    title_desc_font = tkinter.font.Font(size=12)

    # Create the label for the frame
    ap_title = ttk.Label(second_frame, text='Attorney Profile', font=title_font, foreground="#000000")
    ap_title.grid(column=0, row=0, pady=10, padx=10, sticky="ew")
    ap_desc = ttk.Label(second_frame, text='Changes made here will modify signature block information.',
                                font=title_desc_font)
    ap_desc.grid(column=0, row=1, pady=10, padx=10, sticky="ew")

    # Configures the labels
    ap_title.config(anchor="center")
    ap_desc.config(anchor="center")

    ap_form()

    # Create the button for the frame
    second_window_back_button = ttk.Button(button_ap_frame, text="Back", command =call_first_frame_on_top)
    second_window_back_button.grid(column=0, row=9, pady=10, padx=130, sticky='w')

    save_changes_button = ttk.Button(button_ap_frame, text="Save Changes", command=save_to_json)
    save_changes_button.grid(column=1, row=9, pady=10, padx=130, sticky="e")

#----------------------------------------------------------------------------#

# Motion making frame


def get_cause_search_entry():
    cause_search_get = cause_entry.get()
    import_count = 1

    with open('cause_search_entry.txt', 'w') as outfile:
        json.dump(cause_search_get, outfile)

    import CourtData

    if import_count <= 0:
        importlib.reload(CourtData)

    import_count -= 1

    #execfile('CourtData.py')

    messagebox.showinfo("Success", "Case information retrieved.")

    update_court_data()

def updated_case_info():
    # Updated Display
    global cause_new, plaintiff_new, defendant_new, court_new, opposing_counsel_new, judge_new

    cause_new = ttk.Label(cause_search_frame, text="")
    plaintiff_new = ttk.Label(cause_search_frame, text="")
    defendant_new = ttk.Label(cause_search_frame, text="")
    court_new = ttk.Label(cause_search_frame, text="")
    opposing_counsel_new = ttk.Label(cause_search_frame, text="")
    judge_new = ttk.Label(cause_search_frame, text="")

    cause_new.grid(row=5, column=1, sticky="w", pady=5)
    plaintiff_new.grid(row=6, column=1, sticky="w", pady=5)
    defendant_new.grid(row=7, column=1, sticky="w", pady=5)
    court_new.grid(row=8, column=1, sticky="w", pady=5)
    opposing_counsel_new.grid(row=9, column=1, sticky="w", pady=5)
    judge_new.grid(row=10, column=1, sticky="w", pady=5)



def update_court_data():
    with open('case_data.json', 'r') as infile:
        retrieved_court_data = json.load(infile)

    for items in retrieved_court_data['_case_args']:
        cause_new.configure(text=items['_cause_number'])
        plaintiff_new.configure(text=items['_plaintiff'])
        defendant_new.configure(text=items['_defendant'])
        court_new.configure(text=items['_court_number'])
        opposing_counsel_new.configure(text=items['_opposing_counsel'])
        judge_new.configure(text=items['_judge'])

def create_widgets_in_third_frame():
    # Create the label for the frame
    # Sets font styles
    title_font = tkinter.font.Font(size=24, weight="bold")
    title_font_ul = tkinter.font.Font(size=14, weight="bold", underline=True)
    desc_font = tkinter.font.Font(size=12)

    # Create the label for the frame
    mm_title = ttk.Label(third_frame, text='Make a Motion', font=title_font, foreground="#000000")
    mm_title.grid(column=0, row=0, pady=10, padx=10, sticky="ew")
    mm_desc = ttk.Label(third_frame, text='Changes made here will modify information in the motion.',
                        font=desc_font)
    mm_desc.grid(column=0, row=1, pady=10, padx=10, sticky="ew")

    # Configures the labels
    mm_title.config(anchor="center")
    mm_desc.config(anchor="center")

    # Cause Number Search

    cause_search_label = ttk.Label(cause_search_frame, text="Cause Number:", font=desc_font,
                                   justify="center")
    cause_search_label.grid(row=2, column=0)
    cause_search_label.config(anchor="center")

    cause_desc = ttk.Label(cause_search_frame, text='(include dashes)')
    cause_desc.grid(row=3, column=1)

    global cause_entry

    cause_entry = ttk.Entry(cause_search_frame, width=30, font=desc_font)
    cause_entry.grid(row=2, column=1, ipady=2, pady=5, padx=5)

    cause_search_button = ttk.Button(cause_search_frame, text="Find", command=get_cause_search_entry)
    cause_search_button.grid(row=2, column=2, pady=10, padx=5)

    # Case Info Display

    case_info = ttk.Label(cause_search_frame, text="Case Information", font=title_font_ul, foreground="#000000")
    cause = ttk.Label(cause_search_frame, text="Cause Number:", font=desc_font)
    plaintiff = ttk.Label(cause_search_frame, text="Plaintiff:", font=desc_font)
    defendant = ttk.Label(cause_search_frame, text="Defendant:", font=desc_font)
    court = ttk.Label(cause_search_frame, text="Court:", font=desc_font)
    opposing_counsel = ttk.Label(cause_search_frame, text="Opposing Counsel:", font=desc_font)
    judge = ttk.Label(cause_search_frame, text="Judge:", font=desc_font)


    case_info.grid(row=4, column=0, pady=5)
    cause.grid(row=5, column=0, sticky="w", pady=5)
    plaintiff.grid(row=6, column=0, sticky="w", pady=5)
    defendant.grid(row=7, column=0, sticky="w", pady=5)
    court.grid(row=8, column=0, sticky="w", pady=5)
    opposing_counsel.grid(row=9, column=0, sticky="w", pady=5)
    judge.grid(row=10, column=0, sticky="w", pady=5)

    updated_case_info()
    update_court_data()

    # Motion Title

    motion_title = ttk.Label(cause_search_frame, text="Motion Title:", font=desc_font)
    motion_title.grid(row=15, column=0, pady=10)

    global motion_title_entry
    motion_title_entry = ttk.Entry(cause_search_frame, width=30, font=desc_font)
    motion_title_entry.grid(row=15, column=1, ipady=2, pady=10, padx=5)


    # Create the button for the frame
    third_window_back_button = ttk.Button(button_mm_frame, text="Back", command=call_first_frame_on_top)
    third_window_back_button.grid(column=0, row=20, pady=10, padx=75, sticky='n')

    save_as_button = ttk.Button(button_mm_frame, text="Save As", command=None)
    save_as_button.grid(column=1, row=20, pady=10, padx=75, sticky='n')

    third_window_quit_button = ttk.Button(button_mm_frame, text="Publish", command=combine_methods_to_publish)
    third_window_quit_button.grid(column=2, row=20, pady=10, padx=75, sticky='n')

def get_motion_title():
    motion_title_input = motion_title_entry.get()

    with open('motion_title.txt', 'w') as outfile:
        outfile.write(motion_title_input)

    messagebox.showinfo("Success", "Motion template created!")

def combine_methods_to_publish():
    get_motion_title()
    StateCourt.make_template()


#----------------------------------------------------------------------------#

# Hiding windows

def call_first_frame_on_top():
    # This function can be called only from the second window.
    # Hide the second window and show the first window.
    second_frame.grid_forget()
    third_frame.grid_forget()
    first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_second_frame_on_top():
    # This function can be called from the first and third windows.
    # Hide the first and third windows and show the second window.
    first_frame.grid_forget()
    third_frame.grid_forget()
    second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

def call_third_frame_on_top():
    # This function can only be called from the second window.
    # Hide the second window and show the third window.
    first_frame.grid_forget()
    third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))


#----------------------------------------------------------------------------#

# GUI Code

root = ThemedTk(theme="arc")
root.title("Magic Motion Maker")
root.columnconfigure(0, weight=1)
root.configure(bg="#f5f6f7")

# Define window size
window_width = 800
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Create frames inside the root window to hold other GUI elements.
# All frames must be created in the main program, otherwise they are not accessible in functions.

# Main Frame
first_frame = ttk.Frame(root, width=window_width, height=window_height)
first_frame.grid(column=0, row=0, padx=20, pady=5, sticky="ew")
first_frame.columnconfigure(0, weight=1)

# AP Frame
second_frame = ttk.Frame(root, width=window_width, height=window_height)
second_frame.grid(column=0, row=0, padx=20, pady=5, sticky="ew")
second_frame.columnconfigure(0, weight=1)


form_frame = ttk.Frame(second_frame, width=window_width, height=window_height)
form_frame.grid(column=0, row=2, padx=20, pady=5, sticky="n")
form_frame.columnconfigure(0, weight=1)

button_ap_frame = ttk.Frame(second_frame, width=window_width, height=window_height)
button_ap_frame.grid(column=0, row=3, padx=20, pady=5, sticky="n")
button_ap_frame.columnconfigure(0, weight=1)

# MM Frame
third_frame = ttk.Frame(root, width=window_width, height=window_height)
third_frame.grid(column=0, row=0, padx=20, pady=5, sticky="ew")
third_frame.columnconfigure(0, weight=1)

cause_search_frame = ttk.Frame(third_frame, width=window_width, height=window_height)
cause_search_frame.grid(column=0, row=2, padx=20, pady=5)
cause_search_frame.columnconfigure(0, weight=1)

button_mm_frame = ttk.Frame(third_frame, width=window_width, height=window_height)
button_mm_frame.grid(column=0, row=4, padx=20, pady=5, sticky="n")
button_mm_frame.columnconfigure(0, weight=1)



# Create all widgets to all frames
create_widgets_in_third_frame()
create_widgets_in_ap_frame()
create_widgets_in_welcome_frame()

# Hide all frames in reverse order, but leave first frame visible (unhidden).
third_frame.grid_forget()
second_frame.grid_forget()


root.mainloop()
