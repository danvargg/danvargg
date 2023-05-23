## Recommendation System

![Python](https://img.shields.io/badge/-Python-000000?style=flat&logo=Python)
![AWS](https://img.shields.io/badge/-AWS-000000?style=flat&logo=amazonaws)
![Scikit-Learn](https://img.shields.io/badge/-Scikit.Learn-000000?style=flat&logo=Scikit-Learn)

<img src="https://github.com/danvargg/danvargg/blob/main/docs/projects/auraML/auraml.png">

> This a generalized version of the project. The code, architecture, and data are property of the client and cannot be shared.

A Recommendation System for [Aura Health](https://www.aurahealth.io/), an audio streaming service for wellness content, powered by a recommendation system.

### Business Problem

The goal is to choose the best meditation(s) for a user to maximize rating, given input parameters.

### Solution Strategy

For new users a `Collaborative filtering` model was implemented through an `SVD` algorithm. For existing users, a `Content-based filtering` model was implemented through a `Random Forest` algorithm, after also being tested through a `KNN` algorithm.
- Machine Learning (KNN)
- Machine Learning (Random Forest)

### Implementation

A `Random Forest Regressor` was trained on the `meditation` dataset to predict the rating of a meditation given the input parameters. The model was deployed on `AWS Lambda` and `AWS API Gateway` to be used as a REST API.

The output was  an array of `meditationID` in order of recommendation (highest predicted rating first)

### Business Results

Recommendations in near real-time for users to choose their next meditation.
