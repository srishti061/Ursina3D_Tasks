from ursina import *

app = Ursina()

# Ground
ground = Entity(model='plane', scale=30, color=color.green, collider='box')

# Interactive objects
door = Entity(model='cube', color=color.brown, scale=(1,2,0.2), position=(5,1,0), collider='box')  # smaller door
rotating_cube = Entity(model='cube', color=color.azure, scale=2, position=(-4,1,0), collider='box')

# Player
player = Entity(model='cube', color=color.orange, scale_y=2, collider='box')
camera.parent = player
camera.position = (0,1.5,-6)
camera.rotation = (10,0,0)

speed = 5

# Lighting
DirectionalLight().look_at(Vec3(1,-1,-1))
AmbientLight(color=color.rgba(100,100,100,0.5))

# Track door state
door_open = False

def update():
    # Player movement
    direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()
    player.position += direction * time.dt * speed

    # Rotating cube interaction
    if player.intersects(rotating_cube).hit:
        rotating_cube.rotation_y += 100 * time.dt

def input(key):
    global door_open
    if player.intersects(door).hit:
        if key == 'e' and not door_open:
            door.enabled = False
            door_open = True
        elif key == 'q' and door_open:
            door.enabled = True
            door_open = False

app.run()
