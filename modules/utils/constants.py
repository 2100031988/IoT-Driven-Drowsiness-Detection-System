"""Constants used throughout the application"""

# Eye aspect ratio thresholds
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 20

# Facial landmarks indices
LEFT_EYE_START = 36
LEFT_EYE_END = 42
RIGHT_EYE_START = 42
RIGHT_EYE_END = 48

# Display settings
WINDOW_NAME = "Drowsiness Detection"
FONT = "FONT_HERSHEY_SIMPLEX"
FONT_SCALE = 0.7
FONT_COLOR = (0, 0, 255)
FONT_THICKNESS = 2

# Model paths
SHAPE_PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
MODEL_URL = "https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2"