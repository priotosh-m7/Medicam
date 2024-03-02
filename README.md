# Medicam - Readme

## Overview

This Django-based web application provides a user-friendly interface for medical image analysis, focusing on brain tumor detection from MRI scans, pneumonia detection from chest scans, and kidney disease classification from kidney scans. Users can upload their scans in JPEG/JPG format and receive results from the respective Convolutional Neural Network (CNN) models. Additionally, the website includes an informative page containing details about the causes, symptoms, and treatments for various brain, kidney, and chest diseases.

## Features

### 1. Brain Tumor Detection

- **Model**: Utilizes a CNN model trained for detecting brain tumors from MRI scans.
- **Input**: Users can upload their MRI scans in JPEG/JPG format.
- **Output**: Provides binary classification results indicating the presence or absence of a brain tumor.
- **Information**: Accessible information about brain tumors and related details.

### 2. Pneumonia Detection

- **Model**: Uses a CNN model to identify pneumonia from chest scans.
- **Input**: Users can upload their chest scans in JPEG/JPG format.
- **Output**: Offers binary classification results for pneumonia presence.
- **Information**: In-depth information on pneumonia causes, symptoms, and treatments.

### 3. Kidney Disease Classification

- **Model**: Employs a CNN model for classifying kidney diseases from kidney scans.
- **Input**: Users can upload their kidney scans in JPEG/JPG format.
- **Output**: Yields classification results indicating the specific kidney disease category.
- **Information**: Detailed information on various kidney diseases.

### 4. Information Page

- **Content**: Provides comprehensive information on causes, symptoms, and treatments for brain tumors, pneumonia, and kidney diseases.
- **Accessibility**: Users can easily navigate and access relevant information about the diseases analyzed on the platform.

## Installation

To run the application locally, follow these steps:

1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Access the web application by visiting [http://localhost:8000/](http://localhost:8000/) in your web browser.

## Usage

1. Visit the web application homepage.

2. Choose the analysis type: Brain Tumor Detection, Pneumonia Detection, or Kidney Disease Classification.

3. Upload the corresponding medical scan in JPEG/JPG format.

4. Click the "Submit" button to initiate the analysis.

5. View the results on the website.

## Credits

- **Developers**: Priotosh Mondal, Harshita Arnala, Kanak Pendse, Siddharth Rawlani, Doulat Lalwani, Om Gaydhane

## Disclaimer

This application is intended for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Consult with a qualified healthcare professional for medical concerns.
