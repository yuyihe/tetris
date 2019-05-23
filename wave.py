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
        self._head = self._createHead()
        self._snake = [self._head]
        self._candy = self._createCandy()
        self._boundry = self._createBoundry()
        self._speed = speed
        self._snakeDirection = nothing
        self._time = 0
        self._score = 0
        self._highscore = highscore
        self._scoretext = GLabel(left=0,top=GAME_HEIGHT,
        text='Score: '+str(self._score),font_name='RetroGame')
        self._highscoretext = GLabel(right=GAME_WIDTH,top=GAME_HEIGHT,
        text='High Score: '+str(self._highscore),font_name='RetroGame')
        self._fail = False
    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self,direction,dt,game):
        

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self,view):
        """
        Draws the game objects to the view.
        """
        

    # HELPER METHODS FOR COLLISION DETECTION

    def _pickShape(self):
        li = [OTetrimino, ITetrimino, TTetrimino, LTetrimino, JTetrimino, STetrimino, ZTetrimino]
        return random.choice(li)

    def _determine(self,shape):
        if (shape == OTetrimino):
            self._initOTetrimino()
        elif (shape == ITetrimino):
            self._initITetrimino()
        elif (shape == ITetrimino):
            self._initITetrimino()
        elif (shape == ITetrimino):
            self._initITetrimino()
        elif (shape == ITetrimino):
            self._initITetrimino()

    def _createHead(self):
        """
        Return an object of snake head
        """
        left = GAME_WIDTH/BLOCK_WIDTH//2*BLOCK_WIDTH
        bottom = GAME_HEIGHT/BLOCK_WIDTH//2*BLOCK_WIDTH
        width = BLOCK_WIDTH
        fillcolor = 'green'
        head = Snake(left,bottom,width,width,fillcolor)
        return head

    def _createBody(self,left,bottom):
        """
        Return an object of snake body
        """
        width = BLOCK_WIDTH
        fillcolor = 'green'
        body = Snake(left,bottom,width,width,fillcolor)
        return body

    def _createCandy(self):
        """
        Return an object of candy
        """
        left = random.randint(1,GAME_WIDTH/BLOCK_WIDTH-2)*BLOCK_WIDTH
        bottom = random.randint(1,GAME_HEIGHT/BLOCK_WIDTH-2)*BLOCK_WIDTH
        width = BLOCK_WIDTH
        fillcolor = 'red'
        candy = Candy(left,bottom,width,width,fillcolor)
        if self._candyOnEmptyScreen(candy):
            return candy
        else:
            return self._createCandy()

    def _candyOnEmptyScreen(self,candy):
        """
        Return True if the candy that;s about to be created is on empty screen
        """
        create = True
        for part in self._snake:
            if self._whetherCollides(part,candy):
                create = False
        return create


    def _createBoundry(self):
        """
        Return a list of boundrys
        """
        list = (self._boundryTop()+self._boundryLeft()+
        self._boundryRight()+self._boundryBottom())
        return list

    def _boundryTop(self):
        li = []
        for a in range(int(GAME_WIDTH/BLOCK_WIDTH)):
            left = a*BLOCK_WIDTH
            bottom = GAME_HEIGHT-BLOCK_WIDTH
            width = BLOCK_WIDTH
            fillcolor = 'grey'
            boundry = Boundry(left,bottom,width,width,fillcolor)
            li.append(boundry)
        return li

    def _boundryLeft(self):
        li = []
        for a in range(int(GAME_HEIGHT/BLOCK_WIDTH)):
            left = 0
            bottom = a*BLOCK_WIDTH
            width = BLOCK_WIDTH
            fillcolor = 'grey'
            boundry = Boundry(left,bottom,width,width,fillcolor)
            li.append(boundry)
        li.pop(-1)
        return li

    def _boundryRight(self):
        li = []
        for a in range(int(GAME_HEIGHT/BLOCK_WIDTH)):
            left = GAME_WIDTH-BLOCK_WIDTH
            bottom = a*BLOCK_WIDTH
            width = BLOCK_WIDTH
            fillcolor = 'grey'
            boundry = Boundry(left,bottom,width,width,fillcolor)
            li.append(boundry)
        li.pop(-1)
        return li

    def _boundryBottom(self):
        li = []
        for a in range(int(GAME_WIDTH/BLOCK_WIDTH)):
            left = a*BLOCK_WIDTH
            bottom = 0
            width = BLOCK_WIDTH
            fillcolor = 'grey'
            boundry = Boundry(left,bottom,width,width,fillcolor)
            li.append(boundry)
        li.pop(0)
        li.pop(-1)
        return li

    def _direction(self,direction):
        if direction != nothing:
            if len(self._snake) == 1:
                self._snakeDirection = direction
            elif ((self._snakeDirection == left and direction != right) or
            (self._snakeDirection == right and direction != left) or
            (self._snakeDirection == up and direction != down) or
            (self._snakeDirection == down and direction != up)):
                self._snakeDirection = direction

    def _snakeTime(self,dt):
        """
        Method to move the snake across the screen.
        It determines when and which direction the snake should be moving

        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        self._time = self._time+dt
        if self._time > self._speed:
            self._time = 0
            if self._snakeDirection == left:
                self._snakeGoLeft()
            elif self._snakeDirection == right:
                self._snakeGoRight()
            elif self._snakeDirection == up:
                self._snakeGoUp()
            elif self._snakeDirection == down:
                self._snakeGoDown()

    def _snakeGoLeft(self):
        left = self._head.left-BLOCK_WIDTH
        bottom = self._head.bottom
        a = self._createBody(left,bottom)
        self._snake.insert(0,a)
        if self._whetherCollides(self._candy,self._head):
            self._updateCandyAndScore()
        else:
            self._snake.pop(-1)
        self._updateHead()

    def _snakeGoRight(self):
        left = self._head.left+BLOCK_WIDTH
        bottom = self._head.bottom
        a = self._createBody(left,bottom)
        self._snake.insert(0,a)
        if self._whetherCollides(self._candy,self._head):
            self._updateCandyAndScore()
        else:
            self._snake.pop(-1)
        self._updateHead()

    def _snakeGoUp(self):
        left = self._head.left
        bottom = self._head.bottom+BLOCK_WIDTH
        a = self._createBody(left,bottom)
        self._snake.insert(0,a)
        if self._whetherCollides(self._candy,self._head):
            self._updateCandyAndScore()
        else:
            self._snake.pop(-1)
        self._updateHead()

    def _snakeGoDown(self):
        left = self._head.left
        bottom = self._head.bottom-BLOCK_WIDTH
        a = self._createBody(left,bottom)
        self._snake.insert(0,a)
        if self._whetherCollides(self._candy,self._head):
            self._updateCandyAndScore()
        else:
            self._snake.pop(-1)
        self._updateHead()


    def _whetherCollides(self,a,b):
        x = a.left+BLOCK_WIDTH/2
        y = a.bottom+BLOCK_WIDTH/2
        determine = b.contains((x,y))
        return determine

    def _updateCandyAndScore(self):
        self._candy = self._createCandy()
        self._score = self._score+10
        self._scoretext = GLabel(left=0,top=GAME_HEIGHT,
        text='Score: '+str(self._score),font_name='RetroGame')
        if self._score > self._highscore:
            self._highscore = self._score
            self._highscoretext = GLabel(right=GAME_WIDTH,top=GAME_HEIGHT,
            text='High Score: '+str(self._highscore),font_name='RetroGame')

    def _hitBoundry(self):
        """
        Return whether or not the head of the snake collides with the boundry
        """
        collision = False
        for block in self._boundry:
            if self._whetherCollides(block,self._head):
                collision = True
        return collision

    def _eatItself(self):
        """
        Return True if the snake's head collides with it self(eat itself)
        """
        eat = False
        copy = self._snake.copy()
        copy.pop(0)
        for body in copy:
            if self._whetherCollides(body,self._head):
                eat = True
        return eat
