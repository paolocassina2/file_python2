from PIL import Image
import pyocr
import pyocr.builders
import sys

file_path = 'C:\\Users\\Attilio\\Desktop\\file_python\\sudoku.PNG'
#Tool loading
tools = pyocr.get_available_tools()
#If you can't find the tool
if len(tools) == 0:
    print('I cant find pyocr. Please install pyocr.')
    sys.exit(1)
tool = tools[0]
#Image loading
img_org = Image.open(file_path)
# OCR
max_medals = tool.image_to_string(img_org, lang='jpn', builder=pyocr.builders.DigitBuilder(tesseract_layout=6))
print(f'max_medals：{max_medals}')
