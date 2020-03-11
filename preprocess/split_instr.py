import json
import sys


def split_data(file, n):
    with open(file) as f:
        paths = json.load(f)

    interval = int(len(paths) / n)
    for i in range(n):
        start, end = i * interval, min((i + 1) * interval, len(paths))
        with open(file[:-5] + str(i) + '.json', 'w') as outfile:
            json.dump(paths[start:end], outfile, indent=4, separators=(',', ':'))

if __name__ == '__main__':
    split_data(sys.argv[1],int(sys.argv[2]))
    #python split_instr.py ../tasks/R2R/data/R2R_data_augmentation_paths.json 3
    #python split_instr.py ../tasks/R2R/data/R2R_data_augmentation_paths.json 20

