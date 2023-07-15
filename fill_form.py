import pandas as pd
import pyautogui
import time
import os 

# Fills the form

# os.chdir('../../Oxford')

# Load the DataFrame
df = pd.read_csv('trip-records-no-europe.csv')  # Replace 'your_data.csv' with your actual file name

# Convert date columns to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'], dayfirst=True)
df['End Date'] = pd.to_datetime(df['End Date'], dayfirst=True)

# Strip string from location 
df['Location'] = df['Location'].apply(str.strip)

input("Press enter when you are ready to begin. Script will then begin in 2 seconds...")
time.sleep(2) 

# Set starting row index (in case of crashes or bugs)
start_index = 31  # Replace with the desired starting row index

# Loop through the DataFrame rows
for i, row in df.iterrows():
    if i < start_index:
        continue  # Skip rows until the starting index is reached

    # Wait for the form to load
    time.sleep(3)

    # Perform key tabs and inputs
    for i in range(7):  # either this or 2
        pyautogui.press('tab')
        pyautogui.time.sleep(0.2)
        # print(pyautogui.getActiveWindowTitle())
        # if "TextField" in pyautogui.getActiveWindowTitle():
        #     break
    # pyautogui.press('tab', presses=7)
    # pyautogui.time.sleep(0.2)
    pyautogui.typewrite(row['Location'])
    pyautogui.time.sleep(0.2)
    pyautogui.press('tab', presses=2)
    pyautogui.time.sleep(0.2)
    pyautogui.press('up')
    pyautogui.time.sleep(0.2)
    pyautogui.press('down')
    pyautogui.time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.time.sleep(0.2)
    print(str(row['Start Date'].day))
    pyautogui.typewrite(str(row['Start Date'].day))
    pyautogui.time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.time.sleep(0.2)
    print(str(row['Start Date'].month))
    pyautogui.typewrite(str(row['Start Date'].month))
    pyautogui.time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.time.sleep(0.2)
    print(str(row['Start Date'].year))
    pyautogui.typewrite(str(row['Start Date'].year))
    pyautogui.time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.time.sleep(0.2)
    print(str(row['End Date'].day))
    pyautogui.typewrite(str(row['End Date'].day))
    pyautogui.time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.time.sleep(0.2)
    print(str(row['End Date'].month))
    pyautogui.typewrite(str(row['End Date'].month))
    pyautogui.time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.time.sleep(0.2)
    print(str(row['End Date'].year))
    pyautogui.typewrite(str(row['End Date'].year))
    pyautogui.time.sleep(0.2)
    pyautogui.press('tab')
    pyautogui.time.sleep(0.2)
    pyautogui.press('enter')

    # Wait for the form to submit
    time.sleep(3)

    # Print the number of entries completed
    entries_completed = i - start_index + 1
    print(f"Completed {entries_completed} entries.")

    # Check if it's the last entry
    if i < len(df) - 1:
        # Move to the next page
        pyautogui.press('tab', presses=7)
        pyautogui.press('up')
        pyautogui.press('down')
        pyautogui.press('tab')
        pyautogui.press('enter')

# Done!
print("Form filling completed.")
