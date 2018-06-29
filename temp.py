# try:
# 	assert isinstance(shape, pptx.shapes.autoshape.Shape)
# except AssertionError:
# 	continue

# assert (shape._element.x is not None)


# if shape.has_text_frame:
					# 	left = shape._effective_value('left')
					# 	txt = shape.text_frame.paragraphs[0]
					# 	print(str(shape.element))
					# 	print(txt.text)
					# 	print(shape.placeholder_format.type)
				# if left is None:
				# 	shape.left = 0
				# 	left = 800000
				# if top is None:
				# 	shape.top = 0
				# 	top = 80
				# if width is None:
				# 	shape.width = 0
				# 	width = 80
				# if height is None:
				# 	shape.height = 0
				# 	height = 80
				# # if shape.text:
				# # 	text = shape.text
				# # 	print(text)
				# # print(slide.slide_id)
				# # print(shape.shape_type)
				# # print(left)
				# if shape.is_placeholder:
				# 	phf = shape.placeholder_format
				# 	print(phf.idx)
				# 	print(phf.type)
		# print(slide.name)
		# print(type(slide.name))
		# print(slide.slide_id)
		# print(type(slide.slide_id))
				# left = left + 80
				# top = top + 80
				# width = width + 80
				# height = height + 80
				# shape.left = left
				# shape.top = top
				# shape.width = width
				# shape.height = height


				# statinfo = os.stat(file_name)
				# atime = str(statinfo.st_atime_ns).encode()
				# mtime = str(statinfo.st_mtime_ns).encode()
				# atime_length = bytes([len(atime)])
				# mtime_length = bytes([len(mtime)])
				# mtime_length = int.from_bytes(secret_file_bytes[-2:-1], byteorder = 'big')
				# atime_length = int.from_bytes(secret_file_bytes[-3:-2], byteorder = 'big')

				# mtime_partition = (file_name_partition[0] - mtime_length), file_name_partition[0]
				# mtime = secret_file_bytes[mtime_partition[0]:mtime_partition[1]]
				# mtime = int(mtime.decode())

				# atime_partition = (mtime_partition[0] - atime_length), mtime_partition[0]
				# atime = secret_file_bytes[atime_partition[0]:atime_partition[1]]
				# atime = int(atime.decode())
				# os.utime(file_name, ns = (atime, mtime))