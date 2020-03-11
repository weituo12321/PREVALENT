import json
import sys
import numpy as np

def sample_merge_instruction_files(files, outfile, sample_n):

    merged = {}
    for file in files:
        with open(file,'r') as f:
            paths = json.load(f)
        for path in paths:
            if isinstance(path, str):  # speaker_follower validation data
                path_id = path.split('_')[0]
                path = paths[path]
                if path_id not in merged:
                    merged[path_id] = {'path_id':path_id,
                                       'instructions': [' '.join(path['words'])]}
                else:
                    merged[path_id]['instructions'].append(' '.join(path['words']))
            else:  # normal training data
                path_id = path['path_id']
                if path_id not in merged:
                    merged[path_id] = path
                else:
                    merged[path_id]['instructions'].extend(path['instructions'])

    if sample_n>0:
        for path_id, path in merged.items():
            idx = np.random.choice(len(path['instructions']), sample_n, replace=False)
            merged[path_id]['instructions'] = [path['instructions'][i] for i in idx ]
            assert len( merged[path_id]['instructions']) == len(set( merged[path_id]['instructions']))

    with open(outfile,'w') as outfile:
        json.dump([i[1] for i in merged.items()], outfile, sort_keys=True, indent=4, separators=(',', ':'))


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv)<4:
        exit(1)
    sample_merge_instruction_files(sys.argv[1:-2], sys.argv[-2], int(sys.argv[-1]))
'''  { "distance": xx.x,  "scan": "xxx",  "path_id": xxxx,
    "path": [
      "dfa0373deb9d4e5db88b76c95dc0d6a9",
      "ec360e7b39e1449287ee29a80a55345c" ],  
    "heading": x.xxx,
    "instructions": [
     "Turn around and start to walk down the long pathway of wood floor. Once you are halfway past the bar, turn right and stop at the top of the stairs. "]},
'''
"""
sudo chmod +755 tasks/R2R/data/*

python preprocess/merge_instr.py \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_t0.5_literal_speaker_data_augmentation_paths.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed20_t0.5_literal_speaker_data_augmentation_paths.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed30_t0.5_literal_speaker_data_augmentation_paths.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed40_t0.5_literal_speaker_data_augmentation_paths.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed50_t0.5_literal_speaker_data_augmentation_paths.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed60_t0.5_literal_speaker_data_augmentation_paths.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10-60_t0.5_data_aug.json -1

python preprocess/merge_instr.py \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_t0.5_literal_speaker_train.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed20_t0.5_literal_speaker_train.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed30_t0.5_literal_speaker_train.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed40_t0.5_literal_speaker_train.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed50_t0.5_literal_speaker_train.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed60_t0.5_literal_speaker_train.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10-60_t0.5_train.json -1

python preprocess/merge_instr.py \
/home/nav/Source/speaker_follower/tasks/R2R/speaker/faster+bi+nounk/results/speaker_teacher_imagenet_mean_pooled_bi_val_unseen_iter_12700.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_nounk_t0.3_literal_speaker_val_unseen.jsontemp \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_nounk_t0.5_literal_speaker_val_unseen.jsontemp \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed20_nounk_t0.3_literal_speaker_val_unseen.jsontemp \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed20_nounk_t0.5_literal_speaker_val_unseen.jsontemp \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_argmax+seed10t0.3+0.5+seed20t0.3+0.5_literal_speaker_val_unseen.json -1

python preprocess/merge_instr.py \
/home/nav/Source/speaker_follower/tasks/R2R/speaker/faster+bi+nounk/results/speaker_teacher_imagenet_mean_pooled_bi_val_unseen_iter_12700.json \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_nounk_t0.3_literal_speaker_val_unseen.jsontemp \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_nounk_t0.5_literal_speaker_val_unseen.jsontemp \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_nounk_literal_speaker_val_unseen.jsontemp \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_nounk_t2_literal_speaker_val_unseen.jsontemp \
/home/nav/Source/speaker_follower/tasks/R2R/aug/R2R_bi_12700_seed10_argmax_temp0.3-0.5-1-2_literal_speaker_val_unseen.json -1



python preprocess/merge_instr.py \
/home/xql/Downloads/temp/R2R_bi_12700_seed10_literal_speaker_train.json \
/home/xql/Downloads/temp/R2R_bi_12700_seed20_literal_speaker_train.json \
/home/xql/Downloads/temp/R2R_bi_12700_seed30_literal_speaker_train.json \
/home/xql/Downloads/temp/R2R_bi_12700_seed40_literal_speaker_train.json \
/home/xql/Downloads/temp/R2R_bi_12700_seed50_literal_speaker_train.json \
/home/xql/Downloads/temp/R2R_bi_12700_seed60_literal_speaker_train.json \
/home/xql/Downloads/temp/R2R_bi_12700_seed10-60_literal_speaker_train.json -1

python preprocess/merge_instr.py \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed10_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed20_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed30_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed40_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed50_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed60_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed10-60_literal_speaker_train.json -1
python preprocess/merge_instr.py \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed10_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed20_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed30_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed40_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed50_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed60_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed70_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed80_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed90_literal_speaker_train.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_train_nounk/R2R_bi_12700_seed10-90_literal_speaker_train.json -1


python preprocess/merge_instr.py \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed10_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed20_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed30_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed40_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed50_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed60_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed10-60_literal_speaker_data_augmentation_paths.json -1
python preprocess/merge_instr.py \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed10_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed20_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed30_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed40_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed50_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed60_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed70_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed80_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed90_literal_speaker_data_augmentation_paths.json \
tasks/R2R/data/sample/R2R_bi_seed10-90_data_aug_nounk/R2R_bi_12700_seed10-90_literal_speaker_data_augmentation_paths.json -1

# merge
for i in {0..4}
do
python preprocess/merge_instr.py \
tasks/R2R/data/R2R_beam5_literal_speaker${i}_data_augmentation_paths0.json \
tasks/R2R/data/R2R_beam5_literal_speaker${i}_data_augmentation_paths1.json \
tasks/R2R/data/R2R_beam5_literal_speaker${i}_data_augmentation_paths2.json \
tasks/R2R/data/R2R_beam5_literal_speaker${i}_data_augmentation_paths.json -1
done

python preprocess/merge_instr.py \
tasks/R2R/data/R2R_beam5_literal_speaker0_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker1_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker2_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker3_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker4_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker_data_augmentation_paths.json -1

python preprocess/merge_instr.py \
tasks/R2R/data/R2R_beam5_literal_speaker0_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker1_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker2_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker3_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker4_data_augmentation_paths.json \
tasks/R2R/data/R2R_sample3beam5_literal_speaker_data_augmentation_paths.json 3

python preprocess/merge_instr.py \
tasks/R2R/data/R2R_beam5_literal_speaker0_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker1_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker2_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker3_data_augmentation_paths.json \
tasks/R2R/data/R2R_beam5_literal_speaker4_data_augmentation_paths.json \
tasks/R2R/data/R2R_sample2beam5_literal_speaker_data_augmentation_paths.json 2


python preprocess/merge_instr.py \
tasks/R2R/data/R2R_beam0_literal_speaker_train.json \
tasks/R2R/data/R2R_beam1_literal_speaker_train.json \
tasks/R2R/data/R2R_beam2_literal_speaker_train.json \
tasks/R2R/data/R2R_beam3_literal_speaker_train.json \
tasks/R2R/data/R2R_beam4_literal_speaker_train.json \
tasks/R2R/data/R2R_beam5_literal_speaker_train.json \
tasks/R2R/data/R2R_beam6_literal_speaker_train.json \
tasks/R2R/data/R2R_beam7_literal_speaker_train.json \
tasks/R2R/data/R2R_beam8_literal_speaker_train.json \
tasks/R2R/data/R2R_beam9_literal_speaker_train.json \
tasks/R2R/data/R2R_sample2beam10_literal_speaker_train.json 2

python preprocess/merge_instr.py \
tasks/R2R/data/R2R_beam0_literal_speaker_train.json \
tasks/R2R/data/R2R_beam1_literal_speaker_train.json \
tasks/R2R/data/R2R_beam2_literal_speaker_train.json \
tasks/R2R/data/R2R_beam3_literal_speaker_train.json \
tasks/R2R/data/R2R_beam4_literal_speaker_train.json \
tasks/R2R/data/R2R_beam5_literal_speaker_train.json \
tasks/R2R/data/R2R_beam6_literal_speaker_train.json \
tasks/R2R/data/R2R_beam7_literal_speaker_train.json \
tasks/R2R/data/R2R_beam8_literal_speaker_train.json \
tasks/R2R/data/R2R_beam9_literal_speaker_train.json \
tasks/R2R/data/R2R_sample3beam10_literal_speaker_train.json 3

python preprocess/merge_instr.py \
tasks/R2R/data/R2R_beam0_literal_speaker_train.json \
tasks/R2R/data/R2R_beam1_literal_speaker_train.json \
tasks/R2R/data/R2R_beam2_literal_speaker_train.json \
tasks/R2R/data/R2R_beam3_literal_speaker_train.json \
tasks/R2R/data/R2R_beam4_literal_speaker_train.json \
tasks/R2R/data/R2R_beam5_literal_speaker_train.json \
tasks/R2R/data/R2R_beam6_literal_speaker_train.json \
tasks/R2R/data/R2R_beam7_literal_speaker_train.json \
tasks/R2R/data/R2R_beam8_literal_speaker_train.json \
tasks/R2R/data/R2R_beam9_literal_speaker_train.json \
tasks/R2R/data/R2R_beam10merged_literal_speaker_train.json -1


# data_augmentation_paths 
# split to 20 small files
python split_instr.py ../tasks/R2R/data/R2R_data_augmentation_paths.json 20
# generate for each file (use different gpu)
export PYTHONPATH=$PYTHONPATH:tasks/R2R
python tasks/data_aug/data_augmentation_from_speaker.py --pred_splits data_augmentation_paths0
python tasks/data_aug/data_augmentation_from_speaker.py --pred_splits data_augmentation_paths1
...............................................................................................
python tasks/data_aug/data_augmentation_from_speaker.py --pred_splits data_augmentation_paths18
python tasks/data_aug/data_augmentation_from_speaker.py --pred_splits data_augmentation_paths19
# merge same beam level
for i in {0..19}
do
python preprocess/merge_instr.py \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths0.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths1.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths2.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths3.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths4.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths5.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths6.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths7.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths8.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths9.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths10.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths11.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths12.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths13.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths14.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths15.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths16.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths17.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths18.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}_data_augmentation_paths19.json \
tasks/R2R/data/beam20_data_aug/R2R_beam20_literal_speaker${i}merged_data_augmentation_paths.json -1
done

# sample N(=2,3,...,9) instructions from all 20 instructions
for i in {2..9}
do
python preprocess/merge_instr.py \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker0merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker1merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker2merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker3merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker4merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker5merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker6merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker7merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker8merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker9merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker10merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker11merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker12merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker13merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker14merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker15merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker16merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker17merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker18merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/merged/R2R_beam20_literal_speaker19merged_data_augmentation_paths.json \
tasks/R2R/data/beam20_data_aug/sampled/R2R_sample${i}beam20_literal_speaker_data_aug.json ${i}
done
"""
