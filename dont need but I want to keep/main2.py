from tkinter import *
from tkinter import TclError, ttk
from tkinter.font import BOLD, Font

from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    root.title(f"Simple Text Editor - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", END)
        output_file.write(text)
    root.title(f"Simple Text Editor - {filepath}")
   
def load_club_id(container):
    input_frame = club_input(container)
    input_frame.grid(column=1, row=1, sticky='nesw')








def side_buttons(container):
   frame = ttk.Frame(container, relief=RAISED, border=2)

   frame.columnconfigure(0, weight=1)
   
   ttk.Button(frame, text='Open', command=open_file).grid(column=0, row=0)
   ttk.Button(frame, text='Save As...', command=save_file).grid(column=0, row=1)
   ttk.Button(frame, text='Generate From ID', command=load_club_id(container)).grid(column=0, row=2)
#  ttk.Button(frame, text='Cancel').grid(column=0, row=3)

   for widget in frame.winfo_children():
      widget.grid(padx=5, pady=5, sticky='ns')

   return frame





def hide_button(widget):
    # This will remove the widget from toplevel
    widget.pack_forget()
  
  
# Method to make Button(widget) visible
def show_button(widget):
    # This will recover the widget from toplevel
    widget.pack()
    
    
    
def club_input(container): 
   frame = ttk.Frame(container)

   # grid layout for the input frame
   frame.columnconfigure(1, weight=0)
   
   stick = 'nw'
   # Find what
   ttk.Label(frame, text='Find Club:').grid(column=0, row=0, sticky=stick)
   keyword = ttk.Entry(frame, width=30)
   keyword.focus()
   keyword.grid(column=1, row=0, sticky=stick)

   for widget in frame.winfo_children():
      widget.grid(padx=5, pady=5)

   return frame

def help_screen(container):
    frame = ttk.Frame(container)
    ttk.Label(frame, text='Welcome to Strava Scraper!',font=Font(container, size=25, weight=BOLD)).grid(column=0,row=0)
    
    
    return frame




def create_main_window():
    root = Tk()
    root.title('Strava Scraper')
    root.geometry('800x1000')
    

   #  root.resizable(0, 0)
    try:
        # windows only (remove the minimize/maximize button)
        root.attributes('-toolwindow', True)
    except TclError:
        print('Not supported on your platform')


    title = Label(root, text='Strava Scraper', relief=RAISED, justify=CENTER, font=Font(root, size=15, weight=BOLD))
    title.grid(column=0, row=0, sticky='nesw', columnspan=2)

    # layout on the root window
    root.rowconfigure(0, weight=0)
    root.rowconfigure(1, weight=1)
    # root.rowconfigure(1, weight=0)
    root.columnconfigure(1, weight=4)
    

    button_frame = side_buttons(root)
    button_frame.grid(column=0, row=1, sticky='ns')
    
    help_screen_frame = help_screen(root)
    help_screen_frame.grid(column=1,row=1)
    
    
    root.mainloop()

create_main_window()

# root.mainloop()