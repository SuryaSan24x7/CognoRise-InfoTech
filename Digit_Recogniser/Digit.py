import tkinter as tk
from tkinter import Button, Label, filedialog
from PIL import Image, ImageTk
import numpy as np
import torch
from torchvision import transforms
import torch.nn as nn
import torch.nn.functional as F
import cv2

# Define the CNN model architecture
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load the trained model
model_cnn = CNN()
model_cnn.load_state_dict(torch.load("mnist_cnn.pth", map_location=torch.device('cpu')))
model_cnn.eval()

# Define transformation to preprocess the image
transform = transforms.Compose([transforms.Grayscale(num_output_channels=1),
                                transforms.Resize((28, 28)),
                                transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,))])

# Function to recognize the digit
def recognize_digit():
    img = Image.open(image_path)
    img = transform(img)
    with torch.no_grad():
        output = model_cnn(img.unsqueeze(0))
        pred = torch.argmax(output, 1)
        result_label.config(text=f"Predicted Digit: {pred.item()}")

# Function to upload image
def upload_image():
    global image_path
    image_path = filedialog.askopenfilename()
    img = Image.open(image_path)
    img.thumbnail((200, 200))
    img = ImageTk.PhotoImage(img)
    uploaded_label.configure(image=img)
    uploaded_label.image = img


# Initialize the GUI
root = tk.Tk()
root.title("Digit Recognition")
root.geometry("300x400")

upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

uploaded_label = Label(root)
uploaded_label.pack()

recognize_button = Button(root, text="Recognize Digit", command=recognize_digit)
recognize_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
