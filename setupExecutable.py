from distutils.core import setup
import py2exe, sys, os

bkgFolder = 'background'
imgFolder = 'sprites'
sndFolder = 'sound' 
musFolder = 'music'

currentDir = os.path.dirname(os.path.realpath(__file__))

# grabbing all images in bkgFolder
bkgFiles = []
bkgPath = currentDir + '\\' + bkgFolder
for files in os.listdir(bkgPath):
   f1 = bkgPath + "\\"+ files
   if os.path.isfile(f1): # skip directories
       f2 = (bkgFolder, [f1])
       bkgFiles.append(f2)

# grabbing all images in imgFolder
imgFiles = []
imgPath = currentDir + '\\' + imgFolder
for files in os.listdir(imgPath):
   f1 = imgPath + "\\"+ files
   if os.path.isfile(f1): # skip directories
       f2 = (imgFolder, [f1])
       imgFiles.append(f2)

# grabbing all sounds in sndFolder
sndFiles = []
sndPath = currentDir + '\\' + sndFolder
for files in os.listdir(sndPath):
   f1 = sndPath + "\\" + files
   if os.path.isfile(f1): # skip directories
       f2 = (sndFolder, [f1])
       sndFiles.append(f2)

# grabbing all music in musFolder
musFiles = []
musPath = currentDir + '\\' + musFolder
for files in os.listdir(musPath):
   f1 = musPath + "\\" + files
   if os.path.isfile(f1): # skip directories
       f2 = (musFolder, [f1])
       musFiles.append(f2)       
   
# This block of code is necessary or else pygame.mixer will fail
origIsSystemDLL = py2exe.build_exe.isSystemDLL # save the orginal before we edit it
def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll"):
            return 0
    return origIsSystemDLL(pathname) # return the orginal function
py2exe.build_exe.isSystemDLL = isSystemDLL # override the default function with this one
    
# For the icon, use png2ico and use at least two pngs with different sizes.
# Something that has worked for me is one with 128x128 and one with 32x32,
# the one with 128x128 should come first in the command line, like
# png2ico icon.ico png128.png png32.png. Strangely enough, the 128x128
# can be a blank one and most of the time the 32x32 will be the one displayed
target = {
'script' : "cometz.py",
'version' : "0.1",
'copyright' : "Alexandre Lopes & Filipa Silva 2014",
'name' : "CometZ", 
"icon_resources": [(1, "icon.ico")]
}    
    
setup(
    #console=['main.py'],
    windows=[target],
    data_files = bkgFiles + imgFiles + sndFiles + musFiles,
                
    options = {'py2exe': {'bundle_files': 2, 'compressed': True}}
     )
