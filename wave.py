"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in the Alien
Invaders game.  Instances of Wave represent a single wave.  Whenever you move to a
new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on screen.
These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from game2d import *
from consts import *
from models import *
import random
import math

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not permitted
# to access anything in their parent. To see why, take CS 3152)


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.

    This subcontroller has a reference to the ship, aliens, and any laser bolts on screen.
    It animates the laser bolts, removing any aliens as necessary. It also marches the
    aliens back and forth across the screen until they are all destroyed or they reach
    the defense line (at which point the player loses). When the wave is complete, you
    should create a NEW instance of Wave (in Invaders) if you want to make a new wave of
    aliens.

    If you want to pause the game, tell this controller to draw, but do not update.  See
    subcontrollers.py from Lecture 24 for an example.  This class will be similar to
    than one in how it interacts with the main class Invaders.

    #UPDATE ME LATER
    INSTANCE ATTRIBUTES:
        _head:   the snake's head to control [Ship]
        _snake:  the list of the body of the snake in the wave [1d list or None]
        _candy:  the candy for snake
        _time:   The amount of time since the last snake "step" [number >= 0]

    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Invaders. It is okay if you do, but you MAY NOT ACCESS
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that
    you need to access in Invaders.  Only add the getters and setters that you need for
    Invaders. You can keep everything else hidden.

    You may change any of the attributes above as you see fit. For example, may want to
    keep track of the score.  You also might want some label objects to display the score
    and number of lives. If you make changes, please list the changes with the invariants.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    _snakeDirection: which direction the snake is changing into
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self,speed,highscore):
        """
        Initializes the wave

        Parameter speed: The speed the snake are marching in the current game
        Precondition: speed is a float greater than 0
        """
        self._shape = self._pickShape()
        self._determine(self._shape)
        
    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self,direction,dt,game):
        pass
        

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self,view):
        """
        Draws the game objects to the view.
        """
        if self._currentTetriminoObject is not None:
            for part in self._currentTetriminoObject:
                if part is not None:
                    part.draw(view)
           
        

    # HELPER METHODS FOR COLLISION DETECTION

    def _pickShape(self):
        li = [OTetrimino, ITetrimino, TTetrimino, LTetrimino, JTetrimino, STetrimino, ZTetrimino]
        return random.choice(li)

    def _determine(self,shape):
        if (shape == OTetrimino):
            self._initOTetrimino()
        elif (shape == ITetrimino):
            self._initITetrimino()
        elif (shape == TTetrimino):
            self._initTTetrimino()
        elif (shape == LTetrimino):
            self._initLTetrimino()
        elif (shape == JTetrimino):
            self._initJTetrimino()
        elif (shape == STetrimino):
            self._initSTetrimino()
        elif (shape == ZTetrimino):
            self._initZTetrimino()

    def _initOTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH*2)/20)*10
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topLeftOTetrimino = OTetrimino(left,bottom)
        topRightOTetrimino = OTetrimino(left+BLOCK_WIDTH,bottom)
        bottomLeftOTetrimino = OTetrimino(left,bottom-BLOCK_WIDTH)
        topRightOTetrimino = OTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        OTetriminoObject = [topLeftOTetrimino,topRightOTetrimino,bottomLeftOTetrimino,topRightOTetrimino]
        self._currentTetriminoObject = OTetriminoObject

    def _initITetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH*4)/20)*10
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        mostLeftITetrimino = ITetrimino(left,bottom)
        middleLeftITetrimino = ITetrimino(left+BLOCK_WIDTH,bottom)
        middleRightITetrimino = ITetrimino(left+BLOCK_WIDTH*2,bottom)
        mostRightITetrimino = ITetrimino(left+BLOCK_WIDTH*3,bottom)
        ITetriminoObject = [mostLeftITetrimino,middleLeftITetrimino,middleRightITetrimino,mostRightITetrimino]
        self._currentTetriminoObject = ITetriminoObject

    def _initTTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/20)*10
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topTTetrimino = TTetrimino(left,bottom)
        bottomLeftTTetrimino = TTetrimino(left-BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        bottomMiddleTTetrimino = TTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightTTetrimino = TTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        TTetriminoObject = [topTTetrimino,bottomLeftTTetrimino,bottomMiddleTTetrimino,bottomRightTTetrimino]
        self._currentTetriminoObject = TTetriminoObject

    def _initLTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/20)*10
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topLTetrimino = LTetrimino(left+BLOCK_WIDTH,bottom)
        bottomLeftLTetrimino = LTetrimino(left-BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        bottomMiddleLTetrimino = LTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightLTetrimino = LTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        LTetriminoObject = [topLTetrimino,bottomLeftLTetrimino,bottomMiddleLTetrimino,bottomRightLTetrimino]
        self._currentTetriminoObject = LTetriminoObject

    def _initJTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/20)*10
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topJTetrimino = JTetrimino(left-BLOCK_WIDTH,bottom)
        bottomLeftJTetrimino = JTetrimino(left-BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        bottomMiddleJTetrimino = JTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightJTetrimino = JTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        JTetriminoObject = [topJTetrimino,bottomLeftJTetrimino,bottomMiddleJTetrimino,bottomRightJTetrimino]
        self._currentTetriminoObject = JTetriminoObject

    def _initSTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/20)*10
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topLeftSTetrimino = STetrimino(left,bottom)
        topRightSTetrimino = STetrimino(left+BLOCK_WIDTH,bottom)
        bottomLeftSTetrimino = STetrimino(left-BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        bottomRightSTetrimino = STetrimino(left,bottom-BLOCK_WIDTH)
        STetriminoObject = [topLeftSTetrimino,topRightSTetrimino,bottomLeftSTetrimino,bottomRightSTetrimino]
        self._currentTetriminoObject = STetriminoObject

    def _initZTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/20)*10
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topLeftZTetrimino = ZTetrimino(left-BLOCK_WIDTH,bottom)
        topRightZTetrimino = ZTetrimino(left,bottom)
        bottomLeftZTetrimino = ZTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightZTetrimino = ZTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        ZTetriminoObject = [topLeftZTetrimino,topRightZTetrimino,bottomLeftZTetrimino,bottomRightZTetrimino]
        self._currentTetriminoObject = ZTetriminoObject

    