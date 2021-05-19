import copy
import algorithms
import time
import os
import sys
import pygame
import tkinter as tk
import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from tkinter import filedialog

class Bubble_sort(tk.Frame):
	def __init__(self, lists, master=None):
		super().__init__(master)
		self.lists = lists
		self.grid(row=40,column=12)
		self.create_widgets()
		
	def create_widgets(self):
		self.draw = tk.Canvas(self)
		self.draw['height'] = 500
		self.draw['width'] = 500
		self.draw.grid(row=40,column=12)
		for x in range(len(self.lists)):
			self.draw.create_oval(x, self.lists[x], x+5, self.lists[x]+5, fill='black')
		self.animate()

	def animate(self):
		self.draw.delete(tk.ALL)
		for i in range(len(self.lists)-1):
			if self.lists[i] > self.lists[i+1]:
				self.lists[i], self.lists[i+1] = self.lists[i+1], self.lists[i]

		for x in range(len(self.lists)):
			self.draw.create_oval(x, self.lists[x], x+5, self.lists[x]+5, fill='black')

		self.draw.after(100, self.animate)

class	Selection_sort(tk.Frame):
	def __init__(self, lists, master=None):
		super().__init__(master)
		self.lists = lists
		self.grid(row=40,column=12)
		self.create_widgets()

	def create_widgets(self):
		self.draw = tk.Canvas(self)
		self.draw['height'] = 500
		self.draw['width'] = 500
		self.draw.grid(row=40, column=12)
		for x in range(len(self.lists)):
			self.draw.create_oval(x, self.lists[x], x+5, self.lists[x]+5, fill='red')
		self.animate()

	def least_idx(self, start):
		least_idx = start

		for i in range(start + 1, len(self.lists)):
			if self.lists[i] < self.lists[least_idx]:
				least_idx = i

		return least_idx

	def animate(self, i=0):
		if i < len(self.lists):
			self.draw.delete(tk.ALL)
			least = self.least_idx(i)
			self.lists[i], self.lists[least] = self.lists[least], self.lists[i]	

			for x in range(len(self.lists)):
				self.draw.create_oval(x, self.lists[x], x+5, self.lists[x]+5, fill='red')

			self.draw.after(100, self.animate, i+1)


class Insert_sort(tk.Frame):
	def __init__(self, lists, master=None):
		super().__init__(master)
		self.lists = lists
		self.grid(row=40,column=12)
		self.create_widgets()

	def create_widgets(self):
		self.draw = tk.Canvas(self)
		self.draw['height'] = 500
		self.draw['width'] = 500
		self.draw.grid(row=40, column=12)
		for x in range(len(self.lists)):
			self.draw.create_oval(x, self.lists[x], x+20, self.lists[x]+20, fill='blue')
		self.animate()

	def animate(self,i=0):
		if i < len(self.lists)-1:
			self.draw.delete(tk.ALL)
			for j in range(i, 0, -1):
				if self.lists[j] > self.lists[j+1]:
					self.lists[j], self.lists[j+1] = self.lists[j+1], self.lists[j]

			for x in range(len(self.lists)):
				self.draw.create_oval(x, self.lists[x], x+5, self.lists[x]+5, fill='blue')

			self.draw.after(100, self.animate, i+1)

class Merge_Sort(tk.Frame):
	def __init__(self, lists, master=None):
		super().__init__("MergeSort")
		self.lists = lists
		algorithm(self.lists)

	def algorithm(self, array):
		if len(array) < 2:
			return array
		mid = len(array) // 2
		left = self.algorithm(array[:mid])
		right = self.algorithm(array[mid:])
		return self.merge(left, right)

	def merge(self, left, right):
		result = []
		i, j = 0, 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
			self.visualizer.update()
		result += left[i:]
		result += right[j:]
		self.array = result
		self.visualizer.update()
		return result
	
	dimensions = (800, 600)
	display = pg.display.set_mode(dimensions)
	# Fill the window with purple hue
	display.fill(pg.Color("#a48be0"))

	def update(self, algorithm, swap1=None, swap2=None):
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
		pg.display.update()

# class Merge_sort(tk.Frame):
# 	def __init__(self, lists, master=None):
# 		super().__init__(master)
# 		self.lists = lists
# 		self.grid(row=40,column=12)
# 		self.create_widgets()

# 	def create_widgets(self):
# 		self.draw = tk.Canvas(self)
# 		self.draw['height'] = 500
# 		self.draw['width'] = 500
# 		self.draw.grid(row=40, column=12)
# 		self.sort(self.lists)

# 	def animate(self, arr):
# 		self.draw.delete(tk.ALL)
# 		for x in range(len(arr)):
# 			self.draw.create_oval(x, arr[x], x+5, arr[x]+5, fill='blue')

# 	def sort(self, arr):
# 		if len(arr) < 2:
# 			return arr
# 		mid = len(arr) // 2
# 		left_arr = self.sort(arr[:mid])
# 		right_arr = self.sort(arr[mid:])
# 		return self.merge(left_arr, right_arr)

# 	def merge(self, left_arr, right_arr):
# 		result = []
# 		l, h = 0, 0

# 		while l < len(left_arr) and h < len(right_arr):
# 			if left_arr[l] < right_arr[h]:
# 				result.append(left_arr[l])
# 				l += 1
# 			else:
# 				result.append(right_arr[h])
# 				h += 1
# 			self.animate(self.lists)

# 		result += left_arr[l:]
# 		result += right_arr[h:]
# 		self.lists = result
# 		self.animate(self.lists)
# 		return result

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

	def sort_select(self):
		self.sort_num = self.sort_var.get()
		if (self.sort_num == 1):
			# print(self.selection_sort(self.numbers))
			self.result = "선택 정렬\n" + ' '.join(map(str,self.numbers))
			self.numbers = copy.deepcopy(self.nums)
			self.sort_show.config(text="선택 정렬")
			Selection_sort(self.numbers, master=None)
		elif (self.sort_num == 2):
			# print(self.bubble_sort(self.numbers))
			self.result = "버블 정렬\n" + ' '.join(map(str,self.numbers))
			self.numbers = copy.deepcopy(self.nums)
			self.sort_show.config(text="버블 정렬")
			Bubble_sort(self.numbers, master=None)
		elif (self.sort_num == 3):
			# print(self.insert_sort(self.numbers))
			self.result = "삽입 정렬\n" + ' '.join(map(str,self.numbers))
			self.numbers = copy.deepcopy(self.nums)
			self.sort_show.config(text="삽입 정렬")
			Insert_sort(self.numbers, master=None)
		elif (self.sort_num == 4):
			# print(self.merge_sort(self.numbers))
			self.result = "병합 정렬\n" + ' '.join(map(str,self.numbers))
			self.numbers = copy.deepcopy(self.nums)
			self.sort_show.config(text="병합 정렬")
			Merge_sort(self.numbers, master=None)
		else:
			print(self.quick_sort(self.numbers))
			self.result = "퀵 정렬\n" + ' '.join(map(str,self.numbers))
			self.numbers = copy.deepcopy(self.nums)
			self.sort_show.config(text="퀵 정렬")

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


if __name__ == '__main__':
	window = tk.Tk()
	window.title("AL Form Project 201010298 팽건우")
	window.geometry("1080x720") #가로 * 세로
	sort_gui = Sort_Gui(window)
	window.mainloop()