from panda3d.core import Vec3, Point3, Quat, BitMask32
from panda3d.bullet import BulletCapsuleShape, BulletBoxShape, BulletRigidBodyNode

import math


class Player:
    """A Player class - doesn't actually do that much, just arranges collision detection and provides a camera mount point, plus an interface for the controls to work with. All configured of course."""
    def __init__(self, xml):
        self.reload(xml)

    def reload(self, xml):
        shape2 = BulletBoxShape(Vec3(1, 1, 2))
        self.playernode = BulletRigidBodyNode('Earth')
        self.playernode.setMass(100.0)
        self.playernode.addShape(shape2)
        self.playernp = render.attachNewNode(self.playernode)
        self.playernp.setPos(25, 0, 0)
        manager.physics.getWorld().attachRigidBody(self.playernode)

        manager.physics.registerPreFunc("playerController", self.update)

        #ask the universe where to put the player
        self.__currentPos = manager.universe.getSpawnPoint()

    def start(self):
        events.triggerEvent("playerspawn", self.movementParent.getPos())
        pass

    def stop(self):
        pass

    def destroy(self):
        pass

    def update(self):
        pass
