import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("AL Form Project 201010298 팽건우")
window.geometry("1080x720") #가로 * 세로


class Sort_Gui:
	def __init__(self):

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
	
		input_button = tk.Button(window, text="find input file", width=20, command=self.find_file).grid(row=20, column=10)
		window.mainloop()

	def sort_select(self):
		sort_num = self.sort_var.get()
		if (sort_num == 1):
			print(self.selection_sort(self.numbers))
			self.sort_show.config(text="선택 정렬")
		elif (sort_num == 2):
			print(self.bubble_sort(self.numbers))
			self.sort_show.config(text="버블 정렬")
		elif (sort_num == 3):
			print(self.insert_sort(self.numbers))
			self.sort_show.config(text="삽입 정렬")
		elif (sort_num == 4):
			print(self.merge_sort(self.numbers))
			self.sort_show.config(text="병합 정렬")
		else:
			print(self.quick_sort(self.numbers))
			self.sort_show.config(text="퀵 정렬")

	def selection_sort(self, arr):
		for i in range(len(arr) - 1):
			least = i
			for j in range(i+1, len(arr)):
				if arr[j] < arr[least]:
					least = j
			arr[i], arr[least] = arr[least], arr[i]
		return arr

	def bubble_sort(self, arr):
		for i in range(1, len(arr)):
			for j in range(len(arr) - i):
				if arr[j] > arr[j + 1]:
					arr[j], arr[j+1] = arr[j+1], arr[j]
		return arr

	def insert_sort(self, arr):
		for i in range(1, len(arr)):
			for j in range(i, 0, -1):
				if arr[j] < arr[j - 1]:
					arr[j], arr[j - 1] = arr[j - 1], arr[j]
		return arr

	def merge_sort(self, arr):
		if len(arr) < 2:
			return arr
		
		mid = len(arr) // 2
		left_arr = self.merge_sort(arr[:mid])
		right_arr = self.merge_sort(arr[mid:])
		
		result = []
		left = right = 0
		while (left < len(left_arr) and right < len(right_arr)):
			if left_arr[left] < right_arr[right]:
				result.append(left_arr[left])
				left += 1
			else:
				result.append(right_arr[right])
				right += 1
		
		result += left_arr[left:]
		result += right_arr[right:]
		
		return result


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
		self.numbers = []
		input_path = filedialog.askopenfilename(initialdir='/', title='select a file',
											filetypes=(("txt files","*.txt"),("all files","*.*")))
		input_file = open(input_path, "r", encoding='UTF-8')
		num_str = input_file.read().splitlines()
		for num in num_str:
			self.numbers.append(int(num))
				


		

#------------------------

#file 부분 https://appia.tistory.com/111
# https://docs.python.org/ko/3.9/library/dialog.html





# sort_start_button = tk.Button(window, text="Sort Start", width=20, command=sort_select(numbers_global)).grid(row=20, column=15)

# 그래프 그리기 부분
# https://www.delftstack.com/ko/howto/matplotlib/how-to-plot-in-real-time-using-matplotlib/

sort_gui = Sort_Gui()
