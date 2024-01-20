from os.path import join

from dataset import MICROSCOPY, SYNTHESIZED


def get_training_set(dataset, root_dir):
    if dataset=='MICROSCOPY':
        return MICROSCOPY(root_dir, True)
    elif dataset=='SYNTHESIZED':
        return SYNTHESIZED(root_dir, True)

def get_test_set(dataset, root_dir):
    if dataset=='MICROSCOPY':
        return MICROSCOPY(root_dir, False)
    elif dataset=='SYNTHESIZED':
        return SYNTHESIZED(root_dir, False)
