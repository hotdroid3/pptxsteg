from pptxsteg import EmbedExtract
from pptx.exc import PackageNotFoundError
import os


def main():
	"""This is the main function.
	If this module is executed as a script, execution will commence in this function.
	"""
	pptx_file_names = os.listdir(os.getcwd() + '\\test')
	result_list = []
	for pptx in pptx_file_names:
		try:
			pptx_file_path = os.getcwd() + '\\test\\' + pptx
			pptx_file = EmbedExtract(pptx_file_path)
		except PackageNotFoundError as e:
			print('Error! Selected PowerPoint file does not exist!')
			print(pptx_file_path)
			continue
		else:
			stegcap = pptx_file.calculate_capacity()
			file_size = os.stat(pptx_file_path).st_size
			result = stegcap / file_size
			result_list.append(result)

	sum = 0
	for result in result_list:
		sum += result

	final_result = sum / len(result_list)
	print(final_result)




if __name__ == '__main__':
	main()