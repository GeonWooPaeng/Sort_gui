# Extension Quick Sort Code
# importing time module
import time
  
# to implement divide and conquer
def partition(data, head, tail, drawData):
	border = head
	pivot = data[tail]
  
	drawData(data, getColorArray(len(data), head, 
								 tail, border, border))
	time.sleep(0.3)

	for j in range(head, tail):
		if data[j] < pivot:
			drawData(data, getColorArray(
				len(data), head, tail, border, j, True))
			time.sleep(0.3)
  
			data[border], data[j] = data[j], data[border]
			border += 1
  
		drawData(data, getColorArray(len(data), head, 
									 tail, border, j))
		time.sleep(0.3)
  
	# swapping pivot with border value
	drawData(data, getColorArray(len(data), head, 
								 tail, border, tail, True))
	time.sleep(0.3)
  
	data[border], data[tail] = data[tail], data[border]
  
	return border
  
  
# head  --> Starting index,
# tail  --> Ending index
def quick_sort(data, head, tail, 
			   drawData):
	if head < tail:
		partitionIdx = partition(data, head, 
								 tail, drawData)
  
		# left partition
		quick_sort(data, head, partitionIdx-1, 
				   drawData)
  
		# right partition
		quick_sort(data, partitionIdx+1, 
				   tail, drawData)
  
# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - Sfter all elements are sorted
  
# assign color representation to elements
  
  
def getColorArray(dataLen, head, tail, border,
				  currIdx, isSwaping=False):
	colorArray = []
	for i in range(dataLen):
		# base coloring
		if i >= head and i <= tail:
			colorArray.append('Grey')
		else:
			colorArray.append('White')
  
		if i == tail:
			colorArray[i] = 'Blue'
		elif i == border:
			colorArray[i] = 'Red'
		elif i == currIdx:
			colorArray[i] = 'Yellow'
  
		if isSwaping:
			if i == border or i == currIdx:
				colorArray[i] = 'Green'
  
	return colorArray