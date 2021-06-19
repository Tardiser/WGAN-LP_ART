# WGAN-LP_ART
Code for my Bachelor Thesis Project "Art Creation with a Generative Adversarial Network on BAM Dataset"

In my thesis project, I have tried training several different GAN models to generate similar images from BAM Dataset. This repository includes the notebook for my final model, as well as a code for calculating FID scores. Alas, BAM Dataset is not public, therefore I cannot share it here. However, it can be accessed by annotating 50-100 images to help them release the second version of this dataset. Website for BAM Dataset: https://bam-dataset.org/ 

Calculate FID code requires the FID code published in this repository (https://github.com/bioinf-jku/TTUR/blob/master/fid.py) to be in the same directory.

For Calculating the similarity between a generated image and the images in the original dataset, I've used the method proposed in this article: 
https://towardsdatascience.com/african-masks-gans-tpu-9a6b0cf3105c \
Although the author of this article used the 1st and 5th layers of the VGG network, I have used the 4th one because it performed better for me.
\
\
\
Some of the outputs and their similarity scores can be seen in the pictures below:
 
![image](https://user-images.githubusercontent.com/31456081/122655794-fe16c180-d15d-11eb-9d8c-df23547a1219.png)

![image](https://user-images.githubusercontent.com/31456081/122655809-243c6180-d15e-11eb-8c92-b71c4781c1df.png)

Please tell me this is a monster reading a book, because it's all I can see:
![image](https://user-images.githubusercontent.com/31456081/122655811-2b636f80-d15e-11eb-827c-f4c05f512486.png)

Similar images for this output are wrong, because I wasn't able to calculate in a regular way and instead calculated it from a saved image: \
![image](https://user-images.githubusercontent.com/31456081/122655828-4504b700-d15e-11eb-9ace-477ff963ee06.png)

Yep, it's a bowl: \
![image](https://user-images.githubusercontent.com/31456081/122655847-78474600-d15e-11eb-8594-cb349a443447.png)

Na na na na na na, BATMAN! \
![image](https://user-images.githubusercontent.com/31456081/122655868-9dd44f80-d15e-11eb-825a-a38795c9e48c.png)


Casually breaking the fourth wall: \
![image](https://user-images.githubusercontent.com/31456081/122655855-872df880-d15e-11eb-9e80-8e106b1c80dd.png)

