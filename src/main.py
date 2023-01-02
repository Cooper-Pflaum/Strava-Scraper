




from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD, Font

import scraper

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
        title = title_frame(root, self)
        self.frames[title_frame] = title
        title.grid(column=0, row=0)
        self.show_frame(title_frame)
        
        #Generates the side menu option for the user to select
        side_menu = side_menu_frame(root, self)
        self.frames[side_menu_frame] = side_menu
        side_menu.grid(column=0, row=1, sticky='ns')
        self.show_frame(side_menu_frame)
        
        #Generates the frame that handles all of the data-fields to start tracking a new club
        club_track = new_club_tracker_frame(root, self)
        self.frames[new_club_tracker_frame] = club_track
        club_track.grid(column=1,row=1, sticky='nsew')
        
        #Generates the frame that shows all of the available clubs to select from
        track_menu = club_menu_frame(root, self)
        self.frames[club_menu_frame] = track_menu
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
        
        track_menu = club_menu_frame(root, self)
        self.frames[club_menu_frame] = track_menu
        track_menu.grid(column=1,row=1, sticky='nsew')
        # self.show_frame(track_menu)
        
    def regen_current_club(self, cont, index):
        frame = self.frames[cont]
        frame.destroy()
        
        current_club = club_frame(root, self, index)
        self.frames[club_menu_frame] = current_club
        current_club.grid(column=1,row=1, sticky='nsew')



class title_frame(Frame):
    def __init__(self, parent, controller):
        #Initialize the frame
        Frame.__init__(self,parent)
        
        title = Label(parent, text=f'{app_title}', relief=RAISED, justify=CENTER, font=Font(self, size=20, weight=BOLD))
        title.grid(column=0, row=0, sticky='nesw', columnspan=2)



class side_menu_frame(Frame):
    def __init__(self, parent, controller):
        #Initialize the frame
        Frame.__init__(self,parent)
        Frame.configure(self, relief=RAISED, border=2)

        ttk.Button(self, 
                   text='New Club Tracker', 
                   command= lambda: [controller.show_frame(new_club_tracker_frame)], 
                   width=20).grid(column=0, row=0)
        ttk.Button(self, 
                   text='Open Club', 
                   command= lambda: [controller.regen_club_selector(club_menu_frame), controller.show_frame(club_menu_frame)], 
                   width=20).grid(column=0, row=1)
        ttk.Button(self, 
                   text='Settings', 
                   command= lambda: [controller.regen_club_selector(club_menu_frame), controller.show_frame(club_menu_frame)], 
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



class new_club_tracker_frame(Frame):
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



class club_menu_frame(Frame):
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
    data = []
    def __init__(self, parent, controller, index=None):
        #Initialize the frame
        Frame.__init__(self,parent)
        Frame.columnconfigure(self, 0, weight=0)
        Frame.columnconfigure(self, 1, weight=0)
        Frame.columnconfigure(self, 2, weight=0)
        Frame.columnconfigure(self, 3, weight=2)
        Frame.rowconfigure(self, 0, weight=0)
        Frame.rowconfigure(self, 1, weight=0)
        Frame.rowconfigure(self, 2, weight=1)
        

        #Pull data from tracked-clubs
        club_names = []
        club_ids = []
        with open('tracked-clubs.txt', 'r') as file:
            for line in file:
                club_names.append(line.strip().split(',')[1])
                club_ids.append(line.strip().split(',')[0])
                
        if(index != None):
            club_id = Label(self, text=f'{club_names[index]}', font=Font(self, size=20), relief=RAISED)
            club_id.grid(column=0, row=0, sticky='nesw', columnspan=5)
            
            ath = Label(self, text='Athlete', relief=RAISED, width=20)
            ath.grid(column=0, row=1, sticky='nesw')
            
            dist = Label(self, text='Distances', relief=RAISED, width=15)
            dist.grid(column=1, row=1, sticky='nesw')
            
            runs = Label(self, text='Runs', relief=RAISED, width=10)
            runs.grid(column=2, row=1, sticky='nesw')
            
            stats = Label(self, text='Club Stats', relief=RAISED, width=30)
            stats.grid(column=3, row=1, sticky='nesw')
            
            # l4 = Label(self, text='', relief=RAISED)
            # l4.grid(column=0, row=2, sticky='nesw')
            
            # l5 = Label(self, text='', relief=RAISED)
            # l5.grid(column=1, row=2, sticky='nesw')
            
                        
            # btn = ttk.Button(self, text='Generate report', command=self.scrape_data(club_ids[index])).grid(column=0,row=3,columnspan=3)
            data = scraper.get_club_distance(club_ids[index])   
            data = list(data)
               
            total_dist = data[3]
            
            del data[3]
            
            athletes = data[0]
            distances = data[1]
            total_runs = data[2]
            
            for i in range(len(athletes)):
                Frame.rowconfigure(self, i+2, weight=1)
                
                
                athLabel = Label(self, text=athletes[i].title(), relief=RAISED)
                athLabel.grid(column=0, row=i+2, sticky='nesw')
                
                distLabel = Label(self, text=f'{distances[i]}km', relief=RAISED)
                distLabel.grid(column=1, row=i+2, sticky='nesw')
                
                runLabel = Label(self, text=f'{total_runs[i]}', relief=RAISED)
                runLabel.grid(column=2 ,row=i+2, sticky='nesw')
                # print(i, athletes[i], distances[i])

            stats_label = Label(self, text=
f'''Total Distance:             {total_dist}km / {round(total_dist/1.609, 1)}mi
Total Runs:                 {sum(total_runs)}
========================================
Top Runner:                 {athletes[0]}
Distance:                   {distances[0]}km / {round(distances[0]/1.609, 1)}mi
Runs:                       {total_runs[0]}
========================================
                       ''', anchor='nw', justify=LEFT)
            
            stats_label.grid(column=3, row=2, sticky='nesw', rowspan=2+int(len(athletes)/4))

            
            # selected_runner = Label(self, text='Selected Athlete', relief=RAISED).grid(column=3, row=2+int(len(athletes)/4)+1, sticky='nesw')
app = PageContainer()
app.mainloop()

