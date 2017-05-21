
class Engine(object):
    def __init__(self, map):
        pass
    def play(self):
        pass

class Map(object):

    # Give a map of all scenes => in dictionary {name:object, ...}
    # How to current scene  will enter the next scene
    # => is decided in each scene, scenarios-based

    def __init__(self, start_scene):
        pass
    def opening_scene(self):
        pass
    def next_scene(self, scene_name):
        pass

class Scene(object):
    def enter(self):
        pass


class Death(Scene):
    def enter(self): #this will override parent memeber function
        pass


class CentralCorridor(Scene):
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass


class EscapePod(Scene):
    def enter(self):
        pass



a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
