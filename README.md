# Ego-Interaction: A Multiple Hand-to-Rigid and Non-Rigid Object Interaction Dataset
Code and Data for the Ego-Interaction Dataset

![teaser](https://user-images.githubusercontent.com/25514442/104743868-17958680-5744-11eb-96d2-26f17782ba12.png)

## Table of Contents
  * [Abstract](#abstract)
  * [Dataset](#dataset)
    * [Contents](#contents)
    * [Layout](#layout)
    * [Access](access)
  * [Code](#code)
    * [Dependencies](#dependencies)
  * [Citation](#citation)
  * [Contact](#contact)
  
  ## Abstract
  
Novel and immersive VR and AR experiences can be created by transporting physical objects into virtual worlds. This requires a fast and robust algorithm for tracking the behaviour of rigid and nonrigid objects within Egocentric hand-object interaction sequences. In turn, the design of such an algorithm requires high quality and varied data. Existing hand-object datasets are largely limited to rigid object interactions, 3rd person views or are aimed towards hand tracking or action recognition applications and so do not provide the ground truth object pose or shape. Moreover, those datasets which do show non-rigid object interactions provide no ground truth 3D data for the object shape and pose and instead only provide 2D annotations.

We address these limitations in this paper, by presenting a new dataset – Ego-Interaction – the first egocentric hand-object interaction dataset with 3d ground truth data for both rigid and non-rigid objects. The Ego-Interaction dataset contains 92 sequences with 4 rigid, 1 articulated and 4 non-rigid objects and demonstrates handobject interactions with 1 and 2 hands. We also outline an approach for creating additional synthetic sequences, by augmenting the data provided in our dataset and discuss the potential future direction of hand-object tracking datasets. Our dataset and scripts to generate synthetic data will be made publicly available for research purposes.

[Link to paper]()

[Link to video results]()
  
  ## Dataset
  
  ![overview](https://user-images.githubusercontent.com/25514442/104744739-2597d700-5745-11eb-878b-f45fb18a1df9.png)


  
  ### Contents
  
  Our dataset contains hand-object interaction sequences for 4 rigid, 1 articulated and 4 non-rigid objects. We demonstrate sequences with 1 or 2 hand interactions as well as sequences where no hand tracking has been recorded. Interaction sequences contain the following motions:
  * Rotations and translations of object in 3D space
  * Object passed between hands
  * Non-rigid object deformations
  
  For each object, we provide the following data representing the interaction sequences
  * The solved object skeleton
  * Textured object mesh in rest pose
  * The solved hand skeleton
  * Textured hand mesh in rest pose
  * 6DoF Camera pose
  * Egocentric RGBD images capture by Intel Realsense D435 at 30fps
  
  ### Access
  
  Dataset can be accessed via this [link](https://forms.gle/cT12U9CdWkBzR8En9)
  
  ## Code
  
  ## Citation
  
  When using this data, please use the following citation.
  
  ## Contact
  
  This code is maintained by Catherine Taylor (c.taylor3@bath.ac.uk).
