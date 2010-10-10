# -*- coding: utf-8 -*-
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import *
from math import sqrt, ceil

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------

 
class SplitScreen(object):
    '''
    '''
    def __init__(self, cam_count=0):
        '''
        '''
        self.regions = []   # the regions the screen is separated into
        self.cameras = []   # the cameras (empty ones are None)
        
        if cam_count > 0:
            self.addCameras(cam_count)
            
        #for i in range(1,10):    
        #    print i, self.calculateRegions(i)
        print cam_count
        
    # -----------------------------------------------------------------
    
    def addCamera(self):
        '''
        adds a camera for a new player (or an additional view)
        @return: returns the added camera object
        '''
        unused = self.getUnusedRegion()
        # if there is an unused camera slot, use it
        if unused != -1:
            self.cameras[unused] = self.createCamera(self.regions[unused])
        # if there is no free slot, we have to recalculate the regions
        else:
            self.regions = self.calculateRegions(len(self.regions)+1)
            self.cameras.append(self.createCamera(self.regions[unused]))
            self.refreshCameras()
        
        # if there are empty slots, they're filled with None
            for i in xrange(len(self.regions)-len(self.cameras)):
                self.cameras.append(None)
        
        # if there was an unused slot, the camera is now at this place
        # if not, unused is -1 which points to the last element of the list (the newest cam)
        return self.cameras[unused]

    # -----------------------------------------------------------------
    
    def removeCamera(self):
        '''
        removes a camera out of the list
        '''
##      NOT IMPLEMENTED, YET        
        pass

    # -----------------------------------------------------------------
    
    def addCameras(self, cam_count):
        '''
        adds multiple cameras
        @return: (list) returns all recently added cameras
        '''
        cams = [] # this will be returned
        
        unused = self.getUnusedRegions() # this stores all unused slots
        
        # if there are enough unused camera slots, use it
        if len(unused) >= cam_count:
            for i in unused:
                self.cameras[i] = self.createCamera(self.regions[i])
                self.cams.append(self.cameras[i])
                
        # if there are not enough free slots, we have to recalculate the regions
        else:
            self.regions = self.calculateRegions(len(self.cameras)-len(unused)+cam_count)
            
            # first fill the unused slots
            for i in unused:
                self.cameras[i] = self.createCamera(self.regions[i])
                self.cams.append(self.cameras[i])
                
            # then add all other new cams at the end
            for i in xrange(cam_count-len(unused)):
                cam = self.createCamera(self.regions[i])
                self.cameras.append(cam)
                cams.append(cam)
            
            # if there are empty slots, they're filled with None
            for i in xrange(len(self.regions)-len(self.cameras)):
                self.cameras.append(None)
                
            # refresh all cameras
            self.refreshCameras()
            
        
        return cams # return all added cams

    # -----------------------------------------------------------------
            
    def refreshCameras(self):
        '''
        updates the size of all cameras, when the count of the regions has changed
        '''
        for i in xrange(len(self.cameras)):
            if self.cameras[i] != None:
                self.cameras[i].node().getDisplayRegion(0).setDimensions(self.regions[i][0], self.regions[i][1], self.regions[i][2], self.regions[i][3])
            
    # -----------------------------------------------------------------
    
    def getUnusedRegion(self):
        '''
        looks for an unused region to add a new player into it
        @return: (int) the index of an empty camera region
        '''
        for i in xrange(len(self.cameras)):
            if self.cameras[i] == None:
                return i
        else:
            return -1
    
    # -----------------------------------------------------------------
    
    def getUnusedRegions(self):
        '''
        looks for all unused regions to add a new player into it
        @return: (list) the indices of all empty camera regions
        '''
        unused = []
        
        for i in xrange(len(self.cameras)):
            if self.cameras[i] == None:
                unused.append(i)
                
        return unused
    
    # -----------------------------------------------------------------
    
    def createCamera(self,region):
        '''
        Create one Camera for a new Player
        '''
        camera=base.makeCamera(base.win,displayRegion=region)
        camera.node().getLens().setAspectRatio(3.0/4.0)
        camera.node().getLens().setFov(45) #optional.
        camera.setPos(0,-8,3) #set its position.
        return camera

    # -----------------------------------------------------------------

    def calculateRegions(self, count):
        '''
        Calculates the window size and position for a count of n screens
        @return: (tuple) the display region in panda format (x1,x2,y1,y2) x is left-right, y is bottom-up
        '''
        regions = [] #this list stores the display regions for the several screens
        
        separations = ceil(sqrt(count)) # how often has the screen to be separated?
        
        # this is executed if a squarical order isn't senseful
        if ((separations**2) - separations >= count):
            for y in range(int(separations-1), 0, -1):
                for x in range(1,int(separations+1) ,1):
                    regions.append(((x-1)/separations, x/separations, (y-1)/(separations-1), y/(separations-1) ))
                   
        # this is executed if the player count is near a square number e.g. 9 or 16
        else:
            for y in range(int(separations), 0, -1):
                for x in range(1, int(separations+1) ,1):
                    regions.append(((x-1)/separations, x/separations, (y-1)/separations, y/separations ))
        
        return regions  
 

# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
      
if __name__ == "__main__":
    import main
##    app = ShowBase()
##    
##    split = SplitScreen(1)
##    print "initialisation done"
##    split.addCamera()
##    split.addCamera()
##    split.addCamera()
##    
##    app.run()