"""
Models module for Alien Invaders

This module contains the model classes for the Alien Invaders game. Anything that you
interact with on the screen is model: the ship, the laser bolts, and the aliens.

Just because something is a model does not mean there has to be a special class for
it.  Unless you need something special for your extra gameplay features, Ship and Aliens
could just be an instance of GImage that you move across the screen. You only need a new
class when you add extra features to an object. So technically Bolt, which has a velocity,
is really the only model that needs to have its own class.

With that said, we have included the subclasses for Ship and Aliens.  That is because
there are a lot of constants in consts.py for initializing the objects, and you might
want to add a custom initializer.  With that said, feel free to keep the pass underneath
the class definitions if you do not want to do that.

You are free to add even more models to this module.  You may wish to do this when you
add new features to your game, such as power-ups.  If you are unsure about whether to
make a new class or not, please ask on Piazza.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from consts import *
from game2d import *

# PRIMARY RULE: Models are not allowed to access anything in any module other than
# consts.py.  If you need extra information from Gameplay, then it should be
# a parameter in your method, and Wave should pass it as a argument when it
# calls the method.


class OTetrimino(GRectangle):
    """
    A class to represent a OTetrimino.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self,left,bottom):
        super().__init__(left=left,bottom=bottom,width=BLOCK_WIDTH,height=BLOCK_WIDTH,fillcolor='yellow',linecolor='black')
        self._position = 1

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def collides(self,block):
        blx = block.left+0.01
        bly = block.bottom-0.01
        brx = block.left+BLOCK_WIDTH-0.01
        bry = block.bottom-0.01
        return (self.contains((blx,bly)) or self.contains((brx,bry)))
    
    def leftRestricted(self,block):
        btx = block.left-0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left-0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

    def rightRestricted(self,block):
        btx = block.left+BLOCK_WIDTH+0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left+BLOCK_WIDTH+0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))


class ITetrimino(GRectangle):
    """
    A class to represent a ITetrimino.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self,left,bottom):
        super().__init__(left=left,bottom=bottom,width=BLOCK_WIDTH,height=BLOCK_WIDTH,fillcolor='cyan',linecolor='black')
        self._position = 1
    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def collides(self,block):
        blx = block.left+0.01
        bly = block.bottom-0.01
        brx = block.left+BLOCK_WIDTH-0.01
        bry = block.bottom-0.01
        return (self.contains((blx,bly)) or self.contains((brx,bry)))

    def leftRestricted(self,block):
        btx = block.left-0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left-0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

    def rightRestricted(self,block):
        btx = block.left+BLOCK_WIDTH+0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left+BLOCK_WIDTH+0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

class TTetrimino(GRectangle):
    """
    A class to represent a TTetrimino.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self,left,bottom):
        super().__init__(left=left,bottom=bottom,width=BLOCK_WIDTH,height=BLOCK_WIDTH,fillcolor='pink',linecolor='black')
        self._position = 1

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def collides(self,block):
        blx = block.left+0.01
        bly = block.bottom-0.01
        brx = block.left+BLOCK_WIDTH-0.01
        bry = block.bottom-0.01
        return (self.contains((blx,bly)) or self.contains((brx,bry)))

    def leftRestricted(self,block):
        btx = block.left-0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left-0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

    def rightRestricted(self,block):
        btx = block.left+BLOCK_WIDTH+0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left+BLOCK_WIDTH+0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

class LTetrimino(GRectangle):
    """
    A class to represent a LTetrimino.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self,left,bottom):
        super().__init__(left=left,bottom=bottom,width=BLOCK_WIDTH,height=BLOCK_WIDTH,fillcolor='orange',linecolor='black')
        self._position = 1

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def collides(self,block):
        blx = block.left+0.01
        bly = block.bottom-0.01
        brx = block.left+BLOCK_WIDTH-0.01
        bry = block.bottom-0.01
        return (self.contains((blx,bly)) or self.contains((brx,bry)))

    def leftRestricted(self,block):
        btx = block.left-0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left-0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

    def rightRestricted(self,block):
        btx = block.left+BLOCK_WIDTH+0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left+BLOCK_WIDTH+0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

class JTetrimino(GRectangle):
    """
    A class to represent a JTetrimino.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self,left,bottom):
        super().__init__(left=left,bottom=bottom,width=BLOCK_WIDTH,height=BLOCK_WIDTH,fillcolor='blue',linecolor='black')
        self._position = 1

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def collides(self,block):
        blx = block.left+0.01
        bly = block.bottom-0.01
        brx = block.left+BLOCK_WIDTH-0.01
        bry = block.bottom-0.01
        return (self.contains((blx,bly)) or self.contains((brx,bry)))

    def leftRestricted(self,block):
        btx = block.left-0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left-0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

    def rightRestricted(self,block):
        btx = block.left+BLOCK_WIDTH+0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left+BLOCK_WIDTH+0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

class STetrimino(GRectangle):
    """
    A class to represent a STetrimino.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self,left,bottom):
        super().__init__(left=left,bottom=bottom,width=BLOCK_WIDTH,height=BLOCK_WIDTH,fillcolor='green',linecolor='black')
        self._position = 1

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def collides(self,block):
        blx = block.left+0.01
        bly = block.bottom-0.01
        brx = block.left+BLOCK_WIDTH-0.01
        bry = block.bottom-0.01
        return (self.contains((blx,bly)) or self.contains((brx,bry)))

    def leftRestricted(self,block):
        btx = block.left-0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left-0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

    def rightRestricted(self,block):
        btx = block.left+BLOCK_WIDTH+0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left+BLOCK_WIDTH+0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

class ZTetrimino(GRectangle):
    """
    A class to represent a ZTetrimino.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self,left,bottom):
        super().__init__(left=left,bottom=bottom,width=BLOCK_WIDTH,height=BLOCK_WIDTH,fillcolor='red',linecolor='black')
        self._position = 1

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY
    def collides(self,block):
        blx = block.left+0.01
        bly = block.bottom-0.01
        brx = block.left+BLOCK_WIDTH-0.01
        bry = block.bottom-0.01
        return (self.contains((blx,bly)) or self.contains((brx,bry)))

    def leftRestricted(self,block):
        btx = block.left-0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left-0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))

    def rightRestricted(self,block):
        btx = block.left+BLOCK_WIDTH+0.01
        bty = block.bottom+BLOCK_WIDTH-0.01
        bbx = block.left+BLOCK_WIDTH+0.01
        bby = block.bottom-0.01
        return (self.contains((btx,bty)) or self.contains((bbx,bby)))


