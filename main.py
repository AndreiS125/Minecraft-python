from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import data
c = True
now_map=data.map1


def update():
    global c
    if held_keys['1'] and c == False:
        c = True
    bot.chase()
    if held_keys['2'] and c:
        c = False
    if held_keys['escape']:
        mouse.locked=False

    if held_keys['control']:
        player.speed = 10
    else:
        player.speed = 5

    if c:
        player.gravity = 0
        if held_keys['space']:
            player.y += player.speed * time.dt
        if held_keys['shift']:
            player.y -= player.speed * time.dt
    else:
        player.gravity = 1





class Bot(Button):
    def __init__(self, position=(1, 0, 1)):
        super().__init__(
            parent=scene,
            position=position,
            origin_y=0.5,
            model='cube',
            texture='brick',
            scale=(1,2,1),
            color=color.red,
            highlight_color=color.lime)
        self.speed=1
    def chase(self):
        if player.x>self.x:
            self.x+=self.speed*time.dt
        else:
            self.x -= self.speed * time.dt
        if player.z > self.z:
            self.z += self.speed * time.dt
        else:
            self.z -= self.speed * time.dt


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='brick',
            color=color.orange,
            highlight_color=color.lime)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)


app = Ursina()
Sky(color=color.red)

for z in range(30):
    for x in range(30):
        for y in range(1):
            voxel = Voxel((x, -y, z))
for z in range(30):
    for x in range(3):
        voxel = Voxel((z, x+1, 0))
        voxel = Voxel((z, x+1, 29))
for z in range(30):
    for x in range(3):
        voxel = Voxel((0, x+1, z))
        voxel = Voxel((29, x+1, z))
player = FirstPersonController()
bot= Bot((2,1,2))
app.run()
