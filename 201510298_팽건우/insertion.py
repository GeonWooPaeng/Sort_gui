import time

def insertion_sort(data, drawData):
	n = len(data)

	for i in range(1, n):
		for j in range(i, 0, -1):
			if data[j] < data[j-1]:
				data[j-1], data[j] = data[j], data[j-1]

				drawData(data, getColorArray(data, j))
				time.sleep(0.3)

	drawData(data, ['Green' for x in range(n)])


def getColorArray(data, jdx):
	colorArray = []
	for x in range(len(data)):
		if x == jdx:
			colorArray.append('Green')
		elif x == jdx - 1:
			colorArray.append('Blue')
		else:
			colorArray.append('Red')
	return colorArray