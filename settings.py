# _*_ coding: UTF-8 _*_
##############################################################
## this module contains a class to save and load the
## application's settings and configuration
##############################################################

from configobj import ConfigObj

# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------

class Settings(object):
    '''
    This class represents a joystick and holds the pygame data
    '''
    def __init__(self):
        '''
        this class is able to load and save the application's settings
        '''

        self.width = 800
        self.height = 600

        self.fullscreen = False

    # ---------------------------------------------------------

    def saveSettings(self, filename):
        '''
        '''
        config = ConfigObj()
        config.filename = filename

        config["application"] = {}
        #config["application"]["resolution"] = "%dx%d"%(self.width, self.height)
        config["application"]["resolution"] = [str(self.width), str(self.height)]
        config["application"]["fullscreen"] = str(int(self.fullscreen))

        config["joysticks"] = {}

        config.write()


    # ---------------------------------------------------------

    def loadSettings(self, filename):
        '''
        '''
        config = ConfigObj(filename)
        #
        self.width = int(config["application"]["resolution"][0])
        self.height = int(config["application"]["resolution"][1])
        self.fullscreen = bool(int(config["application"]["fullscreen"]))

    # ---------------------------------------------------------



# ---------------------------------------------------------
# ---------------------------------------------------------
# ---------------------------------------------------------






if __name__ == "__main__":
    settings = Settings()
    #settings.saveSettings("user/config.ini")
    settings.loadSettings("user/config.ini")
    print settings.fullscreen
    print settings.width, settings.height
