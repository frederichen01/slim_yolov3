import os


delete_lines = open('delete.txt').readlines()
images_path = os.listdir('images')
count = 0
for image_path in images_path:
    if image_path+'\n' in delete_lines:
        os.remove('images/'+image_path)
        os.remove('labels/'+image_path.split('.')[0]+'.txt')
        count += 1
print(count)

