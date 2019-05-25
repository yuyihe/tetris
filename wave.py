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
        self._time = 0
        self._speed = speed
        self._goLeft = False
        self._goRight = False
        self._rotate = False
        self._shape = self._pickShape()
        self._currentTetriminoObject = self._determine(self._shape)
        
    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self,direction,dt,game):
        if self._currentTetriminoObject is not None:           
            self._moveCurrentTetriminoObject(self._currentTetriminoObject,dt,direction)
           
        

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self,view):
        """
        Draws the game objects to the view.
        """
        if self._currentTetriminoObject is not None:
            for part in self._currentTetriminoObject:
                if part is not None:
                    part.draw(view)

    def _moveCurrentTetriminoObject(self,currentTetriminoObject,dt,direction):
        if direction == left:
            self._goLeft = True
        elif direction == right:
            self._goRight = True
        elif direction == up:
            self._rotate = True
        self._time = self._time+dt
        if self._time > self._speed:
            self._time = 0
            for block in currentTetriminoObject:
                block.bottom = block.bottom-BLOCK_WIDTH
                if self._goLeft:
                    block.left = max(block.left-BLOCK_WIDTH,0)
                elif self._goRight:
                    block.left = min(block.left+BLOCK_WIDTH,GAME_WIDTH-BLOCK_WIDTH)
            if self._rotate:
                self._rotateCurrentTetriminoObject(currentTetriminoObject)
            self._goLeft = False           
            self._goRight = False
            self._rotate = False

    def _rotateCurrentTetriminoObject(self,currentTetriminoObject):
        if self._shape == OTetrimino:
            pass
        elif self._shape == ITetrimino:
            self._rotateITetrimino(currentTetriminoObject)
        elif self._shape == TTetrimino:
            self._rotateTTetrimino(currentTetriminoObject)
        elif self._shape == LTetrimino:
            self._rotateLTetrimino(currentTetriminoObject)
        elif self._shape == JTetrimino:
            self._rotateJTetrimino(currentTetriminoObject)
        elif self._shape == STetrimino:
            self._rotateSTetrimino(currentTetriminoObject)
        elif self._shape == ZTetrimino:
            self._rotateZTetrimino(currentTetriminoObject)

    def _rotateITetrimino(self,currentTetriminoObject):
        if currentTetriminoObject[0]._position == 1:
            self._rotateITetrimino1to2(currentTetriminoObject)  
        elif currentTetriminoObject[0]._position == 2:
            self._rotateITetrimino2to1(currentTetriminoObject)

    def _rotateITetrimino1to2(self,currentTetriminoObject):
        currentTetriminoObject[0].left = currentTetriminoObject[0].left+BLOCK_WIDTH
        currentTetriminoObject[0].bottom = currentTetriminoObject[0].bottom+BLOCK_WIDTH
        currentTetriminoObject[2].left = currentTetriminoObject[2].left-BLOCK_WIDTH
        currentTetriminoObject[2].bottom = currentTetriminoObject[2].bottom-BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left-BLOCK_WIDTH*2
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom-BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 2

    def _rotateITetrimino2to1(self,currentTetriminoObject):
        currentTetriminoObject[0].left = currentTetriminoObject[0].left-BLOCK_WIDTH
        currentTetriminoObject[0].bottom = currentTetriminoObject[0].bottom-BLOCK_WIDTH
        currentTetriminoObject[2].left = currentTetriminoObject[2].left+BLOCK_WIDTH
        currentTetriminoObject[2].bottom = currentTetriminoObject[2].bottom+BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left+BLOCK_WIDTH*2
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom+BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 1

    def _rotateTTetrimino(self,currentTetriminoObject):
        if currentTetriminoObject[0]._position == 1:
            self._rotateTTetrimino1to2(currentTetriminoObject)  
        elif currentTetriminoObject[0]._position == 2:
            self._rotateTTetrimino2to3(currentTetriminoObject)
        elif currentTetriminoObject[0]._position == 3:
            self._rotateTTetrimino3to4(currentTetriminoObject) 
        elif currentTetriminoObject[0]._position == 4:
            self._rotateTTetrimino4to1(currentTetriminoObject) 
    
    def _rotateTTetrimino1to2(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left+BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom-BLOCK_WIDTH
        for block in currentTetriminoObject:
            block._position = 2
    
    def _rotateTTetrimino2to3(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left-BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom+BLOCK_WIDTH
        currentTetriminoObject[0].bottom = currentTetriminoObject[0].bottom-BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 3

    def _rotateTTetrimino3to4(self,currentTetriminoObject):
        currentTetriminoObject[0].bottom = currentTetriminoObject[0].bottom+BLOCK_WIDTH*2
        currentTetriminoObject[3].left = currentTetriminoObject[3].left-BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom-BLOCK_WIDTH
        for block in currentTetriminoObject:
            block._position = 4
    
    def _rotateTTetrimino4to1(self,currentTetriminoObject):
        currentTetriminoObject[3].left = currentTetriminoObject[3].left+BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom+BLOCK_WIDTH
        for block in currentTetriminoObject:
            block._position = 1

    def _rotateLTetrimino(self,currentTetriminoObject):
        if currentTetriminoObject[0]._position == 1:
            self._rotateLTetrimino1to2(currentTetriminoObject)  
        elif currentTetriminoObject[0]._position == 2:
            self._rotateLTetrimino2to3(currentTetriminoObject)
        elif currentTetriminoObject[0]._position == 3:
            self._rotateLTetrimino3to4(currentTetriminoObject) 
        elif currentTetriminoObject[0]._position == 4:
            self._rotateLTetrimino4to1(currentTetriminoObject) 
    
    def _rotateLTetrimino1to2(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left+BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom+BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left-BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom-BLOCK_WIDTH
        currentTetriminoObject[0].bottom = currentTetriminoObject[0].bottom-BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 2
    
    def _rotateLTetrimino2to3(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left-BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom-BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left+BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom+BLOCK_WIDTH
        currentTetriminoObject[0].left = currentTetriminoObject[0].left-BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 3

    def _rotateLTetrimino3to4(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left+BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom+BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left-BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom-BLOCK_WIDTH
        currentTetriminoObject[0].bottom = currentTetriminoObject[0].bottom+BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 4
    
    def _rotateLTetrimino4to1(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left-BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom-BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left+BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom+BLOCK_WIDTH
        currentTetriminoObject[0].left = currentTetriminoObject[0].left+BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 1
    
    def _rotateJTetrimino(self,currentTetriminoObject):
        if currentTetriminoObject[0]._position == 1:
            self._rotateJTetrimino1to2(currentTetriminoObject)  
        elif currentTetriminoObject[0]._position == 2:
            self._rotateJTetrimino2to3(currentTetriminoObject)
        elif currentTetriminoObject[0]._position == 3:
            self._rotateJTetrimino3to4(currentTetriminoObject) 
        elif currentTetriminoObject[0]._position == 4:
            self._rotateJTetrimino4to1(currentTetriminoObject) 

    def _rotateJTetrimino1to2(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left+BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom+BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left-BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom-BLOCK_WIDTH
        currentTetriminoObject[0].left = currentTetriminoObject[0].left+BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 2
    
    def _rotateJTetrimino2to3(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left-BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom-BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left+BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom+BLOCK_WIDTH
        currentTetriminoObject[0].bottom = currentTetriminoObject[0].bottom-BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 3

    def _rotateJTetrimino3to4(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left+BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom+BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left-BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom-BLOCK_WIDTH
        currentTetriminoObject[0].left = currentTetriminoObject[0].left-BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 4
    
    def _rotateJTetrimino4to1(self,currentTetriminoObject):
        currentTetriminoObject[1].left = currentTetriminoObject[1].left-BLOCK_WIDTH
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom-BLOCK_WIDTH
        currentTetriminoObject[3].left = currentTetriminoObject[3].left+BLOCK_WIDTH
        currentTetriminoObject[3].bottom = currentTetriminoObject[3].bottom+BLOCK_WIDTH
        currentTetriminoObject[0].bottom = currentTetriminoObject[0].bottom+BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 1
           
    def _rotateSTetrimino(self,currentTetriminoObject):
        if currentTetriminoObject[0]._position == 1:
            self._rotateSTetrimino1to2(currentTetriminoObject)  
        elif currentTetriminoObject[0]._position == 2:
            self._rotateSTetrimino2to1(currentTetriminoObject) 

    def _rotateSTetrimino1to2(self,currentTetriminoObject):
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom-BLOCK_WIDTH*2
        currentTetriminoObject[2].left = currentTetriminoObject[2].left+BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 2
    
    def _rotateSTetrimino2to1(self,currentTetriminoObject):
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom+BLOCK_WIDTH*2
        currentTetriminoObject[2].left = currentTetriminoObject[2].left-BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 1
    
    def _rotateZTetrimino(self,currentTetriminoObject):
        if currentTetriminoObject[0]._position == 1:
            self._rotateZTetrimino1to2(currentTetriminoObject)  
        elif currentTetriminoObject[0]._position == 2:
            self._rotateZTetrimino2to1(currentTetriminoObject) 

    def _rotateZTetrimino1to2(self,currentTetriminoObject):
        currentTetriminoObject[0].left = currentTetriminoObject[0].left+BLOCK_WIDTH*2
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom-BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 2
    
    def _rotateZTetrimino2to1(self,currentTetriminoObject):
        currentTetriminoObject[0].left = currentTetriminoObject[0].left-BLOCK_WIDTH*2
        currentTetriminoObject[1].bottom = currentTetriminoObject[1].bottom+BLOCK_WIDTH*2
        for block in currentTetriminoObject:
            block._position = 1

    # HELPER METHODS FOR COLLISION DETECTION

    def _pickShape(self):
        li = [OTetrimino, ITetrimino, TTetrimino, LTetrimino, JTetrimino, STetrimino, ZTetrimino]
        return random.choice(li)

    def _determine(self,shape):
        if (shape == OTetrimino):
            return self._initOTetrimino()
        elif (shape == ITetrimino):
            return self._initITetrimino()
        elif (shape == TTetrimino):
            return self._initTTetrimino()
        elif (shape == LTetrimino):
            return self._initLTetrimino()
        elif (shape == JTetrimino):
            return self._initJTetrimino()
        elif (shape == STetrimino):
            return self._initSTetrimino()
        elif (shape == ZTetrimino):
            return self._initZTetrimino()

    def _initOTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH*2)/40)*20
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topLeftOTetrimino = OTetrimino(left,bottom)
        topRightOTetrimino = OTetrimino(left+BLOCK_WIDTH,bottom)
        bottomLeftOTetrimino = OTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightOTetrimino = OTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        OTetriminoObject = [topLeftOTetrimino,topRightOTetrimino,bottomLeftOTetrimino,bottomRightOTetrimino]
        return OTetriminoObject

    def _initITetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH*4)/40)*20
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        mostLeftITetrimino = ITetrimino(left,bottom)
        middleLeftITetrimino = ITetrimino(left+BLOCK_WIDTH,bottom)
        middleRightITetrimino = ITetrimino(left+BLOCK_WIDTH*2,bottom)
        mostRightITetrimino = ITetrimino(left+BLOCK_WIDTH*3,bottom)
        ITetriminoObject = [mostLeftITetrimino,middleLeftITetrimino,middleRightITetrimino,mostRightITetrimino]
        return ITetriminoObject

    def _initTTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/40)*20
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topTTetrimino = TTetrimino(left,bottom)
        bottomLeftTTetrimino = TTetrimino(left-BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        bottomMiddleTTetrimino = TTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightTTetrimino = TTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        TTetriminoObject = [topTTetrimino,bottomLeftTTetrimino,bottomMiddleTTetrimino,bottomRightTTetrimino]
        return TTetriminoObject

    def _initLTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/40)*20
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topLTetrimino = LTetrimino(left+BLOCK_WIDTH,bottom)
        bottomLeftLTetrimino = LTetrimino(left-BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        bottomMiddleLTetrimino = LTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightLTetrimino = LTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        LTetriminoObject = [topLTetrimino,bottomLeftLTetrimino,bottomMiddleLTetrimino,bottomRightLTetrimino]
        return LTetriminoObject

    def _initJTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/40)*20
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topJTetrimino = JTetrimino(left-BLOCK_WIDTH,bottom)
        bottomLeftJTetrimino = JTetrimino(left-BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        bottomMiddleJTetrimino = JTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightJTetrimino = JTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        JTetriminoObject = [topJTetrimino,bottomLeftJTetrimino,bottomMiddleJTetrimino,bottomRightJTetrimino]
        return JTetriminoObject

    def _initSTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/40)*20
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topLeftSTetrimino = STetrimino(left,bottom)
        topRightSTetrimino = STetrimino(left+BLOCK_WIDTH,bottom)
        bottomLeftSTetrimino = STetrimino(left-BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        bottomRightSTetrimino = STetrimino(left,bottom-BLOCK_WIDTH)
        STetriminoObject = [topLeftSTetrimino,topRightSTetrimino,bottomLeftSTetrimino,bottomRightSTetrimino]
        return STetriminoObject

    def _initZTetrimino(self):
        left = math.floor((GAME_WIDTH-BLOCK_WIDTH)/40)*20
        bottom = GAME_HEIGHT-TOP_EDGE-BLOCK_WIDTH
        topLeftZTetrimino = ZTetrimino(left-BLOCK_WIDTH,bottom)
        topRightZTetrimino = ZTetrimino(left,bottom)
        bottomLeftZTetrimino = ZTetrimino(left,bottom-BLOCK_WIDTH)
        bottomRightZTetrimino = ZTetrimino(left+BLOCK_WIDTH,bottom-BLOCK_WIDTH)
        ZTetriminoObject = [topLeftZTetrimino,topRightZTetrimino,bottomLeftZTetrimino,bottomRightZTetrimino]
        return ZTetriminoObject

    