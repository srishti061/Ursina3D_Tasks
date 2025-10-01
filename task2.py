from ursina import *

app = Ursina()

# Ground
ground = Entity(model='plane', scale=20, color=color.green, collider='box')

# Interactive cube
cube = Entity(model='cube', color=color.azure, scale=2, position=(3,1,0), collider='box')

# Player (orange box as character)
player = Entity(model='cube', color=color.orange, scale_y=2, collider='box')

# Attach camera to player
camera.parent = player
camera.position = (0,1.5,-5)
camera.rotation = (10,0,0)

speed = 5  # movement speed

def update():
    # Player movement with WASD
    direction = Vec3(
        held_keys['d'] - held_keys['a'],   # right - left
        0,
        held_keys['w'] - held_keys['s']    # forward - backward
    ).normalized()

    player.position += direction * time.dt * speed

    # Check if player touches the cube
    if player.intersects(cube).hit:
        cube.color = color.red   # change color when touched
    else:
        cube.color = color.azure

app.run()
