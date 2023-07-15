# UK VISA Travel Bot 

No fancy names. Just bot, I guess. 

## Overview 

There are three Python code files here. Each of them does a different thing, and theoretically can run independently of the others. 

After you have filled in trip-records-template.xlsx (and followed the instructions inside), run generate_report.py. This should generate a text document (.txt) with all your trips, formatted with start date, end date, and duration. 

After doing this, you can run get_document.py, which makes this into a Word Document. This will be helpful if you have more than 30 trips; you can upload this as your VISA supporting document. 

For fill_form.py, you need to create a new CSV, 'trip-records-no-europe.csv', which contains all your non-European trips. Once this is done, go to the VISA page where you need to fill in your trips, and run the bot. It should automatically fill in your form as needed. If you want to restart the bot, change your answer for overseas trips to NO, change it back to YES again, and rerun. 


Note: This may not succeed 100% of the time, and the bot can do some crazy weird things. I highly highly recommend being next to your computer and watching the bot while it runs. Definitely not from personal experience while tuning the bot. Definitely. Anyway, if this happens, move your cursor all the way to the toppest rightest corner of your screen and wait for 10 seconds. It should be terminated. 


You may face an error that some directories/folders do not exist. If you face those errors, remove the following line: 

```python 
os.chdir('../../Oxford')
```

Note 2: To run this successfully, copy all your Excel and CSV files into the folder storing this code. Run it from there. 


## Requisite Modules 

The following modules are required for the bot to work: 
```bash
pandas 
python-docx 
pyautogui 
```

You can install them with pip or conda. 


Happy hacking! 



