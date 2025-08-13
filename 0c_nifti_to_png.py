import gl
import os
import sys

# Read and parse input arguments passed via stdin
try:
    input_data = sys.stdin.read().strip()
    args = input_data.split()
except Exception as e:
    print("Error reading from sys.stdin: {}".format(e))
    sys.exit(1)

# Parse arguments
first_mm = float(args[0])
last_mm = float(args[1])
slice_spacing = float(args[2])
nifti_image = args[3]
output_folder = args[4]

# Debug - Check that parameters are correct
print("✅ Parameters:")
print("🔹 First:", first_mm)
print("🔹 Last:", last_mm)
print("🔹 Slice Spacing:", slice_spacing)
print("📂 Input Image:", nifti_image)
print("📂 Output Folder:", output_folder)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Initialize slice range
start = first_mm
end = last_mm
step = slice_spacing
current = start
index = 0

# Reset MRIcroGL and load the image
gl.resetdefaults()
gl.loadimage(nifti_image)
gl.colorbarposition(0)

# Wait for MRIcroGL to update the view
gl.wait(1000)

# Save all sagittal slices in reverse order
while current <= end:
    gl.mosaic("S {}".format(current))
    gl.wait(100)  # Ensure the view is properly updated

    filename = os.path.join(output_folder, 'Slice_{:03d}.png'.format(index))
    gl.savebmp(filename)

    current += step  
    index += 1 

# Close MRIcroGL
gl.quit()


