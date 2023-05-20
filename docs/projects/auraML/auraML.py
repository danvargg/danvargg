"""Aura Health ML pipeline architecture diagram."""
from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.firebase.base import Firebase
from diagrams.aws.ml import MachineLearning
from diagrams.aws.integration import ConsoleMobileApplication

with Diagram('auraML', show=True, direction='LR'):
    mobile = ConsoleMobileApplication('Mobile App')
    firebase = Firebase('Firebase')
    lambda_train = Lambda('Model Training')
    lambda_predict = Lambda('Model Inference')
    model = MachineLearning('Trained Model')

    mobile >> firebase >> lambda_train >> model >> lambda_predict >> firebase
    firebase >> mobile
