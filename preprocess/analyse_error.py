
import json

from eval import Evaluation
from collections import defaultdict


def get_scores(output_file, split):
    output_ids = []

    eval = Evaluation([split], 'lstm')
    eval.scores = defaultdict(list)
    instr_ids = set(eval.instr_ids)
    with open(output_file) as f:
        for item in json.load(f):
            if item['instr_id'] in instr_ids:
                output_ids.append(item['instr_id'])
                instr_ids.remove(item['instr_id'])
                eval._score_item(item['instr_id'], item['trajectory'])

    return output_ids, eval.scores


def find_negative_positive(output_file, split):
    output_ids, scores = get_scores(output_file, split)
    positive_samples = [(id, length) for id, score, length in zip(output_ids, scores['success'], scores['trajectory_lengths']) if score]
    positive_ids = [sample[0] for sample in positive_samples]
    positive_id2lens = dict(positive_samples)

    negative_samples = [(id, length) for id, score, length in zip(output_ids, scores['success'], scores['trajectory_lengths']) if not score]
    negative_ids = [sample[0] for sample in negative_samples]
    negative_id2lens = dict(negative_samples)
    return (positive_ids, positive_id2lens), (negative_ids, negative_id2lens)


def intersect(lists):
    inter = set(lists[0]).intersection(lists[1])
    if len(lists)>2:
        for i,l in enumerate(lists[2:]):
            inter = inter.intersection(l)
    return inter



prev_results = [('tasks/R2R/exps/baseline/seq2seq_sample_imagenet_val_unseen_iter_13100.json',
                'val_unseen'),
               ('/home/nav/Source/speaker_follower/tasks/R2R/eval_outputs/pragmatics_val_unseen_speaker_weight_0.00.json',
                'val_unseen')]

our_result = [('tasks/R2R/exps/Nresult-len8-bi-mean/seq2seq_sample_imagenet_val_unseen_iter_36000.json',
                'val_unseen')]

comparisons = prev_results + our_result

all_pos_ids = []
all_pos_id2lens = []
all_neg_ids = []
all_neg_id2lens = []
for output_file, split in comparisons:
    (positive_ids, positive_id2lens), (negative_ids, negative_id2lens) = find_negative_positive(output_file, split)
    all_pos_ids.append(positive_ids)
    all_pos_id2lens.append(positive_id2lens)

    all_neg_ids.append(negative_ids)
    all_neg_id2lens.append(negative_id2lens)

# find all success samples
pos_inters = intersect(all_pos_ids)
pos_paths = [id[:-2] for id in pos_inters]

# two failed one success
neg2pos1_inters = intersect(all_neg_ids[:2]+[all_pos_ids[-1]])
neg2pos1_paths = [id[:-2] for id in neg2pos1_inters]

# same path not same instr
ambig_paths = intersect([pos_paths, neg2pos1_paths])
print(ambig_paths)


examples = {}
for ambig_path in ambig_paths:
    examples[ambig_path] = {'all hit':[(id, all_pos_id2lens[2][id]) for id in pos_inters if id[:-2] == ambig_path],
                            'two lose one hits':[(id, all_neg_id2lens[0][id], all_neg_id2lens[1][id], all_pos_id2lens[2][id]) for id in neg2pos1_inters if id[:-2] == ambig_path]}

import pprint
pprint.pprint(examples)
print(len(examples))
