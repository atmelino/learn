from tkinter import Tk, Button


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("Hello World")

        self.button = Button(text="My simple app.")
        self.button.bind("event", self.handle_button_press)

    # entry.bind('<event>', evaluate)

        self.button.pack()

    def handle_button_press(self, event):
        self.destroy()


# Start the event loop.
window = Window()
window.mainloop()