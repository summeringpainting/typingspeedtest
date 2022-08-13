from tkinter import Tk, Label, Entry, Button, messagebox, Text
import time
import threading


def start(event):
    """Start the global timer."""
    global running
    if not running:
        running = True
        t = threading.Thread(target=time_thread)
        t.start()


def time_thread():
    """Get text from text box and split it by spaces."""
    """Then divide it by seconds to calculate WPM."""
    global running
    global counter
    global wpm
    a = threading.Thread(target=average)
    a.start()
    while running:
        time.sleep(0.1)
        counter += 0.1
        wps = len(textbox.get("1.0", 'end-1c').split(" ")) / counter
        wpm = wps * 60
        speed.config(text=f"{wpm:.2f} WPM")

avg_list = []


def average():
    """Calculate average based on WPM every two seconds"""
    global running
    global counter
    global wpm
    global avg_list
    while running:
        time.sleep(2)
        avg_list.append(wpm)
        print(avg_list)
    aver = sum(avg_list[:-1]) / (len(avg_list) - 1)
    return aver


def reset():
    """Reset timer and global variables."""
    global running
    global avg_list
    global counter
    running = False
    counter = 0

    messagebox.showinfo(title="AVG WPM",
                        message=average())
    avg_list = []
    textbox.delete('1.0', 'end')
    speed.config(text="0.00 WPM")


window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50, bg="white")

label = Label(text="Type paragraph into text box to get your typing speed",
              bg="white",
              font=("Arial", 14))
label.grid(column=0, row=0)

label2 = Label(text="Income before securities transactions was up 11 percent\n "
                    "from $13.49 million in 1982 to $14.95 million in 1983.\n "
                    "Earnings per share (adjusted for a 10.5 percent stock\n "
                    "dividend distributed on August 26) advanced 10 percent\n "
                    "to $2.39 in 1983 from $2.17 in 1982. Earnings may rise\n "
                    "for 7 years. Hopefully, earnings per share will grow\n "
                    "another 10 percent. Kosy, Klemin, and Bille began\n "
                    "selling on May 23, 1964. Their second store was founded\n "
                    "in Renton on August 3, 1965. From 1964 to 1984, they\n "
                    "opened more than 50 stores through-out the country. As\n "
                    "they expanded, 12 regional offices had to be organized.\n "
                    "Each of these 12 regional offices had to be organized.\n "
                    "Each of these 12 regions employs from 108 to 578 people.\n "
                    "National headquarters employs 1,077 people. Carole owns\n "
                    "118 stores located in 75 cities ranging as far west as\n "
                    "Seattle and as far east as Boston. She owns 46 stores\n "
                    "south of the Mason-Dixon line and 24 stores north of\n "
                    "Denver. Carole buys goods from 89 companies located in\n "
                    "123 countries and all 50 states. Carole started in\n "
                    "business on March 3, 1975. She had less than $6,000 in\n "
                    "capital assets.",
                    width=80)
label2.grid(column=0, row=1, pady=10)

textbox = Text(window, width=80, height=20)
textbox.grid(column=0, row=2, pady=10)
textbox.focus()
textbox.bind("<KeyPress>", start)

button = Button(text="Reset",
                command=reset,
                width=14,
                font=("Arial", 12))

button.grid(sticky='w', column=0, row=3,
            columnspan=2, pady=10)

stop = Button(text="Quit",
              command=window.destroy,
              font=("Arial", 12))

stop.grid(sticky='e', column=0, row=3,
          columnspan=2, pady=10)

speed = Label(text="0.00 WPM")
speed.grid(column=0, row=4)


counter = 0
running = False

window.mainloop()
