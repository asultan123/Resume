
# import module
from pdf2image import convert_from_path
import os
import glob

print('Compiling resume pdf to multiple pngs')

RESUME_FOLDER = './output'

files = glob.glob(RESUME_FOLDER + '/*')
for f in files:
    os.remove(f)

# Clear readme
file = open("README.md","w")
file.write('Resume adapted from https://github.com/sb2nov/resume\n')
file.close()

# Store Pdf with convert_from_path function
images = convert_from_path('main.pdf')

for i in range(len(images)):
    images[i].save(RESUME_FOLDER + '/page'+ str(i) +'.jpg', 'JPEG')
    with open('./README.md', 'a') as md_file:
        md_file.write(f'![Resume](https://github.com/asultan123/Resume/blob/master/output/page{i}.jpg)\n')