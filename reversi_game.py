from Tkinter import *

class Page1():
	def __init__(self, master):
		self.frame=Frame(master, width=880, height=480, bg='black')
		#self.master=master
		self.frame.pack()
		#frame.wm_title('Reversi Game')
		#self._frame=Frame()
		self.create_canvas()
		self.create_colorButton()
		
	def create_canvas(self):
		#splitting the screen into three sections: left, middle and right parts
		#left part of canvas => player 1
		#middle part of canvas => game board display
		#right part of canvas => player 2

		print "Entering create_canvas()..."
		
		self.canvas_left=Canvas(self.frame, width=200, height=480, bg='firebrick3')
		self.canvas_left.pack(side=LEFT) #packing the left part of canvas created into Page1
		self.canvas_middle=Canvas(self.frame, width=480, height=480, bg='green')
		self.canvas_middle.pack(side=LEFT) #packing the middle part of canvas created into Page1
		self.create_grid()		
		self.canvas_right=Canvas(self.frame, width=200, height=480, bg='firebrick3')
		self.canvas_right.pack(side=LEFT) #packing the right part of canvas created into Page1

		#creating 'PLAYER 1' label on left canvas of Page1
		widget_player1 = Label(self.canvas_left, text='PLAYER 1', font='TIMES 20',fg='black', bg='firebrick3')
		widget_player1.pack()
		self.canvas_left.create_window(100, 50, window=widget_player1)

		#creating 'PLAYER 2' label on right canvas of Page1
		widget_player2 = Label(self.canvas_right, text='PLAYER 2', font='TIMES 20',fg='black', bg='firebrick3')
		widget_player2.pack()
		self.canvas_right.create_window(100, 50, window=widget_player2)

	def create_grid(self):
		#create grid in the middle canvas of page 1
		print "Entering create_grid()..."
		self.rows = 8
        	self.columns = 8
        	self.cellwidth = 60
        	self.cellheight = 60

        	self.rect = {}

		for column in range(8):
            		for row in range(8):
				print "Entering create_grid looping..."
				x1 = column*self.cellwidth
        			y1 = row * self.cellheight
				x2 = x1 + self.cellwidth
				y2 = y1 + self.cellheight
                		self.rect[row,column] = square_in_grid(self.canvas_middle, x1, y1, x2, y2)
				print "Updating loop..."
                		
	def create_colorButton(self):
		#setting default color buttons for players on left and right canvases of Page1
		print "Entering create_colorButton DEFAULT..."
		self.canvas_left.create_oval(75, 125, 125, 175, width=1, fill='firebrick3',outline='black')
		self.canvas_left.pack()
		self.canvas_right.create_oval(75, 125, 125, 175, width=1, fill='firebrick3', outline='black')
        	self.canvas_right.pack()
		
		self.choose_color()
	
	def choose_color(self):
		#setting colors for players based on player 1's decision 
		#Player 1 decides his color by clicking on any color button in pop-up window (Page2)
		#Player 2 is assigned the remaining color by default

		print "Entering choose_color..."
		self.master2=Toplevel(self.frame)
		#self.master2.lower(belowThis=self.master)
		self.master2.title('Choose a Color')
		print "Entering Page2..."
		
		self.canvas_top2=Canvas(self.master2, width=400, height=50, bg='firebrick3')
		self.canvas_top2.pack(side=TOP, fill=BOTH, expand=TRUE) #packing the top part of canvas created into page2
		self.label1=Label(self.canvas_top2, text='PLAYER 1 CHOOSE YOUR COLOR', font='TIMES 15',fg='black', bg='firebrick3')
		self.label1.pack(fill=BOTH, expand=TRUE)
		
		self.canvas_left2=Canvas(self.master2, width=200, height=150, bg='firebrick3')
		self.canvas_left2.pack(side=LEFT, fill=BOTH, expand=TRUE) #packing the left part of canvas created into page2
		self.canvas_left2.create_oval(75, 25, 125, 75, fill="white", outline='black')
		button1=Button(self.canvas_left2, text='W', font='TIMES 20',fg='black', bg='firebrick3', command=self.white_button)
		button1.pack(fill=BOTH)
		self.canvas_left2.create_window(100, 120, window=button1)
				
		self.canvas_right2=Canvas(self.master2, width=200, height=150, bg='firebrick3')
		self.canvas_right2.pack(side=LEFT, fill=BOTH, expand=TRUE) #packing the right part of canvas created into page2
		self.canvas_right2.create_oval(75, 25, 125, 75, fill="black", outline='black')
		button2=Button(self.canvas_right2, text='B', font='TIMES 20',fg='black', bg='firebrick3', command=self.black_button)
		button2.pack(fill=BOTH)
		self.canvas_right2.create_window(100, 120, window=button2)
		
	def white_button(self):
		#setting player1 => white, player2 => black on Page1
		print 'Entering create_colorButton P1 WHITE...'
		self.master2.destroy()
		self.canvas_left.create_oval(75, 125, 125, 175, width=1, fill='white',outline='black')
		self.canvas_left.pack()
		self.canvas_right.create_oval(75, 125, 125, 175, width=1, fill='black', outline='black')
        	self.canvas_right.pack()
		self.player_turn()

	def black_button(self):
		#setting player1 => black, player2 => white on Page1
		print 'Entering create_colorButton P1 BLACK...'
		self.master2.destroy()
		self.canvas_left.create_oval(75, 125, 125, 175, width=1, fill='black',outline='black')
		self.canvas_left.pack()
		self.canvas_right.create_oval(75, 125, 125, 175, width=1, fill='white', outline='black')
        	self.canvas_right.pack()
		self.player_turn()

	def player_turn(self):
		#creating 'YOUR TURN' label that indicates which player has to play currently on Page1
		print "Entering player_turn()..."
 		widget_yourTurn = Label(self.canvas_left, text='YOUR TURN', font='TIMES 20', fg='black', bg='firebrick3')
		widget_yourTurn.pack()
		self.canvas_left.create_window(100, 300, window=widget_yourTurn)
		self.score()

	def score(self):
		#scoreboard that updates scores of both players on Page1
		piece=0
		print "Entering score()..."
		widget_score1 = Label(self.canvas_left, text='SCORE: 0', font='TIMES 20', fg='black', bg='firebrick3')
		widget_score1.pack()
		self.canvas_left.create_window(100, 420, window=widget_score1)

		widget_score2 = Label(self.canvas_right, text='SCORE: 0', font='TIMES 20', fg='black', bg='firebrick3')
		widget_score2.pack()
		self.canvas_right.create_window(100, 420, window=widget_score2)

		movable_piece(self.canvas_middle)
		print "movable piece is created..."

class square_in_grid():
	#class for each square in the grid
	def __init__(self,canvas_middle,x1,y1,x2,y2):
		print "Entering class square_in_grid..."
		#self.master=master
		self.canvas_middle=canvas_middle
		self.x1=x1
		self.x2=x2
		self.y1=y1
		self.y2=y2
		self.create_square()

	def create_square(self):
		print "Creating square..."
		self.canvas_middle.create_rectangle(self.x1,self.y1, self.x2, self.y2, fill="green", tags="rect")

class movable_piece():
	#class for movable piece
        def __init__(self, canvas_middle):
		print "Entering movable_piece class..."
            	self.canvas_middle=canvas_middle
		self.radius = 25 #circle/piece is 50x50
		self.centre_x = 270
		self.centre_y = 210
		self.create_movable_piece()
	
	def create_movable_piece(self):
		print "Entering create_movable_piece()..."
          	self.canvas_middle.create_oval(self.centre_x - self.radius, self.centre_y - self.radius,
                                    self.centre_x + self.radius, self.centre_y + self.radius, fill="green", tags = "circle")
            	#self.master.bind('<Configure>', self.resize)
            	#self.canvas.bind('<Button-1>', self.getWords)
            	self.canvas_middle.bind('<Up>', self.moveCircle)
            	self.canvas_middle.bind('<Down>', self.moveCircle)
            	self.canvas_middle.bind('<Left>', self.moveCircle)
            	self.canvas_middle.bind('<Right>', self.moveCircle)
		self.canvas_middle.bind('<space>', self.moveCircle)
            	self.canvas_middle.focus_set()

#        def resize(self, event):
#            self.canvas.configure(width = event.width-4, height = event.height-4)


	def moveCircle(self, event):
		print "Entering moveCricle()..."
		self.x=0
		self.y=0
            	"""move circle up, down, left or right when user clicks an arrow key"""
		if self.y >= 0 and self.y <= 480 and self.x >= 0 and self.x <= 480:
           		if event.keysym == "Up":
                		self.y = -60
				#print self.centre_y
				self.centre_y -= 60
				print "Moving Up..."
            		elif event.keysym == "Down":
                		self.y = 60
				self.centre_y += 60
				print "Moving Down..."
            		elif event.keysym == "Left":
                		self.x = -60
				self.centre_x -= 60
				print "Moving Left..."
            		elif event.keysym == "Right":
                		self.x = 60
				self.centre_x += 60
				print "Moving Right..."
			elif event.keysym == "space":
				print "space bar pressed..."
				fixed_piece(self.canvas_middle,self.radius,self.centre_x,self.centre_y)
			self.canvas_middle.move("circle", self.x, self.y)
	            	self.canvas_middle.update()
		
		else:
			print "Out of canvas bound..."
            	

class fixed_piece():
	#class for fixed piece
	def __init__(self,canvas_middle, radius, centre_x, centre_y):
		print "Entering fixed_piece class..."
            	self.canvas_middle=canvas_middle
		self.radius = radius #circle/piece is 50x50
		self.centre_x = centre_x
		self.centre_y = centre_y
		self.create_fixed_piece()
	
	def create_fixed_piece(self):
		print "creating fixed piece..."
		self.canvas_middle.create_oval(self.centre_x - self.radius, self.centre_y - self.radius,
                                   self.centre_x + self.radius, self.centre_y + self.radius, fill='black',outline='black')
		#self.canvas_middle.pack()

def main():
	root=Tk()
	myGUIPage1=Page1(root)
	root.lift(aboveThis=None)
	#myGUIPage1.master.configure(background='black')
	root.mainloop()

if __name__ == '__main__':
	main()
