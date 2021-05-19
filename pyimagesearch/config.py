# import the necessary packages
import os

# define the path to the training and testing XML files
TRAIN_PATH = os.path.join("ibug_300W_large_face_landmark_dataset",
                          "labels_ibug_300W_train_eyes.xml")
TEST_PATH = os.path.join("ibug_300W_large_face_landmark_dataset",
                         "labels_ibug_300W_test_eyes.xml")

# define the path to the temporary model file
TEMP_MODEL_PATH = "temp.dat"

# define the path to the output CSV file containing the results of
# our experiments
CSV_PATH = "trials.csv"

# define the path to the example image we'll be using to evaluate
# inference speed using the shape predictor
IMAGE_PATH = "image_0237_mirror.jpg"

# define the number of threads/cores we'll be using when trianing our
# shape predictor models
PROCS = -1

# define the maximum number of trials we'll be performing when tuning
# our shape predictor hyperparameters
MAX_TRIALS = 100
