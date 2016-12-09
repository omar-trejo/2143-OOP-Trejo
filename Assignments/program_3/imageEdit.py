import sys
from PIL import Image
import random
import urllib, cStringIO

class ImageEdit(object):
#---------------------------Constructor---------------------------
    def __init__(self, image, output_file = None):
    	self.img = image
    	self.width = self.img.size[0]
    	self.height = self.img.size[1]
    	self.output = output_file
    	
#---------------------------glass_effect---------------------------
    def glass_effect(self):
        blankimg = Image.new('RGBA', (self.width,self.height), (255,255,255,0))
        glass = 2
        pick = []
        for x in range(glass,self.width-glass):
        	for y in range(glass,self.height-glass):
        		for x2 in range(-glass,glass):
        			for y2 in range(-glass,glass):
        				pixel = self.img.getpixel((x+x2,y+y2))
        				pick.append(pixel)
        		choice = random.choice(pick)
        		blankimg.putpixel((x,y),choice)
        		pick = []
        		
    	blankimg.save(self.output)
    	
    	return blankimg
    	
#---------------------------v_flip---------------------------
    def v_flip(self):
    	blankimg = Image.new('RGBA', (self.width,self.height), (255,255,255,0))
    	opposite = self.height - 1
    	for x in range(self.width):
    		for y in range(self.height):
    			pixel = self.img.getpixel((x,opposite-y))
    			blankimg.putpixel((x,y),(pixel[0],pixel[1],pixel[2]))
    	blankimg.save(self.output)
    	return blankimg
    	
#---------------------------h_flip---------------------------
    def h_flip(self):
    	blankimg = Image.new('RGBA', (self.width,self.height), (255,255,255,0))
    	opposite = self.width - 1
    	for x in range(self.width):
    		for y in range(self.height):
    			pixel = self.img.getpixel((opposite - x,y))
    			blankimg.putpixel((x,y),(pixel[0],pixel[1],pixel[2]))
    	blankimg.save(self.output)
    	return blankimg
    
#---------------------------blur---------------------------
    def blur(self):
    	blankimg = Image.new('RGBA', (self.width,self.height), (255,255,255,0))
    	r,g,b = 0,0,0
    	power = 3
    	pixelBlock = (2*power)*(2*power)
    	for x in range(power, self.width-power):
    		for y in range(power, self.height-power):
    			for x2 in range(-power,power):
    				for y2 in range(-power,power):
    					pixel = self.img.getpixel((x+x2,y+y2))
    					r += pixel[0]
    					g += pixel[1]
    					b += pixel[2]
    			blankimg.putpixel((x,y),(int(r/pixelBlock),int(g/pixelBlock),int(b/pixelBlock)))
    			r = 0
    			g = 0
    			b = 0
    	blankimg.save(self.output)
    	return blankimg

#---------------------------posterize---------------------------
    def posterize(self):
    	blankimg = Image.new('RGBA', (self.width,self.height), (255,255,255,0))
    	
    	for x in range(self.width):
    		for y in range(self.height):
    			pixel = self.img.getpixel((x,y))
    			newPixel = self.snap_color(pixel)
    			blankimg.putpixel((x,y),(newPixel[0],newPixel[1],newPixel[2]))
    	blankimg.save(self.output)
    	return blankimg

#---------------------------snap_color---------------------------
    def snap_color(self,rgb,snap_val = 51):
    	rgb = [rgb[0],rgb[1],rgb[2]]
    	rgb2 = []
    	
    	for x in rgb:
    		m = x % snap_val
    		if m < (snap_val // 2):
    			x -= m
    		else:
    			x += (snap_val - m)
    		rgb2.append(x)
    	
    	return ((rgb2[0],rgb2[1],rgb2[2]))

#---------------------------solarize---------------------------
    def solarize(self):
    	r,g,b = 0,0,0
    	blankimg = Image.new('RGBA', (self.width,self.height), (255,255,255,0))
    	for x in range(self.width):
    		for y in range(self.height):
    			pixel = self.img.getpixel((x,y))
    			r,g,b = pixel
    			blankimg.putpixel((x,y),((255-r),(255-g),(255-b)))
    	
    	blankimg.save(self.output)
    	return blankimg
    	
#---------------------------warhol---------------------------
    def warhol(self):
    	blankimg = Image.new('RGBA', (self.width,self.height), (255,255,255,0))
    	self.img = self.img.convert("L")
    	for x in range(self.width):
    		for y in range(self.height):
    			pixel = self.img.getpixel((x,y))
    			r,g,b = pixel,pixel,pixel
    			blankimg.putpixel((x,y),(r,g,b))
    	
    	self.img = blankimg
    	self.img = self.posterize()
    	
    	for x in range(self.width):
    		for y in range(self.height):
    			pixel = self.img.getpixel((x,y))
    			warholColor = pixel[0]
    			
    			if warholColor > 204:
    				pixel = (255,0,255) #magenta
    			elif warholColor > 153:
    				pixel = (0,0,255) #blue
    			elif warholColor > 102:
    				pixel = (255,165,0) #orange
    			elif warholColor > 51:
    				pixel = (255,255,0) #yellow
    			else:
    				pixel = (0,255,0) #lime green
    			blankimg.putpixel((x,y),pixel)
    	
    	blankimg.save(self.output)
    	return blankimg
        
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
	ie = ImageEdit(img,output_file)
	ie.glass_effect()
	
elif commands['-x'][0] == 'v_flip':
	img = Image.open(input_file)
	ie = ImageEdit(img,output_file)
	ie.v_flip()
	
elif commands['-x'][0] == 'h_flip':
	img = Image.open(input_file)
	ie = ImageEdit(img,output_file)
	ie.h_flip()
	
elif commands['-x'][0] == 'blur':
	img = Image.open(input_file)
	ie = ImageEdit(img,output_file)
	ie.blur()
	
elif commands['-x'][0] == 'posterize':
	img = Image.open(input_file)
	ie = ImageEdit(img,output_file)
	ie.posterize()
	
elif commands['-x'][0] == 'solarize':
	img = Image.open(input_file)
	ie = ImageEdit(img,output_file)
	ie.solarize()
	
elif commands['-x'][0] == 'warhol':
	img = Image.open(input_file)
	ie = ImageEdit(img,output_file)
	ie.warhol()
