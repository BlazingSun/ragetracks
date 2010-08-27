# _*_ coding: UTF-8 _*_
###################################################################
## this module is the main one, which contains the game class
###################################################################

from direct.showbase.ShowBase import ShowBase
import menu
import settings

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------

class Game(ShowBase):
    '''
    '''
    def __init__(self):
        '''
        '''
        ShowBase.__init__(self)

        # try to read the ini-file. If it fails the settings class
        # automatically contains default values
        self.settings = settings.Settings()
        try:
            self.settings.loadSettings("user/config.ini")
        except:
            pass    # so here is nothing to do


        # Add the main menu (though this is only temporary:
        # the menu should me a member-variable, not a local one)
        m = menu.Menu()
        m.addOption("New Game", self.newGame)

    # -----------------------------------------------------------------

    def newGame(self):
        '''
        starts the game or goes to the next menu
        '''
        pass
        print "foo"

    # -----------------------------------------------------------------

    def gametask(self):
        '''
        this task runs once per second if the game is running
        '''
        pass

    # -----------------------------------------------------------------

    def menutask(self):
        '''
        this task runs once per second if we are in game menu
        '''
        pass

    # -----------------------------------------------------------------

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------

# this code is only executed if the module is executed and not imported
if __name__ == "__main__":
    game = Game()
    game.run()




