# Handwritten Digit Recognition using Convolutional Neural Network (CNN)

This project implements a Convolutional Neural Network (CNN) to classify handwritten digits from the MNIST dataset.

## Libraries Used:

- **TensorFlow**: Utilized for constructing and training the CNN model.
- **scikit-learn**: Employed for model evaluation and computation of metrics like accuracy, confusion matrix, and classification report.
- **matplotlib**: Utilized for data visualization.

## Data Preparation:

The MNIST dataset is accessed and loaded through the `mnist.load_data()` function from TensorFlow's Keras API. Subsequently, the data undergoes reshaping and normalization to conform to the CNN model's requirements.

## Model Architecture:

The CNN model architecture comprises two convolutional layers succeeded by max-pooling layers, a flattening layer, and two dense layers. The output layer comprises 10 neurons with softmax activation, facilitating multi-class classification.

## Model Training:

The model is compiled with appropriate loss function, optimizer, and evaluation metric settings. It undergoes training on the training data for 25 epochs with a 20% validation split.

## Model Evaluation:

1. **Accuracy**: Model accuracy is computed using scikit-learn's `accuracy_score` function.
2. **Confusion Matrix**: The confusion matrix is visualized using the `confusion_matrix` function from scikit-learn.
3. **Classification Report**: A comprehensive classification report encompassing precision, recall, F1-score, and support metrics is generated via the `classification_report` function from scikit-learn.

## Visualization:

1. **Training History**: Training and validation loss, as well as training and validation accuracy, are plotted across epochs using matplotlib.
2. **Example Predictions**: Several example predictions from the test set are showcased alongside their predicted and true labels.

## File Structure:

- `Digit_Recogniser.ipynb`: Jupyter Notebook containing the complete code.
- `Digit_Recogniser.py`: Python script housing the same code as in the notebook.
- `app.py`: Flask application code for digit recognition using the trained model.
- `generateModel.py`: Script for building the model for digit recognition.
- `templates`: Directory containing HTML templates for the Flask web application.
- `data`: Directory potentially storing the MNIST dataset.
- `build` and `dist`: Directories possibly associated with project build and distribution processes.

---