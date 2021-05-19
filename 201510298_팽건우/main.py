# code for Quick Sort Visualizer 
# using Python and Tkinter
# import modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import random
import copy
from quick import quick_sort
from merge import merge_sort
from bubble import bubble_sort
from selection import selection_sort
from insertion import insertion_sort

# initialising root class for Tkinter
root = Tk()
root.title("Quick Sort Visualizer")
  
# maximum window size
root.maxsize(1080, 720)
root.config(bg="Black")
  
select_alg = StringVar()
data = []
numbers = []
result = ""

def find_file():
	global data, numbers

	input_path = filedialog.askopenfilename(initialdir='/', title='select a file',
										filetypes=(("txt files","*.txt"),("all files","*.*")))
	input_file = open(input_path, "r", encoding='UTF-8')
	num_str = input_file.read().splitlines()
	for num in num_str:
		numbers.append(int(num))
	data = copy.deepcopy(numbers)
	input_file.close()

def save_file():
	output_file = open('output.txt', "w", encoding='UTF-8')
	output_file.write(result)
	output_file.close()

# function to generate the data values 
# by accepting a given range
def generate():
	global data

	sizeval = int(sizeEntry.get())
	drawData(data, ['Red' for x in range(len(data))])
  
# funtion to create the data bars 
# by creating a canvas in Tkinter
def drawData(data, colorlist):
	canvas.delete("all")
	can_height = 380
	can_width = 550
	x_width = can_width/(len(data) + 1)
	offset = 30
	spacing = 10
	# normalizing data for rescaling real-valued 
	# numeric data within the
	# given range
	normalized_data = [i / max(data) for i in data]
  
	for i, height in enumerate(normalized_data):
		# top left corner
		x0 = i*x_width + offset + spacing
		y0 = can_height - height*340
  
		# bottom right corner
		x1 = ((i+1)*x_width) + offset
		y1 = can_height
  
		# data bars are generated as Red 
		# colored vertical rectangles
		canvas.create_rectangle(x0, y0, x1, y1, 
								fill=colorlist[i])
		canvas.create_text(x0+2, y0, anchor=SE, 
						   text=str(data[i]))
	root.update_idletasks()

# function to initiate the sorting 
# process by calling the extension code
def start_algorithm():
	global data, result, numbers
	
	if not data:
		return

	if (algmenu.get() == 'Selection Sort'):
		selection_sort(data, drawData)
		result = ' '.join(map(str, data))
		data = copy.deepcopy(numbers)

	if (algmenu.get() == 'Insertion Sort'):
		insertion_sort(data, drawData)
		result = ' '.join(map(str, data))
		data = copy.deepcopy(numbers)

	if (algmenu.get() == 'Bubble Sort'):
		bubble_sort(data, drawData)
		result = ' '.join(map(str, data))
		data = copy.deepcopy(numbers)

	if (algmenu.get() == 'Quick Sort'):
		quick_sort(data, 0, len(data)-1, drawData)
		drawData(data, ['Green' for x in range(len(data))])
		result = ' '.join(map(str, data))
		data = copy.deepcopy(numbers)

	if (algmenu.get() == 'Merge Sort'):
		merge_sort(data, drawData)
		drawData(data, ['Green' for x in range(len(data))])
		result = ' '.join(map(str, data))
		data = copy.deepcopy(numbers)

# creating main user interface frame
# and basic layout by creating a frame
Mainframe = Frame(root, width=600, height=200, bg="Grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)
  
canvas = Canvas(root, width=600, height=380, bg="Grey")
canvas.grid(row=1, column=0, padx=10, pady=5)
  
# creating user interface area in grid manner
# first row components
Label(Mainframe, text="201510298 팽건우", 
	  bg='Grey').grid(row=0, column=0, 
					  padx=5, pady=5, 
					  sticky=W)

# algorithm menu for showing the 
# name of the sorting algorithm
algmenu = ttk.Combobox(Mainframe, 
					   textvariable=select_alg, 
					   values=["Selection Sort","Insertion Sort","Bubble Sort", "Quick Sort", "Merge Sort", ])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)
  
# creating Start Button to start 
# the sorting visualization process
Button(Mainframe, text="Sort START", 
	   bg="Blue", 
	   command=start_algorithm).grid(row=1, 
									 column=3, 
									 padx=5, 
									 pady=5)
  
# creating Speed Bar using scale in Tkinter
# speedbar = Scale(Mainframe, from_=0.10, 
#                  to=2.0, length=100, digits=2,
#                  resolution=0.2, orient=HORIZONTAL, 
#                  label="Select Speed")
# speedbar.grid(row=0, column=2, 
#               padx=5, pady=5)
  
# second row components
# sizeEntry : scale to select 
# the size/number of data bars
sizeEntry = Scale(Mainframe, from_=3, 
				  to=60, resolution=1,
				  orient=HORIZONTAL, 
				  label="Size")
sizeEntry.grid(row=1, column=0, 
			   padx=5, pady=5)
  
# minEntry : scale to select the 
# minimum value of data bars
# minEntry = Scale(Mainframe, from_=0, 
#                  to=10, resolution=1,
#                  orient=HORIZONTAL, 
#                  label="Minimun Value")
# minEntry.grid(row=1, column=1, 
#               padx=5, pady=5)

# input file 
input_file = Button(Mainframe, text="find input file", 
					command=find_file).grid(row=1,
											column=1, 
											padx=5,
											pady=5)

# maxEntry : scale to select the 
# maximum value of data bars
# maxEntry = Scale(Mainframe, from_=10, 
# 				 to=100, resolution=1,
# 				 orient=HORIZONTAL, 
# 				 label="Maximun Value")
# maxEntry.grid(row=1, column=2, 
# 			  padx=5, pady=5)

output_file = Button(Mainframe, text="Save result file", 
					command=save_file).grid(row=1,
											column=2,
											padx=5,
											pady=5)

# creating generate button
Button(Mainframe, text="Make bar", 
	   bg="Red", 
	   command=generate).grid(row=0, 
							  column=3, 
							  padx=5, 
							  pady=5)



# to stop automatic window termination
root.mainloop()