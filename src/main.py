from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD, Font

app_title = 'Strava Scraper'

def options():
    print ('''\n
**************************************************************
    Welcome to the GUI interface of the python program
**************************************************************''')



class PageContainer(Tk):  
    def __init__(self, *args, **kwargs):  
        # options()
        Tk.__init__(self, *args, **kwargs)

        Tk.geometry(self,'800x1000')  

        global root
        root = Frame(self)  
        root.pack(side='top', fill='both', expand = True )     

        self.frames = {}
    
      
      
        # layout on the root window
        root.rowconfigure(0, weight=0)
        root.rowconfigure(1, weight=1)
        root.columnconfigure(0, weight=0)      
        root.columnconfigure(1, weight=1)      
      
        #Generates the top title bar at the top of the window
        title_frame = title(root, self)
        self.frames[title] = title_frame
        title_frame.grid(column=0, row=0)
        self.show_frame(title)
        
        #Generates the side menu option for the user to select
        side_menu_frame = side_menu(root, self)
        self.frames[side_menu] = side_menu_frame
        side_menu_frame.grid(column=0, row=1, sticky='ns')
        self.show_frame(side_menu)
        
        #Generates the frame that handles all of the data-fields to start tracking a new club
        club_track = new_club_tracker(root, self)
        self.frames[new_club_tracker] = club_track
        club_track.grid(column=1,row=1, sticky='nsew')
        
        #Generates the frame that shows all of the available clubs to select from
        track_menu = club_menu(root, self)
        self.frames[club_menu] = track_menu
        track_menu.grid(column=1,row=1, sticky='nsew')
        
        
        saver = saving(root ,self)
        self.frames[saving] = saver
        saver.grid(column=1,row=1, sticky='nsew')
        
        #This is the frame that shows each club specifically. Only one club at a time
        current_club = club_frame(root,self, None)
        self.frames[club_frame] = current_club
        current_club.grid(column=1,row=1, sticky='nsew')
        
        settings = settings_frame(root,self)
        self.frames[settings_frame] = settings
        settings.grid(column=1,row=1, sticky='nsew')
        
        help_frame = start_help_frame(root,self)
        self.frames[start_help_frame] = help_frame
        help_frame.grid(column=1,row=1, sticky='nsew')
        self.show_frame(start_help_frame)
        
        
        
        
        

        
        
    def show_frame(self, cont):

        frame = self.frames[cont]    
        frame.tkraise()    
        
    def regen_club_selector(self, cont):
        frame = self.frames[cont]
        frame.destroy()
        
        track_menu = club_menu(root, self)
        self.frames[club_menu] = track_menu
        track_menu.grid(column=1,row=1, sticky='nsew')
        # self.show_frame(track_menu)
        
    def regen_current_club(self, cont, index):
        frame = self.frames[cont]
        frame.destroy()
        
        current_club = club_frame(root, self, index)
        self.frames[club_menu] = current_club
        current_club.grid(column=1,row=1, sticky='nsew')



class title(Frame):
    def __init__(self, parent, controller):
        #Initialize the frame
        Frame.__init__(self,parent)
        
        title = Label(parent, text=f'{app_title}', relief=RAISED, justify=CENTER, font=Font(self, size=20, weight=BOLD))
        title.grid(column=0, row=0, sticky='nesw', columnspan=2)



class side_menu(Frame):
    def __init__(self, parent, controller):
        #Initialize the frame
        Frame.__init__(self,parent)
        Frame.configure(self, relief=RAISED, border=2)

        ttk.Button(self, 
                   text='New Club Tracker', 
                   command= lambda: [controller.show_frame(new_club_tracker)], 
                   width=20).grid(column=0, row=0)
        ttk.Button(self, 
                   text='Open Club', 
                   command= lambda: [controller.regen_club_selector(club_menu), controller.show_frame(club_menu)], 
                   width=20).grid(column=0, row=1)
        ttk.Button(self, 
                   text='Settings', 
                   command= lambda: [controller.regen_club_selector(club_menu), controller.show_frame(club_menu)], 
                   width=20).grid(column=0, row=2)

        
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=2)



class settings_frame(Frame):
    def __init__(self, parent, controller):
            #Initialize the frame
            Frame.__init__(self,parent)


       
class start_help_frame(Frame):
    def __init__(self, parent, controller):
        #Initialize the frame
        Frame.__init__(self,parent)
        Frame.columnconfigure(self, 0, weight=1)
        Frame.rowconfigure(self, 0, weight=1)
        Frame.rowconfigure(self, 1, weight=1)
        Frame.rowconfigure(self, 2, weight=1)
        
        title = Label(self, text=f'Welcome to {app_title}', justify=CENTER, font=Font(self, size=20, weight=BOLD))
        title.grid(column=0, row=0, sticky='nsew')
        description1 = Label(self, 
                             text='''
This is an app created by Cooper Pflaum
For the purpose of scraping Strava Clubs
To make my XC Coaches lives easier

Please use responsibly
I am not liable for any legal issues or account lockouts

Enjoy!
''', 
                             justify=CENTER, font=Font(self, size=15))
        description1.grid(column=0, row=1, sticky='nsew')



class saving(Frame):
    def __init__(self, parent, controller):
        #Initialize the frame
        Frame.__init__(self,parent)

        interaction_page = Label(self, text='Save to:')
        interaction_page.grid(column=0, row=0,)
        
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=0, sticky='ew')



class new_club_tracker(Frame):
    def __init__(self, parent, controller):
        #Initialize the frame
        Frame.__init__(self,parent)
        Frame.rowconfigure(self, 0, weight=0)
        Frame.rowconfigure(self, 1, weight=0)
        Frame.rowconfigure(self, 2, weight=1)
        Frame.rowconfigure(self, 3, weight=2)
        Frame.rowconfigure(self, 4, weight=2)
        Frame.columnconfigure(self, 0, weight=0)
        Frame.columnconfigure(self, 1, weight=0)
        Frame.columnconfigure(self, 2, weight=1)

        
        
        
        club_id = Label(self, text='Club ID:', font=Font(self, size=10))
        club_id.grid(column=0, row=0, sticky='nw')
        
        club_id_input = Entry(self, width=30)
        club_id_input.focus()
        club_id_input.grid(column=1, row=0, sticky='nw')



        club_name = Label(self, text='Club Name:', font=Font(self, size=10))
        club_name.grid(column=0, row=1, sticky='nw')
        
        club_name_input = Entry(self, width=30)
        club_name_input.focus()
        club_name_input.grid(column=1, row=1, sticky='nw')
        
        
        
        def submit():
            with open('tracked-clubs.txt', 'a') as target_file:
                target_file.write(f"{club_id_input.get()},{club_name_input.get()}")
                target_file.write("\n")
        ttk.Button(self, 
                   text='Start Tracking', 
                   width=20,
                   command=submit
                   ).grid(column=0, row=2, sticky='nsew', columnspan=3)
        
        for widget in self.winfo_children():
            widget.grid(padx=5, pady=2)



class club_menu(Frame):
    def __init__(self, parent, controller):
        #Initialize the frame
        Frame.__init__(self,parent)
        Frame.columnconfigure(self,0,weight=1)


        #Open the club file and read from the list for name and ID's of clubs
        club_names = []
        with open('tracked-clubs.txt', 'r') as file:
            for line in file:
                club_names.append(line.strip().split(',')[1])


        #create a list of buttons to navigate the clubs
        ClubButtonList = []
        
        
        #Add buttons according to the amount of clubs. Once there is 10 clubs, it starts a new column for them
        col = 0
        row = 0
        for i, c in enumerate(club_names):
            Frame.rowconfigure(self, row, weight=1)
            if(row == 10):
                col += 1
                Frame.columnconfigure(self,col,weight=1)
                row = 0
            ClubButtonList.append(ttk.Button(self, text=club_names[i], width=40, command= lambda c = i: [controller.regen_current_club(club_frame, c)]))
            ClubButtonList[i].grid(column=col, row=row, sticky='nsew', pady=10, padx=20)
            row+=1



class club_frame(Frame):
    def __init__(self, parent, controller, index=None):
        #Initialize the frame
        Frame.__init__(self,parent)
        Frame.columnconfigure(self, 0, weight=1)
        Frame.rowconfigure(self, 0, weight=0)
        Frame.rowconfigure(self, 1, weight=1)
        

        #Pull data from tracked-clubs
        club_names = []
        with open('tracked-clubs.txt', 'r') as file:
            for line in file:
                club_names.append(line.strip().split(',')[1])
                
        if(index != None):
            club_id = Label(self, text=f'Club Name: {club_names[index]}', font=Font(self, size=20), relief=SOLID)
            club_id.grid(column=0, row=0, sticky='nesw')



app = PageContainer()
app.mainloop()

