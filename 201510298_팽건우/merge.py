import time

def merge_sort(data, drawData):
	if len(data) < 2:
		return data
	mid = len(data) // 2
	left = merge_sort(data[:mid], drawData)
	right = merge_sort(data[mid:], drawData)
	return merge(data, left, right, drawData)

def merge(data, left, right, drawData):
	result = []
	i, j = 0, 0

	drawData(data, getColorArray(len(data), head,
						tail, border, border))
	time.sleep(0.3)

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1

		drawData(data, getColorArray(len(data), head, 
							tail, border, border))
		time.sleep(0.3)

	result += left[i:]
	result += right[j:]

	drawData(data, getColorArray(len(data), head,
							tail, border, border))
	time.sleep(0.3)
	return result


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