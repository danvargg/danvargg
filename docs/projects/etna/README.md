## Deep Learning System for Evaluation and Monitoring of Multiple Sclerosis (MS)

![Python](https://img.shields.io/badge/-Python-000000?style=flat&logo=Python)
![coremltools](https://img.shields.io/badge/-coremltools-000000?style=flat&logo=Coremltools)
![Numpy](https://img.shields.io/badge/-Numpy-000000?style=flat&logo=Numpy)
![Scikit-Learn](https://img.shields.io/badge/-Scikit.Learn-000000?style=flat&logo=Scikit-Learn)
![Keras](https://img.shields.io/badge/-Keras-000000?style=flat&logo=Keras)
![Tensorflow](https://img.shields.io/badge/-Tensorflow-000000?style=flat&logo=Tensorflow)
![OpenCV](https://img.shields.io/badge/-OpenCV-000000?style=flat&logo=OpenCV)
![Scipy](https://img.shields.io/badge/-Scipy-000000?style=flat&logo=Scipy)
![Pandas](https://img.shields.io/badge/-Pandas-000000?style=flat&logo=Pandas)

> This a generalized version of the project. The specific code, architecture, and data are property of the client and 
cannot be fully shared.

A deep learning eye-tracking system for [Innodem Neurosciences](https://innodemneurosciences.com/) to aid with the 
evaluation and monitoring of neurological disorders. The system powers the [ETNA-NDHC-MS](
https://apps.apple.com/us/app/etna-ndhc-ms/id1575499467) mobile application. 
This project is an iteration of the [Deep Learning System for Eye Gaze Tracking](
https://github.com/danvargg/danvargg/blob/main/docs/projects/pigio/README.md) project. The data flow in both projects is 
similar, but the model architecture and training process are different.

The `ETNA-NDHC-MS` mobile application is designed to record eye movements in healthy control participants during visual 
tests presented on the iPad to help investigate the link between eye movements and disease progression in patients with 
Multiple Sclerosis (MS). To do so, the application makes use of `Innodem Neurosciences'` patented eye-tracking technology 
using the iPad's camera.

### Business Problem

The goal was to develop a system that could record patients' eye movements during visual tests presented on screen. 
The system had to be able to run in real-time on the iPad, providing precise predictions for eye movement signal 
processing and analysis.

### Implementation

<img src="https://github.com/danvargg/danvargg/blob/main/docs/projects/pigio/images/data_flow.png">

#### 1. Data Collection and Processing

The data was a collection of artificially generated videos of the users faces and stimuli coordinates. The stimuli
coordinates were generated using a predefined pattern on the screen. The stimuli pattern was designed to cover the 
entire screen and to be presented in a random order.

The resulting synthetic video data (and `.json` metadata) was then processed to crop both eyes regions and facial 
landmarks. The face crop, eyes crops and facial landmarks served as input features for the model and the stimuli 
coordinates as the output for training. These features were processed using `mediapipe`'s facial landmark detector on 
the server and `ARKit`'s facial landmark detector on the iPad.

#### 2. Model Architecture

The model architecture was an improved `Residual Neural Network (ResNet)` inspired by [Eye Tracking for Everyone](
https://arxiv.org/abs/1606.05814).

<img src="https://github.com/danvargg/danvargg/blob/main/docs/projects/etna/images/etna_resnet.png">

Each input `ResNet` model was a `pre-trained` image classifier with the last layer removed. The model was then concatenated 
with multiple dense layers and a final regression layer.

This architecture was unit tested to ensure all layers of the model were compatible with Apple's `Apple Neural Engine
(ANE)` and could run on the iPad in real-time.

#### 3. Model Training

The model was trained using `Tensorflow 2.x` on `AWS EC2` instances with multiple `Nvidia Tesla V100` GPUs.
The generated synthetic data was used to train the model and then predict the stimuli coordinates on real users.
The model training was monitored and evaluated through [Weights & Biases](https://wandb.ai/site).

#### 4. Model Deployment

The trained model checkpoint was converted to `CoreML` and with the user of `coremltools` and deployed to the iOS mobile 
application. This model served as a feature extractor.

#### 5. Model Serving

Once the application was downloaded and installed by the user, the model was calibrated (tuned) to the user's eyes.
This tuning was done by the user following a predefined stimuli pattern on the screen. The model's embeddings 
(last dense layer predictions) were then sent to a server where a fine-tuning cycle was performed:

- The model's embeddings served as input features for a tuning `regressor` and the stimuli's coordinates served as 
outputs once again. 
- The trained regressor was evaluated and converted with `coremltools` to a `CoreML` model.
- The converted model was sent back to the application and used for eye gaze tracking in conjunction with the feature 
extractor model.

This fine-tuning allowed the model to provide more accurate and personalized eye gaze predictions to the user's eyes.

### Business Results

The deep learning system allowed the business to record precise eye movements in real-time during every visual test 
presented on screen. The business was able to acquire precise eye movement signals to evaluate and monitor neurological 
disorders over time.
