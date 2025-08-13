Automatic Diploe Segmentation from CT Neurocranium Images – Pipeline Overview

1.	Introduction
This repository contains a complete workflow for automatic segmentation of the cranial diploe from CT scans.
The pipeline processes a neurocranium CT (NIfTI), extracts sagittal slices, performs segmentation via K‑means, morphological operations, watershed algorithm and reconstructs the final diploe mask as a 3D NIfTI volume.

A demo version of the workflow is included: for each step, a Jupyter Notebook (.ipynb) is provided with the code already executed and example results displayed, so you can review outputs without running the full process (1a_cranium_segmentation_demo.ipynb).
In contrast, 1b_cranium_segmentation_full.ipynb runs the full pipeline on all slices.

Required starting input: a CT neurocranium NIfTI image.

2.	Required software and libraries
• Python 3.8+
• MRIcroGL (used to export sagittal PNG slices)

Python packages:
	•	nibabel
	•	numpy
	•	opencv-python
	•	scipy
	•	Pillow
	•	matplotlib

3.	Repository contents (scripts & notebooks)
	•	0a_ct_image_preprocessing.ipynb
Preprocessing of the CT NIfTI: X‑axis reorientation (flip) and gamma correction; saves the corrected NIfTI.
	•	0b_run_mricrogl.py
Launches MRIcroGL, passes coordinates/spacing and controls slice export.
	•	0c_nifti_to_png.py
MRIcroGL script that receives parameters and saves sagittal PNG slices from the NIfTI volume.
	•	1a_cranium_segmentation_demo.ipynb
Demo notebook: single-slice example(s) with code already executed and results shown for quick review.
	•	1b_cranium_segmentation_full.ipynb
Full segmentation: processes all sagittal slices; generates cranium, bone and diploe masks per slice.
	•	2_png_to_nifti.ipynb
Reconstructs the PNG diploe masks into a 3D NIfTI volume aligned to the reference CT.
	•	test.zip
Example/test data for the demo notebooks.

4.	Pipeline steps (high level)
Step 0 – Preprocessing
• Load CT neurocranium NIfTI, reorient (flip X), apply gamma correction, save corrected NIfTI.

Step 1 – Slice extraction (sagittal)
• Use MRIcroGL to export sagittal PNG slices from the corrected NIfTI (coordinates and spacing computed from the affine).

Step 2 – Segmentation
• Single‑slice demo (1a) for inspection/QA.
• Full batch (1b): K‑means (k=2) to separate tissues, morphological closing to fill skull holes, diploe = cranium − bone, watershed to remove border artifacts, save per‑slice masks (cranium/bone/diploe).

Step 3 – Reconstruction to NIfTI
• Read diploe PNG masks, flip/resize to match the reference CT dimensions, map slice indices, assemble 3D volume, save diploe_mask.nii.

5.	Inputs and outputs
Input (required)
• neurocranium_ct_image.nii – CT neurocranium (NIfTI)

Intermediate outputs
• gamma_corrected_neurocranium_ct_image.nii – corrected NIfTI
• png_folder_sagittal_plane/ – sagittal PNG slices
• segmentation_masks_folder_sagittal_plane/
├─ cranium_mask/
├─ bone_mask/
└─ diploe_mask/

Final output
• diploe_mask.nii – 3D NIfTI diploe mask reconstructed from the PNG slices

6.	Notes
• Update file paths in the scripts/notebooks to match your environment.
• Ensure MRIcroGL is installed and callable for slice export.
• The demo notebooks show executed code and results; use the full notebook to run the pipeline on your own data.
