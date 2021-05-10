import copy
import algorithms
import time
import os
import sys
import pygame as pg
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from tkinter import filedialog

class Sort_Gui:
	def __init__(self, window):
		self.window = window
		self.sort_var = tk.IntVar()

		sort_label = tk.Label(window, 
						text="정렬방식:",
						font = ("Arial", "25", "italic")).grid(row=0, column=0)

		file_label = tk.Label(window, 
				text="파일 입력: ",
				font = ("Arial", "25", "italic")).grid(row=20,column=0)

		selection_sort = tk.Radiobutton(window, text='선택 정렬', variable=self.sort_var, value=1, command=self.sort_select, font = ("Arial", "20", "italic")).grid(row=0, column=6)
		bubble_sort = tk.Radiobutton(window, text='버블 정렬', variable=self.sort_var, value=2, command=self.sort_select, font = ("Arial", "20", "italic")).grid(row=0, column=12)
		insert_sort = tk.Radiobutton(window, text='삽입 정렬', variable=self.sort_var, value=3, command=self.sort_select, font = ("Arial", "20", "italic")).grid(row=0, column=18)
		merge_sort = tk.Radiobutton(window, text='병합 정렬', variable=self.sort_var, value=4, command=self.sort_select, font = ("Arial", "20", "italic")).grid(row=0, column=24)
		quick_sort = tk.Radiobutton(window, text='퀵 정렬', variable=self.sort_var, value=5, command=self.sort_select, font = ("Arial", "20", "italic")).grid(row=0, column=30)

		self.sort_show = tk.Label(window)
		self.sort_show.grid(row=10, column=5)
	
		input_button = tk.Button(window, text="find input file", width=20, command=self.find_file).grid(row=20, column=12)
		output_button = tk.Button(window, text="save result", width=20, command=self.save_file).grid(row=20, column=18)
		# play_button = tk.Button(window, text="play sort", width=20, command=self.play_sort).grid(row=30, column=12)
		window.update()
        
		self.dimensions = (800, 600)
		# List all the algorithms available in the project in dictionary and call the
		#  necessary functions from algorithms.py
		self.algorithms = {"SelectionSort": algorithms.SelectionSort(), "BubbleSort": algorithms.BubbleSort(), "InsertionSort": algorithms.InsertionSort(), "MergeSort": algorithms.MergeSort(), "QuickSort": algorithms.QuickSort()}

		# Set the dimensions of the window and display it
		self.display = pg.display.set_mode(self.dimensions)
		# Fill the window with purple hue
		self.display.fill(pg.Color("#a48be0"))

		self.algorithm = self.algorithms['BubbleSort'] # Collect algorithm
        _, time_elapsed = self.algorithm.run() # Run algorithm and time it
        # keep_open(self.algorithm, self.display, time_elapsed) # Display results

	# def sort_select(self):
	# 	self.sort_num = self.sort_var.get()
	# 	if (self.sort_num == 1):
	# 		# print(self.selection_sort(self.numbers))
	# 		self.result = "선택 정렬\n" + ' '.join(map(str,self.numbers))
	# 		self.numbers = copy.deepcopy(self.nums)
	# 		self.sort_show.config(text="선택 정렬")
	# 		Selection_sort(self.numbers, master=None)
	# 	elif (self.sort_num == 2):
	# 		# print(self.bubble_sort(self.numbers))
	# 		self.result = "버블 정렬\n" + ' '.join(map(str,self.numbers))
	# 		self.numbers = copy.deepcopy(self.nums)
	# 		self.sort_show.config(text="버블 정렬")
	# 		Bubble_sort(self.numbers, master=None)
	# 	elif (self.sort_num == 3):
	# 		# print(self.insert_sort(self.numbers))
	# 		self.result = "삽입 정렬\n" + ' '.join(map(str,self.numbers))
	# 		self.numbers = copy.deepcopy(self.nums)
	# 		self.sort_show.config(text="삽입 정렬")
	# 		Insert_sort(self.numbers, master=None)
	# 	elif (self.sort_num == 4):
	# 		# print(self.merge_sort(self.numbers))
	# 		self.result = "병합 정렬\n" + ' '.join(map(str,self.numbers))
	# 		self.numbers = copy.deepcopy(self.nums)
	# 		self.sort_show.config(text="병합 정렬")
	# 		Merge_sort(self.numbers, master=None)
	# 	else:
	# 		print(self.quick_sort(self.numbers))
	# 		self.result = "퀵 정렬\n" + ' '.join(map(str,self.numbers))
	# 		self.numbers = copy.deepcopy(self.nums)
	# 		self.sort_show.config(text="퀵 정렬")

	def quick_sort(self, arr):
		if len(arr) < 2:
			return arr

		pivot = arr[len(arr) // 2]

		small_arr = []
		large_arr = []
		equal_arr = []
		for num in arr:
			if num < pivot:
				small_arr.append(num)
			elif num > pivot:
				large_arr.append(num)
			else:
				equal_arr.append(num)
		
		return self.quick_sort(small_arr) + equal_arr + self.quick_sort(large_arr)

	def find_file(self):
		self.nums = []
		input_path = filedialog.askopenfilename(initialdir='/', title='select a file',
											filetypes=(("txt files","*.txt"),("all files","*.*")))
		input_file = open(input_path, "r", encoding='UTF-8')
		num_str = input_file.read().splitlines()
		for num in num_str:
			self.nums.append(int(num))
		self.numbers = copy.deepcopy(self.nums)
		input_file.close()

	def save_file(self):
		output_file = open('output.txt', "w", encoding='UTF-8')
		output_file.write(self.result)
		output_file.close()


	#-----------------------------------------
	# pygame	
	# def check_events(self): # Check if the pg window was quit
    # 	for event in pg.event.get():
    #     	if event.type == pg.QUIT:
    #         	pg.quit()
    #         	sys.exit()

	def update(self, algorithm, swap1=None, swap2=None, display=display):
		# The function responsible for drawing the sorted array on each iteration
		display.fill(pg.Color("#a48be0"))
		pg.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display on title bar
		k = int(dimensions[0]/len(algorithm.array))
		for i in range(len(algorithm.array)):
			colour = (80, 0, 255)
			if swap1 == algorithm.array[i]:
				colour = (0,255,0)
			elif swap2 == algorithm.array[i]:
				colour = (255,0,0)
			# The most important step that renders the rectangles to the screen that gets sorted.
			# pg.draw.rect(dsiplay_window, color_of_rectangle, size_of_rectangle)
			pg.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
		# check_events()
		pg.display.update()

	# def keep_open(self, algorithm, display, time): # Keep the window open until sort completion
	# 	pg.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
	# 	while True:
	# 		check_events()

if __name__ == '__main__':
	window = tk.Tk()
	window.title("AL Form Project 201010298 팽건우")
	window.geometry("1080x720") #가로 * 세로
	sort_gui = Sort_Gui(window)
	window.mainloop()