from tkinter import Tk, Label
from PIL import Image, ImageTk
from cairo import ImageSurface, Context, FORMAT_ARGB32


class ExampleGui(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        w, h = 800, 600

        self.geometry("{}x{}".format(w, h))

        self.surface = ImageSurface(FORMAT_ARGB32, w, h)
        self.context = Context(self.surface)

        # Draw something
        self.context.scale(w, h)
        self.context.rectangle(0, 0, 1, 1)
        self.context.set_source_rgba(1, 0, 0, 0.8)
        self.context.fill()

        self._image_ref = ImageTk.PhotoImage(Image.frombuffer("RGBA", (w, h), self.surface.get_data(), "raw", "BGRA", 0, 1))

        self.label = Label(self, image=self._image_ref)
        self.label.pack(expand=True, fill="both")

        self.mainloop()


if __name__ == "__main__":
    ExampleGui()