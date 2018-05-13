# Download images from Google Images

## Requirements

- Mac OS
- Python 3.5+ 
- Selenium
- Geckodriver

## Usage
- python3 run.py --queries_file_name="examples.csv"

## Format of csv file (see examples.cvs)
[category name1], [query1], [query2], [query3]  
[category name2], [query2], [query2], [query3]..., [query7]  
PS: There is a spcae after comma.

## Images directory structure

'''
images
|Category name
|  |_ Query1
|  |    |_ 00001.jpg
|  |    |_ 00002.jpg
|  |_ Query2
|_ |_   |
- 
|_ ...
|_ annotations
   |_ instances_train2014.json
   |_ ...
'''

## Update: rename.sh bash script
After you run run.py file with your own csv and satisfy your the result. Please run rename.sh file to rename the image.

## Usage of rename.sh
bash rename.sh


