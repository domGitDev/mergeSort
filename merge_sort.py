from list_validation import validate_list


@validate_list
def merge_sort(start, end, items=None):
	
	def merge_subarray(start, mid, end):
		low_half = [
			items[i] for i in xrange(start, mid+1)]
		high_half = [
			items[j] for j in xrange(mid+1, end+1)]
			
		k = start
		i = 0
		j = 0		
		low_count = mid - start + 1
		high_count = end - mid
		
		while i < low_count and j < high_count:
			if low_half[i] < high_half[j]:
				items[k] = low_half[i]
				i += 1
			else:
				items[k] = high_half[j]
				j+= 1
			k += 1
			
		while i < low_count:
			items[k] = low_half[i]
			i += 1
			k += 1
			
		while j < high_count:
			items[k] = high_half[j]
			j += 1
			k+= 1
			
	if start >= end:
		return 
	if start < end:
		mid = (start + end)	/ 2
		merge_sort(start, mid, items)
		merge_sort(mid+1, end, items)
		merge_subarray(start, mid, end) 
	return items	
			
data = [14, 7, 3, 12, 9, 11, 6, 2]
sorted_data = merge_sort(0, len(data)-1, items=data)
print sorted_data
assert [2, 3, 6, 7, 9, 11, 12, 14] == sorted_data
