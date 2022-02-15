
# import module
from pdf2image import convert_from_path

RESUME_FOLDER = './output'

# Clear readme
file = open("README.md","w")
file.write('See below\n')
file.close()

# Store Pdf with convert_from_path function
images = convert_from_path('main.pdf')
#  ![Resume](https://github.com/asultan123/Resume/blob/master/output/page0.jpg)
for i in range(len(images)):
    images[i].save(RESUME_FOLDER + '/page'+ str(i) +'.jpg', 'JPEG')
    with open('./README.md', 'a') as md_file:
        md_file.write(f'![Resume](https://github.com/asultan123/Resume/blob/master/output/page{i}.jpg)\n')