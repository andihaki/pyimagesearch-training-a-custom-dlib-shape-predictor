https://www.pyimagesearch.com/2019/12/16/training-a-custom-dlib-shape-predictor/

# train dataset
python parse_xml.py \
	--input ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train.xml \
	--output ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train.xml

# test dataset
python parse_xml.py \
	--input ibug_300W_large_face_landmark_dataset/labels_ibug_300W_test.xml \
	--output ibug_300W_large_face_landmark_dataset/labels_ibug_300W_test_lips.xml

# train
python train_shape_predictor.py \
	--training ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train_lips.xml \
	--model lips_predictor.dat

# evaluate 
## train
python evaluate_shape_predictor.py --predictor lips_predictor.dat \
	--xml ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train_lips.xml
	
python evaluate_shape_predictor.py --predictor shape_predictor_68_face_landmarks.dat \
	--xml ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train.xml

## test
python evaluate_shape_predictor.py --predictor lips_predictor.dat \
	--xml ibug_300W_large_face_landmark_dataset/labels_ibug_300W_test_lips.xml

python evaluate_shape_predictor.py --predictor shape_predictor_68_face_landmarks.dat \
	--xml ibug_300W_large_face_landmark_dataset/labels_ibug_300W_test.xml

# predict lips
python predict_lips.py --shape-predictor lips_predictor.dat

# other dataset
- aflw: 21 points https://www.tugraz.at/institute/icg/research/team-bischof/lrs/downloads/aflw/
- UTKFace: 68 points https://susanqq.github.io/UTKFace/
- aflw2k3d: 68 points https://www.tensorflow.org/datasets/catalog/aflw2k3d
- helen: 29 points http://www.f-zhou.com/fa_code.html
- RMWB: 98 point https://keqiangsun.github.io/projects/FAB/RWMB.html
- JDlandmark: 106 point https://facial-landmarks-localization-challenge.github.io/

kazemi
cascade T = 10, K = 500, tree depth = 5, P = 400 piksel
tree_depth: 5
nu: 0.05
cascade_depth: 10
feature_pool_size: 400
num_test_splits: 20
http://dlib.net/train_shape_predictor_ex.cpp.html
oversampling_amount: 300
oversampling_translation_jitter: