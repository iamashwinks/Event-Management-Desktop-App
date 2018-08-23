import tkinter as tk
import csv

class EventManagement(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		container = tk.Frame(self)
		container.grid()

		self.frames = {}
		for F in (Menu_page, Event_page, Add_participants_page, See_participants_page):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("Menu_page")
		self.geometry("390x300+10+10")
		self.title("Event Management App")
		

	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()


class Menu_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Menu")
		label.grid(row=0, column=0, pady=10)

		button1 = tk.Button(self, text="Add Event",
							command=lambda: controller.show_frame("Event_page"))
		button2 = tk.Button(self, text="Add Participants",
							command=lambda: controller.show_frame("Add_participants_page"))
		button3 = tk.Button(self, text="See Participants",
							command=lambda: controller.show_frame("See_participants_page"))
		button1.grid(row=1, column=0, pady=2)
		button2.grid(row=2, column=0, pady=2)
		button3.grid(row=3, column=0, pady=2)

class Event_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.label = tk.Label(self, text="Add Events")
		self.label.grid(row = 0, column = 1, pady=10)
		self.event = tk.Label(self, text = "Enter event name : ")
		self.desc = tk.Label(self, text = "Enter amount : ")
		self.entry1 = tk.Entry(self, width = 40)
		self.entry2 = tk.Entry(self, width = 40)
		self.addbutton = tk.Button(self, text="Add Event", command= self.add_event)
		self.menubutton = tk.Button(self, text="Go to the Menu Page",
						   command=lambda: controller.show_frame("Menu_page"))
		self.event.grid(row=1, column=0, pady=2)
		self.desc.grid(row=2, column=0, pady=2)
		self.entry1.grid(row=1, column=1, pady=2)
		self.entry2.grid(row=2, column=1, pady=2)
		self.addbutton.grid(row = 3 , column = 1, sticky="NSEW", padx=5, pady=10)
		self.menubutton.grid(row = 5 , column = 1, sticky="NSEW", padx=5, pady=10)

	def add_event(self):
		self.val1 = self.entry1.get()
		self.val2 = self.entry2.get()
		with open('events.csv', 'a', newline="") as f:
			self.wr = csv.writer(f, dialect='excel')
			self.wr.writerow([self.val1,self.val2])
		self.added = tk.Label(self, text = "Event Added!")
		self.added.grid(row = 4 , column = 1,pady = 5)

class Add_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.label = tk.Label(self, text="Add Participants")
		self.label.grid(row = 0, column = 1, pady=10)
		self.menubutton = tk.Button(self, text="Go to the Menu Page",
						   command=lambda: controller.show_frame("Menu_page"))
		self.name = tk.Label(self, text = "Enter your name : ")
		self.college = tk.Label(self, text = "Enter your college : ")
		self.select_event = tk.Label(self, text = "Select the event : ")
		self.entry1_1 = tk.Entry(self, width = 40)
		self.entry1_2 = tk.Entry(self, width = 40)
		
		self.var = tk.StringVar(self)
		L = []
		with open('events.csv', 'r') as f:
			rd = csv.reader(f)
			for row in rd:
				ev = row[0]
				L.append(ev)
			#print(L)
			self.var.set(L[0])
		
		option = tk.OptionMenu(self, self.var, *L)
		option.grid(row = 3 , column = 1)
		self.addparticipant = tk.Button(self, text="Add Participant", command= self.add_participant)

		self.name.grid(row=1, column=0, pady=2)
		self.college.grid(row=2, column=0, pady=2)
		self.entry1_1.grid(row=1, column=1, pady=2)
		self.entry1_2.grid(row=2, column=1, pady=2)
		self.select_event.grid(row = 3 , column = 0, pady=2)
		self.addparticipant.grid(row = 4 , column = 1, sticky="NSEW", padx=5, pady=10)
		self.menubutton.grid(row = 6 , column = 1, sticky="NSEW", padx=5, pady=10)

	def add_participant(self):
		self.v1 = self.entry1_1.get()
		self.v2 = self.entry1_2.get()
		self.v3 = self.var.get()
		with open('participants.csv', 'a', newline="") as f:
			self.wr = csv.writer(f, dialect='excel')
			self.wr.writerow([self.v1,self.v2, self.v3])
		self.added = tk.Label(self, text = "Participant Added!")
		self.added.grid(row = 5 , column = 1,pady = 5)

class See_participants_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.label = tk.Label(self, text="Participants Details")
		self.label.grid(row = 0, column = 1, pady=4)
		self.seeparticipant = tk.Button(self, text="View All Participants", command= self.view_participant)
		self.tb1 = tk.Text(self, width=45, height=10)
		self.menubutton = tk.Button(self, text="Go to the Menu Page",
						   command=lambda: controller.show_frame("Menu_page"))
		self.seeparticipant.grid(row = 1 , sticky="NSEW", padx=5, pady=10)
		self.tb1.grid( row=2, column=0, columnspan=2, sticky="NSEW", padx=5, pady=10)
		self.menubutton.grid(row = 3 , column = 1, sticky="NSEW", padx=5, pady=10)

	def view_participant(self):
		P = []
		E = []
		with open('participants.csv', 'r') as f:
			rd = csv.reader(f)
			for row in rd:
				pt = row[0]
				ev = row[2]
				P.append(pt)
				E.append(ev)
			self.tb1.insert('0.0', str(P) + '\n')
			self.tb1.insert('0.0', str(E) + '\n')

app = EventManagement()
app.mainloop()