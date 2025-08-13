import os
import nibabel as nib
import numpy as np
import subprocess

mricrogl_path = r"path\to\MRIcroGL.exe" ## Change with your MRIcroGL folder path
mricrogl_script_path = "0c_nifti_to_png.py"

ct_nifti_path = r"test\gamma_corrected_neurocranium_ct_image.nii"
nifti_img = nib.load(ct_nifti_path)

# Get the updated affine matrix after reorientation
affine = nifti_img.affine
shape = nifti_img.shape

########################## SAGITTAL AXIS ##################################################

# New coordinates of the first and last voxel along the X axis
first_voxel = np.array([0, 0, 0, 1])               # First voxel (X=0)
last_voxel = np.array([shape[0] - 1, 0, 0, 1])     # Last voxel (X=max)

# Convert from voxel space to millimeter (mm) space
start_x_mm = np.dot(affine, first_voxel)[0]
end_x_mm = np.dot(affine, last_voxel)[0]
slice_spacing_x = np.linalg.norm(affine[0, :3])    # Distance between slices

print(f"Start X: {start_x_mm} mm, End X: {end_x_mm} mm, Step: {slice_spacing_x} mm")

png_path = r"test\png_folder_sagittal_plane"

# 🔹 1️⃣ Create the argument string (space-separated values)
args = "{} {} {} {} {}".format(
    start_x_mm, end_x_mm, slice_spacing_x, ct_nifti_path, png_path
)

###########################################################################################

########################## CORONAL AXIS (COMMENTED OUT) ##################################

# New coordinates of the first and last voxel along the Y axis
# first_voxel = np.array([0, 0, 0, 1])
# last_voxel = np.array([0, shape[1] - 1, 0, 1])

# Convert from voxel space to millimeter (mm) space
# start_y_mm = np.dot(affine, first_voxel)[1]
# end_y_mm = np.dot(affine, last_voxel)[1]
# slice_spacing_y = np.linalg.norm(affine[1, :3])

# print(f"Start Y: {start_y_mm} mm, End Y: {end_y_mm} mm, Step: {slice_spacing_y} mm")

# png_path = os.path.join(patient_path, f"Slices_Coronal_{pat}_HR_CT_Surface")

# 🔹 1️⃣ Create the argument string (space-separated values)
# args = "{} {} {} {} {}".format(
#     start_y_mm, end_y_mm, slice_spacing_y, ct_nifti_path, png_path
# )

###########################################################################################

# 🔹 2️⃣ Run MRIcroGL and pass the arguments via stdin
process = subprocess.Popen(
    [mricrogl_path, mricrogl_script_path],
    stdin=subprocess.PIPE,
    text=True
)

# 🔹 3️⃣ Send the arguments to the MRIcroGL script
process.communicate(input=args)


        




