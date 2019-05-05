
# raycasting_pyqt

## Description
Implementation of raycasting method used in Wolfenstein 3D.   
Inspired by this video, https://youtu.be/eOCQfxRQ2pY  , which talks about map renderer used in Wolfenstein 3D.  
id Software used raycasting method to map 2D information onto screen and make it look like 3D, a marvelous engineering technique!  
## Demo
 ![](gif/rotate.gif)   ![](gif/move.gif)
## Run
**Requirements**: PyQt5  
Execute ```driver.py``` to open the window.  
Use arrow keys to move player's position by 10 px, and ```Q``` and ```E``` to rotate viewing angle by 1 degree. *rotating to certain angles (like 90 degree) will not update frame due to incalculable tangent function.

## Trivia 
1. The distance used to map collision point to screen is not the distance between collision point and player; instead, it's the distance between a line traveling through collision point and is perpendicular to the viewing angle. Otherwise, it will end up with fish-eye effect.  
2. This distance can be calculated via ```d * cos(theta)``` where d is the distance between collision point and player; and theta is the viewing angle. The most intuitive way to calculate ```d``` involves ```sqrt``` operation, which may be computationally expensive for a computer then, so a hack was applied by using trigonometry ```d = dy*cos(beta) + dx*sin(beta)``` where ```beta``` is the angle between ray cast out and viewing.
3. Some other computationally expensive steps (like wall height mapping) were also pre-calculated to speed up run-time efficiency.
