"""Utility for downloading and managing models"""
import os
import urllib.request
import bz2

class ModelDownloader:
    def __init__(self):
        self.model_url = "https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2"
        self.model_path = "shape_predictor_68_face_landmarks.dat"
        self.compressed_path = f"{self.model_path}.bz2"
    
    def download_if_needed(self):
        """Download and extract the model if it doesn't exist"""
        if not os.path.exists(self.model_path):
            print("Downloading facial landmarks predictor model...")
            self._download_model()
            self._extract_model()
            self._cleanup()
            print("Model downloaded and extracted successfully!")
        else:
            print("Model file already exists!")
    
    def _download_model(self):
        """Download the compressed model file"""
        urllib.request.urlretrieve(self.model_url, self.compressed_path)
    
    def _extract_model(self):
        """Extract the bz2 compressed model file"""
        with bz2.BZ2File(self.compressed_path) as fr, open(self.model_path, "wb") as fw:
            fw.write(fr.read())
    
    def _cleanup(self):
        """Remove the compressed file after extraction"""
        if os.path.exists(self.compressed_path):
            os.remove(self.compressed_path)