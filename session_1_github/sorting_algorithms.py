def merge_sort(arr):
	"""Merge Sort Algorithm - O(n log n) time complexity"""
	if len(arr) <= 1:
		return arr
	
	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	
	return merge(left, right)

def merge(left, right):
	"""Helper function to merge two sorted arrays"""
	result = []
	i = j = 0
	
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	
	result.extend(left[i:])
	result.extend(right[j:])
	return result

def insertion_sort(arr):
	"""Insertion Sort Algorithm - O(n²) time complexity"""
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		
		arr[j + 1] = key
	
	return arr

def quick_sort(arr):
	"""Quick Sort Algorithm - O(n log n) average time complexity"""
	if len(arr) <= 1:
		return arr
	
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	
	return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
	# Sample list for testing
	sample_list = [64, 34, 25, 12, 22, 11, 90, 5]
	
	print("Original list:", sample_list)
	print()
	
	# Test Merge Sort
	merge_result = merge_sort(sample_list.copy())
	print("Merge Sort result:", merge_result)
	
	# Test Insertion Sort
	insertion_result = insertion_sort(sample_list.copy())
	print("Insertion Sort result:", insertion_result)
	
	# Test Quick Sort
	quick_result = quick_sort(sample_list.copy())
	print("Quick Sort result:", quick_result)