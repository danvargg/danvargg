"""Aura Health ML pipeline architecture diagram."""
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

from diagrams.aws.compute import Lambda
from diagrams.firebase.base import Firebase

with Diagram('auraML', show=False, direction='LR'):
    Firebase("lb") >> [
        Lambda("worker1"),
    ] >> RDS("events")
