from flask import Flask, render_template, request, redirect
import torch
from torchvision import transforms
from PIL import Image
import io

app = Flask(__name__)

# CNN model definition
class CNN(torch.nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.pool = torch.nn.MaxPool2d(2, 2)
        self.conv2 = torch.nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = torch.nn.Linear(64 * 7 * 7, 128)
        self.fc2 = torch.nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(torch.nn.functional.relu(self.conv1(x)))
        x = self.pool(torch.nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = torch.nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Load the trained model
model_cnn = CNN()
model_cnn.load_state_dict(torch.load("mnist_cnn.pth", map_location=torch.device('cpu')))
model_cnn.eval()

# Define transformation to preprocess the image
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            image_bytes = file.read()
            img = Image.open(io.BytesIO(image_bytes))
            img = transform(img)
            with torch.no_grad():
                output = model_cnn(img.unsqueeze(0))
                predicted_digit = torch.argmax(output, 1).item()
            return render_template("result.html", digit=predicted_digit)
    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
