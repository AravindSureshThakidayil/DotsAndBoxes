![Plasmo Notion](https://user-images.githubusercontent.com/64391274/219694678-8f1a2829-b0b2-41de-9152-4c4a4e43c2d5.png)


# This is a work in progress.
<hr/> 

# Dots and Boxes
`Dots and Boxes` is our PyGame implementation of the game of Dots and Boxes,
widely blayed in classrooms, at parties and at teatime. The game is simple enough;
two or more players take turns in drawing vertical or horizontal lines in a
square lattice, and each player scores a point when they draw the last side of
a 1x1 square. The winner is the player with the maximum score when no more lines
can be drawn.
## Team members
1. [Aravind Suresh Thakidayil](https://github.com/AravindSureshThakidayil)
2. [Sūraj Krishna](https://github.com/IAMSUPERBOY)
## Link to product walkthrough
[link to video]
## Working
Explaining the working of project
1. The algorithm is quite simple: lines are removed from a pre-written collection
of boxes as they are drawn. Once a box is removed entirely, the player receives
a point.
2. Embed video of project demo
## Libraries used
PyGame is the only dependency used here.
## Configuration
On a computer with a Python interpreter and sufficient functionality to run PyGame,
download this repository and run `start.py`.
## How to Run
Simply execute `start.py`. Press enter to get to the grid. Click on a dot to draw a line from that dot
and click on a second, adjacent dot to complete it. Scores are on either side.
