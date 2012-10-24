from panda3d.core import BitMask32
from panda3d.core import PointLight
from panda3d.core import VBase4


class Camera:
    """Does camera set up - will probably end up with lots of options."""
    def __init__(self, manager, xml):
        base.camNode.setCameraMask(BitMask32.bit(0))
        #only temporary while testing
        self.plight = PointLight('plight')
        bright = 2
        self.plight.setColor(VBase4(bright, bright, bright, 1))
        #self.plight.setAttenuation(Point3(0, 0, 0.5))
        plnp = base.camera.attachNewNode(self.plight)
        #plnp.setPos(0, 0, 0)
        render.setLight(plnp)

        #base.disableMouse()
        self.reload(manager, xml)

    def reload(self, manager, xml):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def destroy(self):
        pass
