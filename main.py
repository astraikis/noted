import os
from datetime import datetime


def get_daily_note():
    # make .config directory
    if not os.path.exists("./.config"):
        os.makedirs("./.config")

    # make save location file
    if not os.path.exists("./.config/save-location.txt"):
        file = open("./.config/save-location.txt", "x")

    # get save location
    save_location_file = open("./.config/save-location.txt", "r")
    save_location = save_location_file.read()

    print("saving note to: " + save_location)
    change = input("change? [y/n] ")

    # change save location
    if change == "y":
        save_location = input("\nlocation: ")
        file = open("./.config/save-location.txt", "w")
        file.write(save_location)

    # create save location dir if needed
    if not os.path.exists(save_location):
        os.makedirs(save_location)

    # create daily note file
    daily_note = open(save_location + "/" + date + ".md", "a")
    num_lines = len(open(save_location + "/" + date + ".md", "r").readlines())

    # if new daily note
    if num_lines == 0:
        daily_note.write("## " + date + "\n")
        daily_note.write("---\n")

    return daily_note


# get date and time
today = datetime.today()
date = today.strftime("%b-%d-%Y")
now = datetime.now()
time = now.strftime("%H:%M:%S")

print(date)
print(time + "\n")

daily_note = get_daily_note()

# get feeling and note
feeling = input("\nhow are you feeling? ")
note = input("\nwhat's on your mind?\n")

# write to note
daily_note.write("\n### " + time + "\n\n")
daily_note.write("feeling: " + feeling + "  \n")
daily_note.write(note + "\n")
