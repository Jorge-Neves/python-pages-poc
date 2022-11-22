from tkinter import *
from pages.page01 import page_data_01
from pages.page02 import page_data_02
from pages.page03 import page_data_03
from pages.page04 import page_data_04
from pages.page05 import page_data_05
from pages.page06 import page_data_06
from pages.page07 import page_data_07
from pages.page08 import page_data_08
from pages.page09 import page_data_09
from pages.page10 import page_data_10
from pages.page11 import page_data_11
from pages.page12 import page_data_12
from pages.page13 import page_data_13
from pages.page14 import page_data_14
from pages.page15 import page_data_15

root = Tk()

root.geometry("500x250")

pages_array = [page_data_01,
               page_data_02,
               page_data_03,
               page_data_04,
               page_data_05,
               page_data_06,
               page_data_07,
               page_data_08,
               page_data_09,
               page_data_10,
               page_data_11,
               page_data_12,
               page_data_13,
               page_data_14,
               page_data_15]

current_page = 1

my_text = page_data_01


# function define for
# updating the my_label
# widget content
def update_text():
    # use global variable
    global my_text

    # configure
    myLabel.config(text=my_text)


def decrease_page_number():
    global current_page


def increase_page_number():
    global current_page
    global pages_array
    if current_page < 15:
        current_page += 1
        if current_page < 10:
            for z in pages_array:
                if z[6:7] == str(current_page):
                    myLabel.config(text=z)
        if 10 <= current_page <= 15:
            for w in pages_array:
                if w[5:7] == str(current_page):
                    myLabel.config(text=w)


# create a button widget and attached
# with counter function
myButton = Button(root, text="Click", command=decrease_page_number)

# create a Label widget
# Initial Label widget content
myLabel = Label(root, text="Hello GitHub")

for x in pages_array:
    print(x[5:7])

print("---------")
for x in pages_array:
    print(x[6:7])

myLabel.pack(pady=20)
myButton.pack(pady=20)

root.mainloop()
