from ursina import *

app = Ursina()

cube = Entity(model='cube', color=color.azure, scale=2)

def update():
    cube.rotation_y += 1

app.run()
