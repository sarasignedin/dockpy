# escape-room-lab/scripts/data_copy.py
import shutil

# Define source and destination paths
src1 = 'data/data.csv'
src2 = 'data/data2.csv'
dst1 = 'data/copy_data.csv'
dst2 = 'data/copy_data2.csv'

# Copy data files
shutil.copy(src1, dst1)
shutil.copy(src2, dst2)

print("Data files copied to local container locations.")
