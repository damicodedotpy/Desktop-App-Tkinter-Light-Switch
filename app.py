from tkinter import Tk, Label, Frame
from tkinter.ttk import Button, Style
from PIL import Image, ImageTk

# Initialize the main application window
app = Tk()
style = Style()

# Set the geometry of the window and the theme
app.geometry('500x250')
app.resizable(False, False)
style.theme_use("clam")

# Function to handle the 'ON' button click
def on():
    # Disable the 'ON' button and enable the 'OFF' button
    onButton['state'] = 'disabled'
    offButton['state'] = 'normal'  # Use 'normal' instead of 'active' for consistency
    # Load and display the 'on' image
    image = Image.open('./on.png').resize((250, 250))
    tkImage = ImageTk.PhotoImage(image)
    # Configure the image to be showed on the Label
    imageLabel.config(image=tkImage)
    imageLabel.image = tkImage  # Keep a reference to avoid garbage collection while Label keeps needing to show the image

# Function to handle the 'OFF' button click
def off():
    # Disable the 'OFF' button and enable the 'ON' button
    offButton['state'] = 'disabled'
    onButton['state'] = 'normal'  # Use 'normal' instead of 'active' for consistency
    # Load and display the 'off' image
    image = Image.open('./off.png').resize((250, 250))
    tkImage = ImageTk.PhotoImage(image)
    # Ensure the label is accessible by storing it as an attribute
    imageLabel.config(image=tkImage)
    imageLabel.image = tkImage  # Keep a reference to avoid garbage collection

# Create frames for buttons and images
masterFrame = Frame(app)
buttonsFrame = Frame(masterFrame)
imagesFrame = Frame(masterFrame)
# Create the 'ON' and 'OFF' buttons
onButton = Button(buttonsFrame, text='ON', command=on, state='normal')
offButton = Button(buttonsFrame, text='OFF', command=off, state='disabled')
# Create a label for displaying images
imageLabel = Label(imagesFrame)


masterFrame.place(relwidth=1, relheight=1)  # Ocupa todo el espacio de 'app'
buttonsFrame.place(relheight=1, width=250)  # Altura relativa al contenedor, ancho fijo
imagesFrame.place(relx=0.5, relwidth=0.5, relheight=1)  # Comienza en la mitad de 'masterFrame' y ocupa la mitad restante
onButton.place(relx=0.25, rely=0.30)
offButton.place(relx=0.25, rely=0.5)
imageLabel.pack()

# Start the main application loop
app.mainloop()