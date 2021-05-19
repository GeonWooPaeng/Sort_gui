import time

def selection_sort(data, drawData):
	n = len(data)

	for i in range(n):
		min_idx = i
		for j in range(i+1, n):
			if data[j] < data[min_idx]:
				min_idx = j
		data[i], data[min_idx] = data[min_idx], data[i]

		drawData(data, getColorArray(data, i, min_idx))
		time.sleep(0.3)
	drawData(data, ['Green' for x in range(n)])

def getColorArray(data, idx, mdx):
	colorArray = []
	for x in range(len(data)):
		if x == idx:
			colorArray.append('Green')
		elif x == mdx:
			colorArray.append('Blue')
		else:
			colorArray.append('Red')
	return colorArray


