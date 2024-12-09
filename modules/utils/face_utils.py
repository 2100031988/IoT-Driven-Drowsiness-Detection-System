"""Facial feature utilities"""
import numpy as np
from scipy.spatial import distance as dist

def get_eye_aspect_ratio(eye_points):
    """Calculate the eye aspect ratio"""
    # Compute euclidean distances between eye landmark points
    A = dist.euclidean(eye_points[1], eye_points[5])
    B = dist.euclidean(eye_points[2], eye_points[4])
    C = dist.euclidean(eye_points[0], eye_points[3])
    
    # Calculate eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

def extract_eye_points(landmarks, start, end):
    """Extract eye landmark points"""
    points = []
    for n in range(start, end):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        points.append((x, y))
    return points