# create a splash screen, 80% of display screen size, centered,
# displaying a GIF image with needed info, disappearing after 5 seconds
import Tkinter as tk
import os
def runSplashScreen():
    root = tk.Tk()
    # show no frame
    root.overrideredirect(True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry('%dx%d+%d+%d' % (width, height, 0, 0))
    # take a .jpg picture you like, add text with a program like PhotoFiltre
    # (free from http://www.photofiltre.com) and save as a .gif image file
    image_file = 'files/splash.gif'
    assert os.path.exists(image_file)
    # use Tkinter's PhotoImage for .gif files
    image = tk.PhotoImage(file=image_file)
    canvas = tk.Canvas(root, height=height, width=width, bg="white")
    canvas.create_image(width/2, height/2, image=image)
    canvas.pack()
    # show the splash screen for 5000 milliseconds then destroy
    root.after(5000, root.destroy)
    root.mainloop()