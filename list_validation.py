import functools


def validate_list(func):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		if 'items' in kwargs:
			items = kwargs['items']
			if not isinstance(items, (list, tuple, set)):
				raise TypeError(
					'Expected list, tuple or set, got %s.' % type(items))
			kwargs['items'] = list(items)		
		return func(*args, **kwargs)
	return wrapper
  
