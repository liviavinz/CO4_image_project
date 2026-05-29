# Project Work: E. Coli Colony Segmentation

**Students**: Livia Vinzens, Cyrille Niklaus  
**Course**: MSLS / CO4 — ZHAW, 2nd Semester

## Abstract

A classical image segmentation pipeline for detecting and counting E. coli colonies on petri dishes. We scanned self-made agar plates dyed with food-grade colorants (red = Kanamycin, green = Carbenicillin, white = no antibiotic), then applied preprocessing (quantization, morphological cleaning, denoising), k-means clustering, and connected component analysis to extract colony masks and counts. Results were validated against manually created ground-truth masks (GIMP). We also explored thresholding to separate touching colonies.

## Repository Structure

```
├── CO4_Project_Work.ipynb   # Main notebook: full pipeline and evaluation
├── requirements.txt         # Python dependencies
├── data_to_submit/          # Cropped plate/ preprocessed images and automated segmentation masks
├── gimp_masks/              # Manual ground-truth masks created in GIMP
└── tools/                   # Helper modules (plotting, file I/O, colors, system info)
```

## References

- Dataset was made in the laboratories of the Institute of Medical Virology at the University of Zurich. We thank Prof. Alexandra Trkola for her help.
- Denoising: [OpenCV Filtering](https://docs.opencv.org/4.x/d4/d13/tutorial_py_filtering.html), [OpenCV Non-Local Means](https://docs.opencv.org/4.x/d5/d69/tutorial_py_non_local_means.html)
- GIMP: [https://www.gimp.org/downloads/](https://www.gimp.org/downloads/)
- Connected Components: [Wikipedia — Connected-component labeling](https://en.wikipedia.org/wiki/Connected-component_labeling)
- Generative AI tools (ChatGPT, Claude.ai) were used to assist with coding tasks — primarily for refactoring, debugging, and resolving image format issues. We avoided purely AI-generated code.
