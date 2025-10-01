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

# Track door state (open or closed)
door_open = False

def update():
    global door_open
    
    # Player movement
    direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()

    player.position += direction * time.dt * speed

    # --- Door disappears/reappears ---
    if player.intersects(door).hit:
        if held_keys['e'] and not door_open:  # Open (disappear)
            door.enabled = False
            door_open = True
        elif held_keys['q'] and door_open:    # Close (reappear)
            door.enabled = True
            door_open = False

    # Rotating cube interaction
    if player.intersects(rotating_cube).hit:
        rotating_cube.rotation_y += 100 * time.dt

app.run()
