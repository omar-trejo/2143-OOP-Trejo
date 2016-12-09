from PIL import Image
import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import imageEdit
import urllib, cStringIO


if __name__=="__main__":
	print(sys.argv)

flags = ['-i','-o','-x','-h']

commands = {}

for i in range(1,len(sys.argv),2):
    commands[sys.argv[i]] = sys.argv[i+1]

commands['-x'] = commands['-x'].split(',')
print(commands)

if '-i' in commands.keys():
    input_file = commands['-i']
    
if '-o' in commands.keys():
    output_file = commands['-o']
else:
    output_file = (str(commands['-x'])+'.jpg')

if commands['-x'][0] == 'glass_effect':
	img = Image.open(input_file)
	ie = imageEdit.ImageEdit(img,output_file)
	ie.glass_effect()
	
elif commands['-x'][0] == 'v_flip':
	img = Image.open(input_file)
	ie = imageEdit.ImageEdit(img,output_file)
	ie.v_flip()
	
elif commands['-x'][0] == 'h_flip':
	img = Image.open(input_file)
	ie = imageEdit.ImageEdit(img,output_file)
	ie.h_flip()
	
elif commands['-x'][0] == 'blur':
	img = Image.open(input_file)
	ie = imageEdit.ImageEdit(img,output_file)
	ie.blur()
	
elif commands['-x'][0] == 'posterize':
	img = Image.open(input_file)
	ie = imageEdit.ImageEdit(img,output_file)
	ie.posterize()
	
elif commands['-x'][0] == 'solarize':
	img = Image.open(input_file)
	ie = imageEdit.ImageEdit(img,output_file)
	ie.solarize()
	
elif commands['-x'][0] == 'warhol':
	img = Image.open(input_file)
	ie = imageEdit.ImageEdit(img,output_file)
	ie.warhol()
