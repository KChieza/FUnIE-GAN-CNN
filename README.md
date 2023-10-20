# [Investigating the Effect of Deep Learning for Image Preprocessing in Fish Classification](https://www.example.com)
## Abstract
Automated fish species classification in underwater environments poses challenges due to the poor image quality and similarities among fish species. This study addresses these challenges by introducing a novel approach, utilizing a state-of-the-art underwater image enhancement GAN called FUnIE-GAN for image preprocessing. 

Results demonstrate FUnIE-GAN's effectiveness in enhancing fish classification, particularly in imbalanced datasets. The proposed system, which uses FUnIE-GAN for preprocessing and a CNN for classification, achieved state-of-the-art results, obtaining an f1 score of 95\% and 97% on two imbalanced datasets with 23 and 10 classes, respectively. The system also performed reasonably well on a dataset with 39 classes, yielding an accuracy of 81%.
Implementation of my honours thesis project, submitted 20 October 2022.

[Link to Official FUnIE-GAN repo](https://github.com/xahidbuffon/FUnIE-GAN). This repo contains the code to train and evaluate FUnIE-GAN and a trained FUnIE-GAN model.

[Link to Offical Fish4knowledge dataset page](https://homepages.inf.ed.ac.uk/rbf/Fish4Knowledge/). Link to a dataset used in this research.

Create Sharpened versions of fish datasets using sharp.py.
Create FUnIE-GAN enhanced versions of fish datasets using the Funie-Gan Model.

Set your path_to_fish_dataset to your original, sharpened, and FUnIE-GAN-enhanced images in the different notebook sections, as noted by the markdowns.
