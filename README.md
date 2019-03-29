# Evaluating Human and Machine Performance in Object Recognition with Scrambled Images 
by Roshni Sahoo

## Introduction

Deep neural networks are achieving previously unseen performance in object classification, raising questions about whether DNNs operate similarly to human vision. In this study, we investigate whether global shape of an object is essential to accurately completing object classification tasks for humans and for machines. We hypothesize that shape is an important cue for recognition in human vision. As a result, when we distort the global shape of an object in an image, we expect human performance on the object classification task to degrade. On the other hand, many studies suggest that deep neural networks do not rely on global shape for classification tasks. This implies that If we distort the global shape of an object but simultaneously preserve local features, then DNNs will achieve similar classification accuracy. 

To test this hypothesis, we define a specific type of distortion called scrambling and evaluate human and machine performance on object classification tasks with scrambled images. We can define “scrambling” as the following procedure. Given an image with dimensions $$n \cdot n$$ and a scrambling factor $$r$$, we can divide the image into $$r^2$$ smaller squares of size $$\frac{n}{r} \cdot \frac{n}{r}$$ and stitch them randomly back together to make a scrambled $$n \cdot n$$ image. A highly scrambled image corresponds to a high $$r$$ value.

The motivation for this project is to gain insight that will ultimately make deep learning systems more transparent. Deep learning systems are often construed as a black box because people cannot pinpoint exact reasons for why a system makes a particular decision. Furthermore, we aim to assess whether machines are better than humans at object recognition on these types of images because this may provide insight in how the human visual system may differ from computer vision systems. We can also determine when both of these systems fail by determining the point at what point human and machine performance compromised due to scrambling. 

## Hypotheses

We define $$t$$ to be the object classification accuracy on a sample set of scrambled images. 

1. $$H_{0}: t_{model} = t_{human}$$.  Our null hypothesis is that the model’s classification accuracy will match that of humans.
2. $$H_{1}: t_{model} > t_{human}$$.  Our alternative hypothesis is that the model’s classification accuracy surpass that of human’s.
## Variables of Interest

We highlight our independent variables for this experiment.

1. Scrambling Factor ($$r$$) - The scrambling factor represents the degree to which we scramble an image. We plan on creating $$200$$ scrambled images; there will be $$25$$ images for each scrambling factor $$r=1, 2, 3, 4, 5, 6, 7, 8$$.
2.  Exposure Time for Scrambled Image ($$s$$)- The exposure time for scrambled image is the length of time that we will show human subjects the scrambled image. We will show an image for $$s$$seconds, where $$s \in \{0.01, 0.1, 1, 5, 10 \text{ seconds}\}$$.

We explain our metrics, or dependent variables, for this experiment

1. Classification Accuracy ($$t$$) - The classification accuracy for humans is the number of images that humans classifies correctly for a given combination of scrambling factor and exposure time ($$r, s$$). The classification accuracy for machines is the number of images that the model classifies correctly for a given scrambling factor ($$r$$).
## Experimental Design

The first step of this process involves image processing, we will take 200 images from various categories whose labels are in the vocabulary of the ImageNet dataset. We will randomly select 25 for each scrambling factor. Using libraries such as OpenCV and Scikit-Image, we will generate scrambled images. In addition, all of the images will be converted to grayscale.

The next step is data collection. We will create a survey to collect data from humans. Each question will involve a match-to-sample question for a human to answer.  The scrambled image will depict a scrambled picture of an image from an ImageNet category. The answer choices will depict unscrambled images from different ImageNet categories. The correct answer will be an image from the same category as the scrambled image. 

We will give the humans 200 scrambled images with assorted scrambling factors. We expose the humans to the scrambled images for various lengths of exposure time and they will click on the that they believe matches the category of the unscrambled image. We will measure the classification accuracy for humans for a given value of $$r$$ and for a given exposure time.

We will run the same experiment on a neural network (AlexNet) that has been pretrained on ImageNet (including grayscale inputs). For every question in the survey, we can find the network’s answers to each of these questions. We will pass the scrambled image as an input to the network. After that, we will extract the weights of the logits that correspond to the image categories that are in our answer space. We will normalize these values. The logit that has the highest value represents the answer choice that the network has selected. We will measure the classification accuracy for machines for a given value of $$r$$.





