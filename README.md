# Ego-Interaction: Visual Hand-Object Pose Correction for VR Experiences
Code and Data for the Ego-Interaction Dataset

![teaser](https://user-images.githubusercontent.com/25514442/104743868-17958680-5744-11eb-96d2-26f17782ba12.png)

## Table of Contents
  * [Abstract](#abstract)
  * [Dataset](#dataset)
    * [Contents](#contents)
    * [Layout](#layout)
    * [Access](access)
  * [Citation](#citation)
  * [Contact](#contact)
  
  ## Abstract
  

Immersive virtual reality (VR) experiences might often be required to track both a users hands and a physical object at the same time and use the information to animate computer generated representations of the two interacting. However, to render visually without artefacts requires highly accurate tracking of the objects themselves and their relative locations -- made even more difficult when the objects themselves are articulated or deformable. If this tracking is incorrect, then the quality of the visual experience is reduced. In this paper we turn the problem around -- instead of focusing on improving high quality renders of hand-object interactions by improving tracking quality, we acknowledge there will be tracking errors and just focus on fixing the visualisations. We propose a Deep Neural Network (DNN) that modifies hand pose based on it's relative position with the object. However, to train the network we require sufficient labeled data. We therefore also present to the community a new dataset of hand-object interactions -- Ego-Interaction. This is the first egocentric hand-object interaction dataset with 3D ground truth data for both rigid and non-rigid objects. The Ego-Interaction dataset contains 92 sequences with 4 rigid, 1 articulated and 4 non-rigid objects and demonstrates hand-object interactions with 1 and 2 hands. carefully captured, rigged and animated using motion capture. The data set is not intended to be useful not just for our visualisation problem, but as a general resource for researchers in the VR and AI community interested in other hand-object and egocentric tracking related problems.

[Link to paper]()

  
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
  * MANO hand parameters
  * Textured hand mesh in rest pose
  * 6DoF Camera pose
  * Egocentric RGBD images capture by Intel Realsense D435 at 30fps
  
  
  D435 colour intrinsic: [622.084, 0, 426.034, 0, 622.154, 245.07, 0, 0, 1]
  
  D435 depth intrinsic: [423.053, 0, 428.72, 0, 423.053, 247.33, 0, 0, 1]


  
  ### Access
  
  Dataset can be accessed via this [link](https://forms.gle/cT12U9CdWkBzR8En9)
   
  
  ## Citation
  
  When using this data, please use the following citation.
  
  ```
  @inproceedings{taylor_MIG_21,
author = {Taylor, Catherine and Evans, Murray and Crellin, Eleanor and Parsons, Martin and Cosker, Darren},
title = {Ego-Interaction: Visual Hand-Object Pose Correction for VR Experiences},
year = {2021},
publisher = {Association for Computing Machinery},
booktitle = {Motion, Interaction and Games},
series = {MIG '21}
}
  ```
  ## Contact
  
  This code is maintained by Catherine Taylor (catherine.a.taylor2@gmail.com).
