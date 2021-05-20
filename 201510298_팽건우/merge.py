import time

def merge_sort(data, left, right, drawData):
	if left < right:
		mid = (left + right) // 2
		merge_sort(data, left, mid, drawData)
		merge_sort(data, mid + 1, right, drawData)
		merge(data, left, mid, right, drawData)

def merge(data, left, mid, right, drawData):
	
	drawData(data, getColorArray(len(data), left, mid, right))
	time.sleep(0.3)

	left_part = data[left:mid+1]
	right_part = data[mid+1:right+1]

	left_idx, right_idx = 0, 0

	for data_idx in range(left, right+1):
		if left_idx < len(left_part) and right_idx < len(right_part):
			if left_part[left_idx] <= right_part[right_idx]:
				data[data_idx] = left_part[left_idx]
				left_idx += 1
			else:
				data[data_idx] = right_part[right_idx]
				right_idx += 1
		elif left_idx < len(left_part):
			data[data_idx] = left_part[left_idx]
			left_idx += 1
		else:
			data[data_idx] = right_part[right_idx]
			right_idx += 1

	drawData(data, ['Green' if x >= left and x <= right else "White" for x in range(len(data))])
	time.sleep(0.3)

def getColorArray(dataLen, left, mid, right):
	colorArray = []
	for i in range(dataLen):
		# base coloring
		if i >= left and i <= right:
			if i <= mid:
				colorArray.append("Yellow") #left_part
			else:
				colorArray.append("Blue") #right_part
		else:
			colorArray.append("White")
	return colorArray