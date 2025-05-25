# -question 3-*-
"""
Created on Wed Aug 15 23:02:59 2018

@author: SRIKANT
"""

from PIL import Image
import os




input_dir='../input_image/'
output_dir='../result/'


if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
img=Image.open(input_dir+'lenna.jpg')


img1=img
img1=img1.crop((200,200,365,400))
img1.save(output_dir+'3-lenna_cropped.jpg')

img.paste(img1)

img.save(output_dir+'4-lenna_paste.jpg')


r,g,b = img1.split()
r.save(output_dir+'5-lenna_red.jpg')
g.save(output_dir+'6-lenna_green.jpg')
b.save(output_dir+'7-lenna_blue.jpg')


new_img = Image.merge("RGB",(r,g,b))
new_img.save(output_dir+'8-lenna_paste.jpg')



img = Image.open(input_dir+'lenna.jpg')
resize_img = img.resize((150,250), resample=0)
resize_img.save(output_dir+'9-lenna_resize.jpg')


img = Image.open(input_dir+'lenna.jpg')
rot_image = img.rotate(30)
rot_image.save(output_dir+'9-lenna_rotate.jpg')



img = Image.open(input_dir+'lenna.jpg')
tran = img.transpose(Image.FLIP_TOP_BOTTOM)
tran.save(output_dir+'10-lenna_trans.jpg')



A = Image.open(input_dir+'lenna.jpg')
A = A.resize((512,512), resample = 0)
B = Image.open(input_dir+'lenna.jpg')
B = B.resize((512,512), resample = 0)
C = Image.blend(A, B, alpha = 0.5)
C.save(output_dir+'9-lenna.jpg')

#Image copying
A = Image.open(input_dir+'lenna.jpg')
D = A.copy()
D.save(output_dir+'10-len.jpg')

#getbands
A = Image.open(input_dir+'lenna.jpg')
F = A.getbands()
print('Image bands of lenna.jpg {}'.format(F))
#getextrema
G = Image.open(input_dir+'lenna.jpg')
F = G.getextrema()
print('Extremas of lenna.jpg {}'.format(F))

#getpixel
H = Image.open(input_dir+'lenna.jpg')
F = H.getpixel((250,250))
print('Value of pixel at location 250,250 in lenna.jpg {}'.format(F))
#putpixel
H = Image.open(input_dir+'lenna.jpg')
H = H.resize((512,512))
for i in range(512):
    H.putpixel((i,i), (0,0,0,255))

H.save(output_dir+'lenna-putpxl.jpg')





