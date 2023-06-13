## Deep Learning System for Eye Gaze Tracking

![Python](https://img.shields.io/badge/-Python-000000?style=flat&logo=Python)
![coremltools](https://img.shields.io/badge/-coremltools-000000?style=flat&logo=Coremltools)
![Numpy](https://img.shields.io/badge/-Numpy-000000?style=flat&logo=Numpy)
![Scikit-Learn](https://img.shields.io/badge/-Scikit.Learn-000000?style=flat&logo=Scikit-Learn)
![Keras](https://img.shields.io/badge/-Keras-000000?style=flat&logo=Keras)
![Tensorflow](https://img.shields.io/badge/-Tensorflow-000000?style=flat&logo=Tensorflow)
![OpenCV](https://img.shields.io/badge/-OpenCV-000000?style=flat&logo=OpenCV)

> This a generalized version of the project. The specific code, architecture, and data are property of the client and 
cannot be fully shared.

A deep learning eye-tracking system for [Innodem Neurosciences](https://innodemneurosciences.com/) to help patients 
communicate using only eye movements.

The system powers both the [Pigio™: Gaze-to-Speech](
https://apps.apple.com/us/app/pigio-gaze-to-speech/id1399641303) and the [Pigio™ ICU: Gaze-to-Speech](
https://apps.apple.com/us/app/pigio-icu-gaze-to-speech/id1466945385) applications.
These Software-as-a-Medical-Device (SaaMD) applications allow Intensive Care Unit patients (conscious but intubated 
or paralyzed) to communicate through eye movements.

### Business Problem

The goal was to develop a system that allowed patients to use the device using only eye movements. The system had to be 
able to run in real-time on the iPad and be robust to changes in lighting conditions and patient appearance 
(e.g., facial hair, glasses, etc.).

### Implementation

<img src="https://github.com/danvargg/danvargg/blob/main/docs/projects/pigio/images/data_flow.png">

#### 1. Data Collection and Processing

The data was collected through the iPad's camera. The user was asked to follow a stimuli on the screen for a determined 
amount of frames.

The resulting video (and `.json` metadata) of the user's face was then processed to crop both eyes regions and facial 
landmarks. The eye crops and facial landmarks served as input features for the model and the stimuli coordinates as 
the output for training. These features were processed using `dlib`'s facial landmark detector.

#### 2. Model Architecture

The model architecture was a simplified `Convolutional Neural Network (CNN)` inspired by [Eye Tracking for Everyone](
https://arxiv.org/abs/1606.05814), where the inputs were each eye crop and the outputs are the eye gaze coordinates.

<img src="https://github.com/danvargg/danvargg/blob/main/docs/projects/pigio/images/nn_arch.png">

#### 3. Model Training

The model was trained using `Tensorflow 2.x` on `AWS EC2` instances with multiple `Nvidia Tesla V100` GPUs.
Data augmentation techniques (cropping, flipping, rotation, etc.) were added during training time to improve the model's generalization.

#### 4. Model Deployment

The trained model checkpoint was converted to `CoreML` and with the user of `coremltools` and deployed to the iOS mobile 
application. This model served as a feature extractor.

#### 5. Model Serving

Once the application was downloaded and installed by the user, the model was calibrated (tuned) to the user's eyes.
This tuning was done by the user following a predefined stimuli pattern on the screen. The model's predictions were then 
sent to a server where a fine-tuning cycle was performed:

- The model's predictions served as input features for a tuning `regressor` and the stimuli's coordinates served as 
outputs once again. 
- The trained regressor was evaluated and converted with `coremltools` to a `CoreML` model.
- The converted model was sent back to the application and used for eye gaze tracking in conjunction with the feature 
extractor model.

This fine-tuning allowed the model to provide more accurate and personalized eye gaze predictions to the user's eyes.

Furthermore, the model had it's weights quantized (post-conversion) to `16-bit` floating-point numbers to reduce the model's size and 
improve the inference speed.

### Business Results

The deep learning system allowed the business to improve the performance of its eye  tracking technology to a level 
that is comparable or better than existing infrared solutions.
