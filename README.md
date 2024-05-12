# Add-Tag-tool-for-Lora-training
This tool is used to quickly add tags to text files when training Lora.
Please forgive me for the current GUI being very simple.

## Files
The executable file can be executed directly, and the python file is code.

## There are 3 functions in total:
1.Rename and number the pictures(,png). For example, if you want to name your lora "Name", fill in "Name" in the File Name field and your pictures will be renamed Name1.png, Name2.png...  
2.Add a text file with the same name to the image.  
3.There are three modes to choose from when adding tags to text files. "All" means adding tags to all text files in the folder. "Range" means you can select a range and fill in the number corresponding to the first function. "One" refers to adding a Tag to a file. Just fill in "lower bound" (input field on the left). After selecting the mode and target file, fill in the required Tag into "content", such as "1girl,beautiful" ", and be careful not to use "," at the end.


## Precautions:
1.Due to some problems, renaming cannot be the same as before. If you need to rename to the same name (which may happen when you delete some files and want to realign the files), you need to use another name first.  
2.The same reason is due to some problems. When adding text files, it is best to ensure that there are only pictures(.png) in the folder.
