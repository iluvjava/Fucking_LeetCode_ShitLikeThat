import os
# os.rename(r'C:\Users\Ron\Desktop\Test\Products.txt',r'C:\Users\Ron\Desktop\Test\Shipped Products.txt')

# ToRenameDir = os.listdir(".")[-1]
# Newname = "New name"
# os.rename(ToRenameDir, Newname)

AllFolders = os.listdir("./")
AllFoldersNewName = [S.replace(" ", "-") for S in AllFolders]
for Old, New in zip(AllFolders, AllFoldersNewName):
    os.rename(Old, New)

