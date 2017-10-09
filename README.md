# Meow or Not: A foray into computer vision

In these jupyter notebooks, I've explored detection and classification techniques in computer vision.
For data, I took advantage of the absurd number of photos I've taken of my cat, Meow.

## Table of Contents

1. Object Detectors in Dlib
	1. Off-the-shelf face detection
		1. HOG-based
		2. CNN-based
	2. Custom-trained HOG-based Meow face detector
2. CNN Image Classifiers in Keras
	1. Example of using an off-the-shelf CNN (ResNet50)
	2. Building a custom Meow classifier via transfer learning (VGG16)

## Examples

Here's a live demo of my Meow face detector (dlib):
![meow_detected](https://user-images.githubusercontent.com/26487650/31292982-64c44b90-aa8a-11e7-8c1e-bd716e4f2638.gif)

The Meow classifier (keras) performed quite well:
![auc_plots](https://user-images.githubusercontent.com/26487650/31352680-7cd4850e-ace4-11e7-9f5f-3b358fca6241.png)

Here are some examples of how the model can even distinguish Meow from very similar looking cats:
![meow_alike1](https://user-images.githubusercontent.com/26487650/31352681-7ce3229e-ace4-11e7-9706-54908aca8e8d.png)

The model can't get this one though -- can you?
![meow_alike2](https://user-images.githubusercontent.com/26487650/31352682-7cea90ce-ace4-11e7-95c0-60d1880b5328.png)

(The one on the left is the ultimate Meow doppelgänger.)
