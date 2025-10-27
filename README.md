# <img src="./pac.ico" alt="PyPacman logo" /> PyPacman

This project replicates the famous Pacman game using the Python language.

I developed it as a project for the Object Oriented Programming subject for the Bachelor's degree of Electronic and Computer Engineering at the University of Messina.

## Features
- File-based map generation. The "standard_map.txt" file in the "maps" folder, represent the classic Pacman map, while it is possible to generate new map by modifing that file.
- File-based character and map tiles image loading. The "default.png" file inside the "textures" folder represent the basic tile and characters implementation for the classical map. It is possible to modify this file or generate a new one to change the textures.
- One thread and one AI "personality" for each ghost. This was not particularly tuned and could be improved.

## Build & Run
It is possbile to build the game by installing the ``pyinstaller`` library:
```
pip install pyinstaller
```
After that, is possible to build the executable with the command:
```
pyinstaller -F pypacman.py --specpath ./ --name pypacamn --icon pac.ico
```
This will generate the executable file in the "dist" folder. In addition, it is necessary to copy the "maps" and "textures" folders inside the dist directory to make the application work.

In alternative, it is possible to run the code with the command:
```
python pypacman.py
```