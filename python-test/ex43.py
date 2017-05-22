
class Engine(object):
    def __init__(self, map):
        self.scene_map = map


    def play(self):
        current_scene = self.scene_map.opening_scene() #Scene object
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # run through the finished scene
        current_scene.enter()

class Scene(object):
    def enter(self):
        print ""
        print "*** Scene ***"


class Death(Scene):
    def enter(self): #this will override parent memeber function
        super(Death, self).enter()
        print "enter: Death"
        return "finished"


class CentralCorridor(Scene):
    def enter(self):
        print "enter: Centrol Corridor"
        return "laser_weapon_armory"

class LaserWeaponArmory(Scene):
    def enter(self):
        print "enter: Laser Weapon Armory"
        return "the_bridge"

class TheBridge(Scene):
    def enter(self):
        print "enter: The Bridge"
        return "escape_pod"


class EscapePod(Scene):
    def enter(self):
        print "enter: Escape Pod"
        return "death"

class Finished(Scene):
    def enter(self):
        print "enter: Finished"

class Map(object):

    # Give a map of all scenes => in dictionary {name:object, ...}
    # How the current scene  will enter the next scene
    # => is decided in each scene, scenarios-based
    scenes = { #scenes is a class variable to store a dict for the mapping
               # of the scene-name to Scene object
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "the_bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "death": Death(),
        "finished": Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene # a string for the start scene

    def opening_scene(self): # pass a string, return the Scene object
        val = self.next_scene(self.start_scene)
        return val

    def next_scene(self, scene_name): #Give a scene_name, pass a Scene object
        val = Map.scenes.get(scene_name)
        return val

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
