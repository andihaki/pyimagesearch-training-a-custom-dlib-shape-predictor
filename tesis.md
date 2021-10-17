paper:
https://www.researchgate.net/publication/264419855_One_Millisecond_Face_Alignment_with_an_Ensemble_of_Regression_Trees

https://www.pyimagesearch.com/2019/12/16/training-a-custom-dlib-shape-predictor/

# train model
python parse_xml.py \
	--input ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train.xml \
	--output ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train_lips.xml

# test model
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

## test
python evaluate_shape_predictor.py --predictor lips_predictor.dat \
	--xml ibug_300W_large_face_landmark_dataset/labels_ibug_300W_test_lips.xml

# predict lips
python predict_lips.py --shape-predictor lips_predictor.dat

# other dataset
- aflw: 21 points https://www.tugraz.at/institute/icg/research/team-bischof/lrs/downloads/aflw/
- UTKFace: 68 points https://susanqq.github.io/UTKFace/
- aflw2k3d: 68 points https://www.tensorflow.org/datasets/catalog/aflw2k3d
- helen: 29 points http://www.f-zhou.com/fa_code.html
- RMWB: 98 point https://keqiangsun.github.io/projects/FAB/RWMB.html
- JDlandmark: 106 point https://facial-landmarks-localization-challenge.github.io/