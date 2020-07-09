from distutils.core import setup
from os import path

DESCRIPTION = """freshlybuiltimagejaano is the library made to allow users to get info about 
                 the input image"""

# The directory containing this file
this_directory = path.abspath(path.dirname(__file__))

# Import the README and use it as the long-description.
try:
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
  name = 'freshlybuiltimagejaano',         
  packages = ['freshlybuiltimagejaano'],   
  version = '0.0.0.1',     
  license='MIT',        
  description = 'Photo k baare m jaano',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Vishal Sharma',                   
  author_email = 'vishalsharma.gbpecdelhi@gmail.com',      
  url = 'https://github.com/freshlybuiltongithub/freshlybuiltimagejaano',   
  download_url = 'https://github.com/FreshlyBuilt/freshlybuiltimagebol/archive/v0.0.0.1.tar.gz',  
  keywords = ['Image', 'Audio', 'Text'],   
  install_requires=[            
          'hyper',
          'googletrans',
          'gTTS',
          'Pillow',
          'pytesseract',
          'opencv-python',
          'numpy',
          'matplotlib',
          'imutils'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
