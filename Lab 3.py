import pandas as pd
#reading of csv file
df=pd.read_csv("Iris.csv")
print(df.head())


#reading of json file
dfjson=pd.read_json("iris.json")
print(dfjson.head())


#reading of text file
dftxt=open("file.txt")
print(dftxt.read())


#reading of excel file
dfexcel=pd.read_excel("historical_data.xlsx")
print(dfexcel.head())

#image file
from matplotlib import pyplot as plt
from matplotlib import image as mpimg 
plt.title("image")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")
image = mpimg.imread("Untitled design (22).png")
plt.imshow(image)
plt.show()



#zipfile
import zipfile
archive=zipfile.ZipFile("Untitled design (22).zip")
img=archive.read("Untitled design (22).png")
print(img)

#.html
from bs4 import BeautifulSoup
html_file = open("booking.html")
index = html_file.read()
print(index)
#.pda
