# pip install py2app
# make sure have the following libraries installed: pyautogui, keyboard
# then run `python autocliker_setup.py py2app`
# and the program should spit out a build folder.

from setuptools import setup
APP = ['autoclicker.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pyautogui', 'keyboard'],
    'plist': {
        'CFBundleName': 'MouseTool',
        'NSAAppleScriptEnabled': 'Yes'
    }
}

setup(
    app=APP,
    options={'py2app':OPTIONS},
    setup_requires=['py2app'],
)