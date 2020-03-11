#!/usr/bin/env bash

cd ~/Source/speaker-follower/

# generate more training instructions
tasks/R2R/data_augmentation_from_speaker.py --speaker_model_prefix tasks/R2R/snapshots/release/speaker_final_release \
--pred_results_output_file tasks/R2R/data/R2R_argmax \
--pred_splits train \
--seed 10 --feedback argmax

tasks/R2R/data_augmentation_from_speaker.py --speaker_model_prefix tasks/R2R/snapshots/release/speaker_final_release \
--pred_results_output_file tasks/R2R/data/R2R_argmax \
--pred_splits train \
--seed 10 --feedback sample

tasks/R2R/data_augmentation_from_speaker.py --speaker_model_prefix tasks/R2R/snapshots/release/speaker_final_release \
--pred_results_output_file tasks/R2R/data/R2R_argmax \
--pred_splits train \
--seed 20 --feedback sample

# generate more training instructions by beam_search
tasks/R2R/data_augmentation_from_speaker.py --speaker_model_prefix tasks/R2R/snapshots/release/speaker_final_release \
--pred_results_output_file tasks/R2R/data/R2R_argmax \
--pred_splits data_augmentation_paths \
--seed 10 --feedback argmax \
--beam_size 5

# Using "/home/nav/Source/speaker_follower/tasks/R2R/data_augmentation_from_speaker.py to generate instructions
#=============================================================================================================
# R2R_argmax
#
#"image_feature_type": ["mean_pooled"], "image_attention_size": null, "image_feature_datasets": ["imagenet"], "bottom_up_detections": 20, "bottom_up_detection_embedding_size": 20, "downscale_convolutional_features": false, "feedback_method": "sample", "bidirectional": false, "n_iters": 20000, "use_pretraining": false, "pretrain_splits": [], "n_pretrain_iters": 50000, "no_save": false, "use_train_subset": false, "use_test_set": false, "speaker_model_prefix": "tasks/R2R/snapshots/release/speaker_final_release", "pred_results_output_file": "tasks/R2R/data/R2R_argmax", "batch_size": 20, "pred_splits": ["data_augmentation_paths"], "seed": 10, "feedback": "argmax", "follower_model_prefix": null, "rational_speaker_weights": null, "rational_speaker_n_candidates": 40, "pdb": false, "ipdb": false, "no_cuda": false}
#
#Loading image features from img_features/ResNet-152-imagenet.tsv
#Loading navigation graphs for 61 scans
#R2RBatch loaded with 14039 instructions, using splits: train
#Using GloVe embedding
#Loading navigation graphs for 60 scans
#R2RBatch loaded with 178300 instructions, using splits: data_augmentation_paths
#ix 0 / 178300/home/nav/anaconda3/lib/python3.7/site-packages/torch/nn/_reduction.py:49: UserWarning: size_average and reduce args will be deprecated, please use reduction='none' instead.
#  warnings.warn(warning.format(ret))
#/home/nav/anaconda3/lib/python3.7/site-packages/torch/nn/_reduction.py:49: UserWarning: size_average and reduce args will be deprecated, please use reduction='mean' instead.
#  warnings.warn(warning.format(ret))
#ix 178300 / 178300Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#pred literal_speaker data_augmentation_paths model_score	-20.118176956805232
#pred literal_speaker data_augmentation_paths bleu	0.0
#pred literal_speaker data_augmentation_paths unpenalized_bleu	0
#=============================================================================================================
#R2R sample seed10
#
#{"image_feature_type": ["mean_pooled"], "image_attention_size": null, "image_feature_datasets": ["imagenet"], "bottom_up_detections": 20, "bottom_up_detection_embedding_size": 20, "downscale_convolutional_features": false, "feedback_method": "sample", "bidirectional": false, "n_iters": 20000, "use_pretraining": false, "pretrain_splits": [], "n_pretrain_iters": 50000, "no_save": false, "use_train_subset": false, "use_test_set": false, "speaker_model_prefix": "tasks/R2R/snapshots/release/speaker_final_release", "pred_results_output_file": "tasks/R2R/data/R2R_sample_seed10", "batch_size": 20, "pred_splits": ["data_augmentation_paths"], "seed": 10, "feedback": "sample", "follower_model_prefix": null, "rational_speaker_weights": null, "rational_speaker_n_candidates": 40, "pdb": false, "ipdb": false, "no_cuda": false}
#
#Loading image features from img_features/ResNet-152-imagenet.tsv
#Loading navigation graphs for 61 scans
#R2RBatch loaded with 14039 instructions, using splits: train
#Using GloVe embedding
#Loading navigation graphs for 60 scans
#R2RBatch loaded with 178300 instructions, using splits: data_augmentation_paths
#ix 0 / 178300/home/nav/Source/speaker_follower/tasks/R2R/speaker.py:172: UserWarning: Implicit dimension choice for softmax has been deprecated. Change the call to include dim=X as an argument.
#  probs = F.softmax(logit)    # sampling an action from model
#/home/nav/anaconda3/lib/python3.7/site-packages/torch/nn/_reduction.py:49: UserWarning: size_average and reduce args will be deprecated, please use reduction='none' instead.
#  warnings.warn(warning.format(ret))
#/home/nav/anaconda3/lib/python3.7/site-packages/torch/nn/_reduction.py:49: UserWarning: size_average and reduce args will be deprecated, please use reduction='mean' instead.
#  warnings.warn(warning.format(ret))
#ix 178300 / 178300Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#pred literal_speaker data_augmentation_paths model_score	-60.19590198261445
#pred literal_speaker data_augmentation_paths bleu	0.0
#pred literal_speaker data_augmentation_paths unpenalized_bleu	0
#=============================================================================================================
#R2R sample seed20
#
#{"image_feature_type": ["mean_pooled"], "image_attention_size": null, "image_feature_datasets": ["imagenet"], "bottom_up_detections": 20, "bottom_up_detection_embedding_size": 20, "downscale_convolutional_features": false, "feedback_method": "sample", "bidirectional": false, "n_iters": 20000, "use_pretraining": false, "pretrain_splits": [], "n_pretrain_iters": 50000, "no_save": false, "use_train_subset": false, "use_test_set": false, "speaker_model_prefix": "tasks/R2R/snapshots/release/speaker_final_release", "batch_size": 20, "pred_results_output_file": "tasks/R2R/data/R2R_sample_seed20", "pred_splits": ["data_augmentation_paths"], "seed": 20, "feedback": "sample", "follower_model_prefix": null, "rational_speaker_weights": null, "rational_speaker_n_candidates": 40, "pdb": false, "ipdb": false, "no_cuda": false}
#
#Loading image features from img_features/ResNet-152-imagenet.tsv
#Loading navigation graphs for 61 scans
#R2RBatch loaded with 14039 instructions, using splits: train
#Using GloVe embedding
#Loading navigation graphs for 60 scans
#R2RBatch loaded with 178300 instructions, using splits: data_augmentation_paths
#ix 0 / 178300/home/nav/Source/speaker_follower/tasks/R2R/speaker.py:172: UserWarning: Implicit dimension choice for softmax has been deprecated. Change the call to include dim=X as an argument.
#  probs = F.softmax(logit)    # sampling an action from model
#/home/nav/anaconda3/lib/python3.7/site-packages/torch/nn/_reduction.py:49: UserWarning: size_average and reduce args will be deprecated, please use reduction='none' instead.
#  warnings.warn(warning.format(ret))
#/home/nav/anaconda3/lib/python3.7/site-packages/torch/nn/_reduction.py:49: UserWarning: size_average and reduce args will be deprecated, please use reduction='mean' instead.
#  warnings.warn(warning.format(ret))
#ix 178300 / 178300Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#Use of uninitialized value in division (/) at scripts/multi-bleu.perl line 139, <STDIN> line 178300.
#pred literal_speaker data_augmentation_paths model_score	-60.08752602631499
#pred literal_speaker data_augmentation_paths bleu	0.0
#pred literal_speaker data_augmentation_paths unpenalized_bleu	0