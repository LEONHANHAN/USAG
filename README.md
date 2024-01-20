# USAG: Unsupervised Segmentation network learning by Adversarial Generation
A clean and readable Pytorch implementation of USAG

## Prerequisites
Code is tested on python 3.7.x with pytorch 1.0.1, it hasn't been tested with previous versions.

### [PyTorch & torchvision](http://pytorch.org/)
Follow the instructions in [pytorch.org](http://pytorch.org) for your current setup

## Training
### 1. Setup the dataset
First, you will need to create your own dataset by cropping some cells from a dataset. Recommended using ``Phc-U373'' and ``Phase100'' (http://celltrackingchallenge.net/2d-datasets/) dataset. 
```
mkdir datasets

```
### 2. Train!
```
python train.py --cuda
```
This command will start a training session using the images under the *./datasets/* directory.  You are free to change those hyperparameters. 

If you don't own a GPU remove the --cuda option, although I advise you to get one!

You need to adjust the hyperparameters to get good segmentation results.

After generating cell images and masks with size of 128*128, you need to choose 16 of them to stitch together to get a cell image with size of 512*512. Then, with the synthesized cell images and masks, you can train a segmentation network (e.g., U-Net).


### 3. Result

Examples of the generated outputs are saved under the *./result/* directory.


### 4. Acknowledgement
Most codes are borrowed from the project of ``VEGAN: Unsupervised Meta-learning of Figure-Ground Segmentation via Imitating Visual Effects'' (https://arxiv.org/abs/1812.08442)
