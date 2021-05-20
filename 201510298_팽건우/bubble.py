import time

def bubble_sort(data, drawData):
	n = len(data)

	for i in range(n):
		for j in range(0, n-i-1):
			if data[j] > data[j+1]:
				data[j], data[j+1] = data[j+1], data[j]

				drawData(data, getColorArray(data, j))
				time.sleep(0.3)

def getColorArray(data, jdx):
	colorArray = []
	for x in range(len(data)):
		if x == jdx:
			colorArray.append('Green')
		elif x == jdx + 1:
			colorArray.append('Blue')
		else:
			colorArray.append('Red')
	return colorArray