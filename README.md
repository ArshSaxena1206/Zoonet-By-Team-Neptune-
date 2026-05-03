

[![header](https://capsule-render.vercel.app/api?type=waving&color=2E8B57&height=120§ion=header)](https://capsule-render.vercel.app)

# 🦁 ZooNet — Animal Species Classifier

**CNN-powered real-time animal identification using Computer Vision & Deep Learning**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=black)

*Team Neptune · Hackathon Project*




---

## 📌 Overview

ZooNet is a deep learning system that identifies and classifies animal species from images and video in real-time. Using a custom-trained CNN model, it processes each camera frame within microseconds to deliver accurate species predictions — making it useful for wildlife monitoring, conservation research, and ecological studies.

> Built as a hackathon project by **Team Neptune** using TensorFlow, Keras, and OpenCV.

---

## ✨ Features

- 🔍 **Real-time classification** — processes live camera frames in microseconds
- 🧠 **CNN architecture** — custom-built and trained on merged multi-source datasets
- 🐆 **Multi-species support** — identifies a wide range of animal species
- 📊 **Optimized training** — includes data augmentation, batch preprocessing, and model tuning
- 📱 **Mobile-ready** — designed to integrate with a mobile application capture interface

---

## 🗂️ Project Workflow

| Step | Task |
|------|------|
| 1 | Data Exploration & Collection |
| 2 | Dataset Creation & Merging |
| 3 | Data Preprocessing |
| 4 | Image Preprocessing (Keras ImageDataGenerator) |
| 5 | CNN Model Architecture Design |
| 6 | Model Training with Optimization & Enhancement |
| 7 | Real-time Inference with Computer Vision |

---

## 📊 Training Results




| Metric | Value |
|--------|-------|
| Model | Custom CNN |
| Framework | TensorFlow / Keras |
| Dataset Size | Multi-source merged (Kaggle) |
| Training Split | 80% Train / 20% Test |




**Accuracy & Loss Curves:**

![Accuracy Graph](accuracy%20graph.png)
![Loss Graph](Loss%20graph.png)

---

## 🗃️ Data Sources

| Dataset | Source |
|---------|--------|
| African Wildlife | [Kaggle — biancaferreira](https://www.kaggle.com/biancaferreira/african-wildlife) |
| Animal Classification | [Kaggle — kdnishanth](https://www.kaggle.com/kdnishanth/animal-classification) |
| Animal Detection Small | [Kaggle — viswatejag](https://www.kaggle.com/viswatejag/animal-detection-small-dataset) |
| Cheetah Tiger Wolf | [Kaggle — jerrinbright](https://www.kaggle.com/jerrinbright/cheetahtigerwolf) |

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install tensorflow keras opencv-python numpy pandas matplotlib
```

### Run the Notebook

1. Clone this repository:
```bash
git clone https://github.com/ArshSaxena1206/Zoonet-By-Team-Neptune-.git
cd Zoonet-By-Team-Neptune-
```

2. Open the notebook:
```bash
jupyter notebook Zoonet_Project.ipynb
```

3. To use your own Kaggle datasets, set up your Kaggle API key:
```bash
export KAGGLE_USERNAME=your_username
export KAGGLE_KEY=your_api_key
```



---




[![footer](https://capsule-render.vercel.app/api?type=waving&color=2E8B57&height=120&section=footer&reversal=true)](https://capsule-render.vercel.app)

