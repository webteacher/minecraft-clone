from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# більшість речей в урсині - це сутності. Сутність - це річ, яку ви розміщуєте у світі.
# ви можете думати про них як про GameObjects в Unity або Actors в Unreal.
# перший параметр говорить нам, що модель сутності буде 3d-моделлю, яка називається "куб".
# ursina включає деякі базові моделі, такі як 'cube', 'sphere' та 'quad'.

# наступний параметр вказує нам, що колір моделі має бути помаранчевим.

# 'scale_y=2' вказує нам, наскільки великим має бути об'єкт по вертикальній осі, наскільки він має бути високим.
# в ursina додатні значення x - це праворуч, додатні значення y - вгору, а додатні значення z - вперед.

blocks = [
    load_texture('assets/grass.png'), # 0
    load_texture('assets/grass.png'), # 1
    load_texture('assets/stone.png'), # 2
    load_texture('assets/gold.png'),  # 3
    load_texture('assets/lava.png'),  # 4
]

block_id = 1


class Sky(Entity):
    def __init__(self):
	    super().__init__(
        parent=scene,
        model='sphere',
        texture=load_texture('assets/sky.jpg'),
        scale=500,
        double_sided=True
    )

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='assets/grass.png'):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            scale=0.5
        )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                Voxel(position=self.position + mouse.normal, texture=blocks[block_id])
            elif key == 'right mouse down':
                destroy(self)

for z in range(40):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z))

# create a window
player = FirstPersonController()
# start running the game
sky = Sky()

app.run()