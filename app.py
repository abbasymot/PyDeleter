import os



path = input("Enter the directory path => (E:\\New Folder): ")
file_format = input("Enter the format that you want to delete => (.srt, .mp4 etc): ")

delete = int(input(f"""
1- If you wanna delete all of the {file_format}'s: \n
2- If you wanna delete all of the other files, EXCLUDE {file_format}: """))

for file in os.listdir(path): # For file in directory
	if delete == 1:
		if file.endswith(file_format):
			os.unlink(f"{path}\\{file}")
	elif delete == 2:
		if not file.endswith(file_format):
			os.unlink(f"{path}\\{file}")
	else:
		print ("Wrong input, Select from 1 to 2!")
		break
