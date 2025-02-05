with open("diary.txt", "w") as fp:
    while True:
        text=input("How are you doing today? (type q to quit)")
        if text == "q":
            break
        fp.write(f"{text}\n") # this is the same as line below
        # fp.write(text + "\n")