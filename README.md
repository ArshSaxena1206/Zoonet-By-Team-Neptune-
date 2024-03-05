# Zoonet
This  project endeavors to bring out the approach of electronic animal idenƟficaƟon with employing of  computer vision and deep learning. The basic aim is to create a system that will intelligently label the  animals in an image or video to deliver the correct name of the species.Using the advancements in computer vision and deep learning algorithms, ZooNet can identify and classify a wide range of animal species from visual sources such as images.. Whether you're a wildlife enthusiast, researcher, or conservationist, ZooNet provides a powerful tool to monitor and protect wildlife populations.
## Description:
A CNN model for the detection of a variety of animal species which are captured with the help of the mobile application. We are making predictions in real-time, as the animal comes in front of the camera, each frame would be sent to the system where our model will produce the output within a few micro-seconds.
Project Consists of the following subtask:
1. Data Exploration and Collection
2. Dataset Creation
3. Data Preprocessing
4. Image Preprocessing
5. Model Creation
6. Model Training with Optimization and Enhancement
7. Using a Trained model with Computer Vision Techniques
We collected various datasets of images of various animal species which was present on Kaggle, from their by the help of kaggle api key imported these datasets to our Google Colab notebook and did some processing and merged them to make a single dataset then divided whole dataset into train and test dataset. By the help of Keras framework we did image preprocessing on batches of dataset. Then these batches of dataset was applied to our CNN model and based on that network, we made our model learn the features of images and later on classify animal images into classes.
## Data Sources:
1. https://www.kaggle.com/biancaferreira/african-wildlife
2. https://www.kaggle.com/kdnishanth/animal-classification
3. https://www.kaggle.com/viswatejag/animal-detection-small-dataset
4. https://www.kaggle.com/jerrinbright/cheetahtigerwolf 
