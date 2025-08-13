# Project 5: Crop and Weed Detection

### Project Overview
This project focuses on building a computer vision model to automatically detect and classify crops and weeds in agricultural images. The goal is to develop a system that can be used for precision agriculture, enabling automated spraying of pesticides only on weeds, thereby reducing chemical waste and improving crop health.

### Methodology
The solution was developed using a deep learning approach with the following key technologies:
- **Programming Language:** Python
- **Environment:** Google Colab with GPU acceleration
- **Model:** YOLOv8n (a fast and efficient object detection model)
- **Dataset:** A custom dataset containing 1300 images of sesame crops and various weeds, with annotations in YOLO format.

The project workflow included:
1.  **Data Preparation:** Correctly structuring the dataset and creating a `data.yaml` configuration file.
2.  **Model Training:** Training a pre-trained YOLOv8n model for 50 epochs on the custom dataset.
3.  **Model Evaluation:** Using `val()` to get quantitative metrics and generating plots like `results.png` and a confusion matrix.
4.  **Inference:** Making predictions on unseen images to visually demonstrate the model's performance.

### Key Results
After training for 50 epochs, the model achieved the following performance on the test set:
- **mAP50:** [Insert your mAP50 score here, e.g., 0.8543]
- **Precision:** [Insert your Precision score here, e.g., 0.8211]
- **Recall:** [Insert your Recall score here, e.g., 0.7952]
The model successfully detects and classifies crops and weeds, demonstrating strong performance for this task.

### How to Run the Code
You can run the entire project by opening the provided Colab notebook.
1.  Click on the `Project_5_Crop_Weed_Detection_Colab_Workflow.ipynb` file in this repository.
2.  Click the "Open in Colab" button at the top of the page.
3.  Run the cells sequentially from top to bottom. The notebook will handle all data setup, model training, and evaluation automatically.

### Dataset
The dataset used in this project can be accessed from the following link:
- [Link to your dataset on Google Drive]
