"""Script to download the facial landmarks predictor model"""
from modules.utils.model_downloader import ModelDownloader

def main():
    downloader = ModelDownloader()
    downloader.download_if_needed()

if __name__ == "__main__":
    main()