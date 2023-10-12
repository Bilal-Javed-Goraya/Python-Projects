from tkinter import *


window = None
counter = 0


def start():

    global counter

    counterLabel = Label(window, fg='red',
                         bg='pink')


    counterLabel.grid(row=2, column=2,
                      ipadx="25", ipady="25",
                      padx="25", pady="25")

    counter += 1

    counterLabel.config(text=str(counter))


    counterLabel.after(1000, start)

    val = statusField.get()


    if val == "Stop":
        counterLabel.destroy()
        statusField.delete(0, "end")
        counter -= 1


def stop():

    global counter

    counterLabel = Label(window, text=str(counter),
                         fg='red', bg='black')

    counterLabel.grid(row=2, column=2,
                      ipadx="25", ipady="25",
                      padx="25", pady="25")

    statusField.insert(0, "Stop")



def reset():

    global counter

    counter = 0

    counterLabel = Label(window, text=str(counter),
                         fg='black', bg='green')

    counterLabel.grid(row=2, column=2,
                      ipadx="25", ipady="25",
                      padx="25", pady="25")


if __name__ == "__main__":

    window = Tk()

    window.configure(background='light green')

    window.geometry("300x200")


    window.title("Counter GUI")

    counterLabel = Label(window, text=str(counter),
                         fg='black', bg='green')

    counterLabel.grid(row=2, column=2,
                      ipadx="25", ipady="25",
                      padx="25", pady="25")

    startButton = Button(window, text="Start",
                         bg="red", fg="black",
                         command=start)

    startButton.grid(row=3, column=1,
                     padx="25", ipadx="10")

    stopButton = Button(window, text="Stop",
                        bg="red", fg="black",
                        command=stop)

    stopButton.grid(row=3, column=2,
                    ipadx="10")

    resetButton = Button(window, text="Reset",
                         bg="red", fg="black",
                         command=reset)


    resetButton.grid(row=3, column=3,
                     ipadx="10")


    statusField = Entry(window)

    window.mainloop()
