# eye_predictor_v1.dat
options.tree_depth = 5
options.nu = 0.05
options.cascade_depth = 10
options.feature_pool_size = 400
options.num_test_splits = 50
options.oversampling_amount = 300
options.oversampling_translation_jitter = 0.1

(dlib3) ➜  training-dlib git:(tunning) ✗ python evaluate_shape_predictor.py --predictor eye_predictor_v1.dat \

[INFO] evaluating shape predictor...
[INFO] error: 7.665492339032554