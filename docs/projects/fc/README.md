## Deep Learning System for Human Activity Recognition (Tracking)

![Python](https://img.shields.io/badge/-Python-000000?style=flat&logo=Python)
![Numpy](https://img.shields.io/badge/-Numpy-000000?style=flat&logo=Numpy)
![Scikit-Learn](https://img.shields.io/badge/-Scikit.Learn-000000?style=flat&logo=Scikit-Learn)
![Keras](https://img.shields.io/badge/-Keras-000000?style=flat&logo=Keras)
![Tensorflow](https://img.shields.io/badge/-Tensorflow-000000?style=flat&logo=Tensorflow)
![Android](https://img.shields.io/badge/Android-3DDC84?logo=android&logoColor=white)

> This a generalized version of the project. The specific code, architecture, and data are property of the client and 
cannot be fully shared.

A deep learning system for human activity recognition delivered to [FightCamp](https://joinfightcamp.com/) to track and classify user's 
movement (punches and kicks) during a workout session, in real time, through IMU sensors.

### Business Problem

The goal was to develop a system that allowed users to track and classify their movements during a workout session. 
The system had to be able to run in real-time on the Android-power edge device, while delivering accurate and fast 
predictions on the IMU sensor data.

### Implementation

#### 1. Data Collection and Processing

The data was collected from the IMU sensors (accelerometer and gyroscope) of the user's wearable device, and manually labeled. 
The data raw data was directly fed into the deep learning model for training and inference.
A VAE (Variational Autoencoder) was trained to generate synthetic data to increase the size of the training dataset.

#### 2. Model Architecture

<img src="https://github.com/danvargg/danvargg/blob/main/docs/projects/fc/images/fightcamp-github.jpg">

The model architecture was a `Convolutional Neural Network (CNN)` where the model input was the raw imu data 
(accelerometer and gyroscope) and the output was the user's classified movement.

#### 3. Model Training

The model was trained using `Tensorflow 2.x` on `AWS EC2` instances with multiple `Nvidia Tesla V100` GPUs.
Data augmentation techniques were added during training time to improve the model's generalization.

#### 4. Model Deployment

The trained model checkpoint was converted to `TensorflowLite` and deployed to the Android edge device.

#### 5. Model Serving

The model was served on the Android device using the `TensorflowLite` runtime to classify the user's movements in real-time. 

Furthermore, the model had it's weights quantized (post-conversion) to `16-bit` floating-point numbers to reduce the model's size and 
improve the inference speed.

### Business Results

The deep learning system allowed the business to improve the performance of its activity tracking technology and 
provide a more accurate and personalized experience to its users. The system was able to track and classify the user's 
movements in real-time with high accuracy and low latency.
