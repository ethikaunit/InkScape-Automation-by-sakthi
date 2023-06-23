#inkscape file2.svg --export-type=png --export-filename=./exported/file3.png
#inkscape filename.svg --export-type=png --export-dpi=300 --export-filename=./temp/file_name.png
import subprocess
import os
current_dir = os.getcwd()
file_list = os.listdir(current_dir)
file_count = len(file_list)

for i in range(file_count-2):
	print(i)
	cmdl = 'inkscape file{0}.svg --export-type=png --export-dpi=300 --export-filename=./exported/file{1}.png'.format(i,i)
	cmd = cmdl
	result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
	print("Output:")
	print(result.stdout)
	print("\nError:")
	print(result.stderr)