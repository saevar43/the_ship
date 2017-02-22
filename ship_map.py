# -*- coding: utf-8 -*-
import ship_scenes

class Map(object):

    scenes = {
        'your_room': ship_scenes.YourRoom(),
        'hallway': ship_scenes.Hallway(),
        'engine_room': ship_scenes.EngineRoom(),
        'bridge': ship_scenes.Bridge(),
        'fight': ship_scenes.Fight(),
        'deck': ship_scenes.Deck(),
        'lifeboat': ship_scenes.LifeBoat(),
        'death': ship_scenes.Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        scene = Map.scenes.get(scene_name)
        return scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)
