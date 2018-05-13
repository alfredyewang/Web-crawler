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

```
images
|Category name1
|  |_Query1
|  |    |_00001.jpg
|  |    |_00002.jpg
|  |_Query2
|  |    |_00001.jpg
|  |    |_00002.jpg
|Category name2
|  |_Query1
|  |    |_00001.jpg
|  |    |_00002.jpg
|  |_Query2
|  |    |_00001.jpg
|  |    |_00002.jpg
```

## Update: Category csv file and rename.sh script
After you run run.py with your own csv and satisfy your the result. Please run rename.sh file to rename the image. It will give each image a unique ID. The format should be ```<CategoryID>_<ImageID>.jpg```

## Usage of rename.sh
bash rename.sh

## Images directory structure after you rename images

```
images
|Category name1
|  |_Query1
|  |    |_00001.jpg
|  |    |_00002.jpg
|  |_Query2
|  |    |_00001.jpg
|  |    |_00002.jpg
|  |_Category name1_all
|  |    |_00001_00001.jpg
|  |    |_00001_00002.jpg

|Category name2
|  |_Query1
|  |    |_00001.jpg
|  |    |_00002.jpg
|  |_Query2
|  |    |_00001.jpg
|  |    |_00002.jpg
|  |_Category name2_all
|  |    |_00002_00001.jpg
|  |    |_00002_00002.jpg
```


