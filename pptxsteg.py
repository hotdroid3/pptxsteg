from pptx import Presentation
import lzma
import math

class EmbedExtract():
	"""docstring for EmbedExtract"""
	def __init__(self, pptx_file_name):
		super().__init__()
		self.pptx_file_name = pptx_file_name
		self.pptx_file = Presentation(pptx_file_name)
		
	def get_pptx_obj(self):
		return self.pptx_file

	def save_pptx(self, file_name):
		self.get_pptx_obj().save(file_name)

	def embed_hex(self, hex_strings):

		if (self.get_num_of_shapes() * 4) > len(hex_strings): #need to calc capacity
			hex_strings.reverse()
			pptx = self.get_pptx_obj()
			slides = pptx.slides

			for slide in slides:
				shapes = slide.shapes
				for shape in shapes:

					left = shape.left
					top = shape.top
					width = shape.width
					height = shape.height

					if left is None:
						continue

					elif top is None:
						continue

					elif width is None:
						continue

					elif height is None:
						continue

					if len(hex_strings) == 0:
						left = left // 1000
						left = left * 1000
						left = left + 256
						self.change_shape_dimensions(shape, dimensions = [left, top, width, height])
						return
					else:
						left = left // 1000
						left = left * 1000
						left = left + int(hex_strings.pop(), 16)
						self.change_shape_dimensions(shape, dimensions = [left, top, width, height])
					
					if len(hex_strings) == 0:
						top = top // 1000
						top = top * 1000
						top = top + 256
						self.change_shape_dimensions(shape, dimensions = [left, top, width, height])
						return
					else:
						top = top // 1000
						top = top * 1000
						top = top + int(hex_strings.pop(), 16)
						self.change_shape_dimensions(shape, dimensions = [left, top	, width, height])

					if len(hex_strings) == 0:
						width = width // 1000
						width = width * 1000
						width = width + 256
						self.change_shape_dimensions(shape, dimensions = [left, top, width, height])
						return
					else:
						width = width // 1000
						width = width * 1000
						width = width + int(hex_strings.pop(), 16)
						self.change_shape_dimensions(shape, dimensions = [left, top, width, height])
						
					if len(hex_strings) == 0:
						height = height // 1000
						height = height * 1000
						height = height + 256
						self.change_shape_dimensions(shape, dimensions = [left, top, width, height])
						return
					else:
						height = height // 1000
						height = height * 1000
						height = height + int(hex_strings.pop(), 16)
						self.change_shape_dimensions(shape, dimensions = [left, top, width, height])

		else:
			raise InsufficientCapacityError(self.count_num_of_shapes() * 4, len(hex_strings) + 1)

	def extract_hex(self):

		hex_strings = []
		pptx = self.get_pptx_obj()
		slides =  pptx.slides

		for slide in slides:
			shapes = slide.shapes
			for shape in shapes:

				left = shape.left
				top = shape.top
				width = shape.width
				height = shape.height

				if left is None:
					continue

				elif top is None:
					continue

				elif width is None:
					continue

				elif height is None:
					continue

				if left % 1000 == 256:
					return hex_strings
				else:
					left = left % 1000
					left = bytes([left]).hex()
					hex_strings.append(left)

				if top % 1000 == 256:
					return hex_strings
				else:
					top = top % 1000
					top = bytes([top]).hex()
					hex_strings.append(top)

				if width % 1000 == 256:
					return hex_strings
				else:
					width = width % 1000
					width = bytes([width]).hex()
					hex_strings.append(width)

				if height % 1000 == 256:
					return hex_strings
				else:
					height = height % 1000
					height = bytes([height]).hex()
					hex_strings.append(height)
					


	def change_shape_dimensions(self, shape, dimensions):
		"""Helper method to change the shape dimensions"""
		shape.left, shape.top, shape.width, shape.height = dimensions

	def get_num_of_shapes(self):
		""""""
		p = self.get_pptx_obj();
		count = 0
		slides = p.slides
		for slide in slides:
			shapes = slide.shapes
			count += len(shapes)
		return count

	def get_num_of_usable_shapes(self):

		count = 0
		p = self.get_pptx_obj();
		slides = p.slides
		for slide in slides:
			shapes = slide.shapes
			for shape in shapes:
				if shape.left is None:
					print(shape.left)
					continue
				elif shape.top is None:
					print(shape.top)
					continue
				elif shape.width is None:
					print(shape.width)
					continue
				elif shape.height is None:
					print(shape.height)
					continue
				count = count + 1
		return count

class Error(Exception):
	"""Base class for exceptions in this module."""
	pass

class InsufficientCapacityError(Error):
	"""Exception raised when there is insufficient steganographic capacity
	provided by the cover PowerPoint file to store the steganograms.
	"""
	def __init__(self, steganographic_capacity, required_capacity):
		super().__init__()
		self.steganographic_capacity = steganographic_capacity
		self.required_capacity = required_capacity
		
	def __str__(self):
		avail_steg_cap = 'Available Steganographic Capacity: {} bytes\n'.format(self.steganographic_capacity)
		req_steg_cap = 'Required Steganographic Capacity: {} bytes\n'.format(self.required_capacity)
		return avail_steg_cap + req_steg_cap

def main():
	"""This is the main function.
	If this module is executed as a script, execution will commence in this function.
	"""
	# codec = EncoderDecoder()
	embed = EmbedExtract('testing.pptx')
	hex_strings = embed.extract_hex()
	EncoderDecoder.decode_to_file(hex_strings,'virus.py')
	# hex_strings = EncoderDecoder.encode_from_file('stegpptx.py')
	# embed.embed_hex(hex_strings)
	# embed.save_pptx('testing.pptx')
	# print(embed.count_num_of_shapes())
	# print(embed.count_num_of_usable_shapes())
	# hex_strings = EncoderDecoder.encode_from_file('123.zip')
	# embed.embed_hex(hex_strings)
	# embed.save_pptx('testing.pptx')
	# print(embed.count_num_of_shapes() * 4)
	# embedded = EmbedExtract('testing.pptx')
	# hex_strings = embedded.extract_hex()
	# EncoderDecoder.decode_to_file(hex_strings,'test.py')
	# print(embed.count_num_of_shapes())
	# embed.embed_hex('blabla')
	# embed.save_pptx('test.pptx')
	# hexstring = EncoderDecoder.encode_from_file('1.jpg')
	# EncoderDecoder.decode_to_file(hexstring, '123.jpg')
	# hex_str = EncoderDecoder.encode_from_string('hello world')
	# print(EncoderDecoder.decode_to_string(hex_str))
	# print(dir(pptx))

if __name__ == '__main__':
	main()


##coreproperties -
##check font size property -

##shape.name 1641 -

##find out how big file size to determine how much space should go into the shape.name

##remember to catch FileNotFoundError, catch FileNameTooLong when calling encode_from_file


#count_num_of_usable_shapes compare with count num of shapes

#calculate capacity


##use property


##write exceptions for opening files
##slide number and object that is giving problem

##if compress, last char is c
##if not compressed, last char is n

##extract and straight run exe?




##encryption and authenticity



##print compression savings, test compression savings

##check compression if working

##do gui

##separate into modules







##remember filename - done

##shape.rotation - precision is not good enough - done

##create new class for compression error - done

##test custom error handling classes
	##CompressionError - done
	##FileNameTooLongError - done
	##InsufficientCapacityError - ?