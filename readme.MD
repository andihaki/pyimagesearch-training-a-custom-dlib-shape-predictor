https://www.pyimagesearch.com/2019/12/16/training-a-custom-dlib-shape-predictor/

# train model
python parse_xml.py \
	--input ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train.xml \
	--output ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train_eyes.xml

# test model
python parse_xml.py \
	--input ibug_300W_large_face_landmark_dataset/labels_ibug_300W_test.xml \
	--output ibug_300W_large_face_landmark_dataset/labels_ibug_300W_test_eyes.xml

# train
python train_shape_predictor.py \
	--training ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train_eyes.xml \
	--model eye_predictor.dat

# evaluate 
## train
python evaluate_shape_predictor.py --predictor eye_predictor.dat \
	--xml ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train_eyes.xml

## test
python evaluate_shape_predictor.py --predictor eye_predictor.dat \
	--xml ibug_300W_large_face_landmark_dataset/labels_ibug_300W_test_eyes.xml

# predict eye
python predict_eyes.py --shape-predictor eye_predictor.dat