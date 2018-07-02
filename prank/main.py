import os

# Take All the Image Names
file_list = os.listdir('C:/Users/Mim/Desktop/prank/images')
print os.getcwd()
for image in file_list:
	os.chdir(r"C:/Users/Mim/Desktop/prank/images")
	os.rename(image,image.translate(None,'1234567890'))
print 'Done Renamin'