import os

print os.getcwd()
# Change The Directory According to it print out
# Take All the Image Names
file_list = os.listdir(r'c:/users/mim/Desktop/secret_message/alphabet')
for image in file_list:
	os.chdir(r"c:/users/mim/Desktop/secret_message/alphabet")
	os.rename(image,image.translate(None,'1234567890'))
print 'Done Renamin'