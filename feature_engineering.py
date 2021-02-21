#Project Aayu
#Feature Engineering
#renaming files by using python script


#importing os library
import os

#assigning path of the folder
path = os.chdir("C:\\Users\\Bhagya\\Desktop\\New folder")

#assigning initial starting value to 0
initial =1

#using for loop
for file in os.listdir(path):
    #new renaming format (.jpg format)
    new_picture_name="{}.jpg".format(initial)


    os.rename(file,new_picture_name)
    #counting one by one and going to the next picture
    initial=initial+1