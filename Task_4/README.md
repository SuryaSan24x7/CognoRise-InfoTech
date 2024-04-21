# Handwritten Digit Recognition using Convolutional Neural Network (CNN)

This code is an implementation of a Convolutional Neural Network (CNN) for classifying handwritten digits from the MNIST dataset.

## Libraries Used:

- **TensorFlow**: Used for building and training the CNN model.
- **scikit-learn**: Used for evaluating the model and computing metrics such as accuracy, confusion matrix, and classification report.
- **matplotlib**: Used for data visualization.

## Data Preparation:

The MNIST dataset is loaded using `mnist.load_data()` function from TensorFlow's Keras API. The data is then reshaped and normalized to fit the CNN model.

## Model Architecture:

The CNN model consists of two convolutional layers followed by max-pooling layers, a flattening layer, and two dense layers. The output layer has 10 neurons with softmax activation, suitable for multi-class classification.

## Model Training:

The model is compiled with the appropriate loss function, optimizer, and evaluation metric. It's then trained on the training data for 25 epochs with 20% validation split.

## Model Evaluation:

1. **Accuracy**: The model's accuracy is calculated using scikit-learn's `accuracy_score` function.
2. **Confusion Matrix**: The confusion matrix is plotted using `confusion_matrix` function from scikit-learn.
3. **Classification Report**: The classification report containing precision, recall, F1-score, and support is generated using `classification_report` function from scikit-learn.

## Visualization:

1. **Training History**: The training and validation loss, as well as training and validation accuracy, are plotted over epochs using matplotlib.
2. **Example Predictions**: Some example predictions from the test set are displayed along with their predicted and true labels.

## File Structure:

- `Digit_Recognition.ipynb`: Jupyter Notebook containing the complete code.
- `Digit_Recognition.py`: Python script containing the same code as in the notebook.
