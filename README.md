# CO4 Imaging: E.Coli Colony Segmentation
## Goals: 
- Compare manual vs. automatic classical segmentation on lab E.Coli colonies on petri dishes
- compare algorithm on AGAR dataset images
- produce classical segmentation + bounding box pipeline for DeepLearning Project

## Workflow:
- Acquire 5 lab images of E. coli colonies (document conditions: lighting, plate type,...)
- Preprocess (grayscale/color, illumination, denoising etc)
  
- Manual segmentation (GROUND THRUTH MASK)
- "Classic" oldschool automatic segmentation (f.ex. watershed for touching colonies)

- Evaluate on lab images (IoU, count error)
- Generalization on 5 AGAR images:
  - Manual segmentation  (GROUND THRUTH MASK)
  - Run THE SAME automatic pipeline
  - Report the same metrics

## Handoff to Deep Learning Project
- fit bonding boxes around each colony
- classical segmentation + bounding-box pipeline becomes the non-learned baseline for the DL project
