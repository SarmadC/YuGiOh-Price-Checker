![YGO Price Check Banner](https://github.com/SarmadC/YuGiOh-Price-Checker/blob/main/YUGIOH%20PRICE%20CHECK.png)

![Downloads](https://img.shields.io/github/downloads/SarmadC/YuGiOh-Price-Checker/total?style=flat-square)

#### What the program does?
This program gathers Yugioh card pricing data and populates an excel file using unique tags. The data in the excel file can then be analyzed to create visualizations and a dashboard containing price trend information. 

#### How was the program created?
The program was created in Python using the YGO prices API.

#### Why YGO Prices API?
The reason YGO prices API was used is that it is free and does not require access to a private key compared to the TCG Player API.

### Future Features

I would like this program to provide quick visual access to the price trends of Yugioh cards, pricing anomalies, and much more. Another feature I want to
implement is the ability to preview images of the card in the excel file by hovering over the image URL. This could be possible with using VBA

**Requirements**
---

1. Python

    + [Download here](https://www.python.org/downloads/)
        - Version 3.0+

2. Microsoft Excel

    + Create a New Blank Sheet
        - Blank sheet must have a ['print_tag'](https://user-images.githubusercontent.com/20826612/201443560-7c0cbda7-282e-462c-85ed-13c6b3adc0c2.png)  column and insert your print_tags under this column like so 
        - ![Print tag examples](https://user-images.githubusercontent.com/20826612/201444295-1cc4cdc8-c7f0-4ce3-ba23-725bd1fd1bf8.png)

        - Make sure to save the .xlsx file in the same file path where the .py file was downloaded
        

**How to Use**
---
1. Install the 'YGO Price.py' file and import the required libraries
    ```
    import openpyxl
    import requests
    import pandas as pd
    import time
    ```
    + pip install these libraries from Terminal if not already downloaded

2. Import your print tag .xlsx file into the program
   + ```df = pd.read_excel('Your excel file.xlsx', usecols = ['print_tag'])```

3. Give your file an output name
   ```df2.to_excel('Name Your Excel File Output.xlsx')```

4. Open your file and your dataset should be there


**Use Case for Dataset**
---

1. Interactive PowerBI Dashboard
     <img width="1222" alt="Screenshot 2022-11-10 at 10 30 04 PM" src="https://user-images.githubusercontent.com/20826612/201270198-06a71be1-e132-4b95-bd6b-cf678d15a5a6.png">

2. Excel Spreadsheet
    <img width="1559" alt="Screenshot 2022-11-10 at 10 37 55 PM" src="https://user-images.githubusercontent.com/20826612/201271144-a4fc7145-d3bd-4793-9b35-c742ed7e4e3f.png">


**Donation**

This is free, open-source software. If you'd like to support the development of future projects, or say thanks for this one, you can 
[buy me a coffee](https://ko-fi.com/sarmadc).
