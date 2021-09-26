from tkinter import *
import time
import random
WIDTH = 295
HEIGHT = 520
root = Tk()
character_W = 50
character_H = 70
platform_H = 10
platform_W = 59
root.title('Jumping Fishbear')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)
background = PhotoImage(file='backpng.png')
header = PhotoImage(file='headerpng.png')
char = PhotoImage(file='charpng.png')
platpng = PhotoImage(file='platpng.png')
heartpng = PhotoImage(file='life.png')
root.iconphoto(True, header)
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='black', bd=0, highlightthickness=0)
canvas.create_image(0, 0, image=background, anchor=NW)
canvas.pack()
character = canvas.create_image(0, 355, image=char, anchor=NW)
score = 0
speed = 25
gravity_moved = 0
stamina = 30
hit = False
jump_platform = 0
landing_platform = 0
repeat = 0
helps = 5


class Platform:
    def __init__(self, x, y):
        self.platform = canvas.create_image(x, y, image=platpng, anchor=NW)

    def move(self, amount):
        canvas.move(self.platform, 0, amount)

    def coords(self):
        coord_list_core = canvas.coords(self.platform)
        coord_list_core.append(coord_list_core[0] + platform_W)
        coord_list_core.append(coord_list_core[1] + platform_H)
        return coord_list_core


class Heart:
    def __init__(self, x, y):
        self.heart = canvas.create_image(x, y, image=heartpng, anchor=NW, tag='heart')
        pass


a1 = random.randint(0, 37)  # starting platforms
a2 = random.randint(444, 520)
b1 = random.randint(0, 37)
b2 = random.randint(358, 434)
c1 = random.randint(96, 133)
c2 = random.randint(444, 520)
d1 = random.randint(96, 133)
d2 = random.randint(358, 434)
e1 = random.randint(192, 229)
e2 = random.randint(444, 520)
f1 = random.randint(192, 229)
f2 = random.randint(358, 434)
g1 = random.randint(0, 37)
g2 = random.randint(272, 348)
h1 = random.randint(0, 37)
h2 = random.randint(186, 262)
i1 = random.randint(96, 133)
i2 = random.randint(272, 348)
j1 = random.randint(96, 133)
j2 = random.randint(186, 262)
k1 = random.randint(192, 229)
k2 = random.randint(272, 348)
l1 = random.randint(192, 229)
l2 = random.randint(186, 262)
m1 = random.randint(0, 37)
m2 = random.randint(100, 176)
n1 = random.randint(0, 37)
n2 = random.randint(14, 90)
o1 = random.randint(100, 133)
o2 = random.randint(100, 176)
p1 = random.randint(96, 133)
p2 = random.randint(14, 90)
q1 = random.randint(192, 229)
q2 = random.randint(100, 176)
r1 = random.randint(192, 229)
r2 = random.randint(14, 90)
spawn_1 = Platform(a1, a2)
spawn_2 = Platform(b1, b2)
spawn_3 = Platform(c1, c2)
spawn_4 = Platform(d1, d2)
spawn_5 = Platform(e1, e2)
spawn_6 = Platform(f1, f2)
spawn_7 = Platform(g1, g2)
spawn_8 = Platform(h1, h2)
spawn_9 = Platform(i1, i2)
spawn_10 = Platform(j1, j2)
spawn_11 = Platform(k1, k2)
spawn_12 = Platform(l1, l2)
spawn_13 = Platform(m1, m2)
spawn_14 = Platform(n1, n2)
spawn_15 = Platform(o1, o2)
spawn_16 = Platform(p1, p2)
spawn_17 = Platform(q1, q2)
spawn_18 = Platform(r1, r2)
platforms = [spawn_1, spawn_2, spawn_3, spawn_4, spawn_5, spawn_6, spawn_7, spawn_8, spawn_9, spawn_10, spawn_11,
             spawn_12, spawn_13, spawn_14, spawn_15, spawn_16, spawn_17, spawn_18]


def spawn_platform():
    spawn_chance = random.randint(0, 92)
    a1 = random.randint(0, 37)
    a2 = random.randint(-30, 0)
    c1 = random.randint(96, 133)
    c2 = random.randint(-46, 0)
    e1 = random.randint(192, 229)
    e2 = random.randint(-96, 7)
    if spawn_chance > 90:
        platform1 = Platform(a1, a2)
        platform2 = Platform(c1, c2)
        platform3 = Platform(e1, e2)
        platforms.append(platform1)
        platforms.append(platform2)
        platforms.append(platform3)
    if 60 > spawn_chance > 40:
        platform1 = Platform(a1, a2)
        platform2 = Platform(c1, c2)
        platforms.append(platform1)
        platforms.append(platform2)
    if 40 > spawn_chance > 20:
        platform2 = Platform(c1, c2)
        platform3 = Platform(e1, e2)
        platforms.append(platform2)
        platforms.append(platform3)
    if 20 > spawn_chance > 0:
        platform1 = Platform(a1, a2)
        platform3 = Platform(e1, e2)
        platforms.append(platform1)
        platforms.append(platform3)
    if 70 > spawn_chance > 60:
        platform1 = Platform(a1, a2)
        platforms.append(platform1)
    if 80 > spawn_chance > 70:
        platform2 = Platform(c1, c2)
        platforms.append(platform2)
    if 90 > spawn_chance > 80:
        platform3 = Platform(e1, e2)
        platforms.append(platform3)


def platform_move(move, plat):
    global platforms
    global score
    moved = 0
    while move > 0 and (canvas.coords(character)[1] + character_H) < 450:
        if moved >= 60:
            moved = 0
            spawn_platform()
        coords = Platform.coords(plat)
        if coords[1] >= 400:
            break
        time.sleep(0.001)
        for platform in platforms:
            plat_list = platform.coords()
            platform.move(4.5)
            root.update()
            if plat_list[1] >= 520:
                canvas.delete(platform)
                try:
                    platforms.remove(platform)
                except:
                    pass
                score += 1
        canvas.move(character, 0, 4.5)
        move -= 4.5
        moved += 4.2


def platform_hit():
    global hit
    global landing_platform
    for platform in platforms:
        coords_list = platform.coords()
        if coords_list[0]+10 <= canvas.coords(character)[0] <= coords_list[2]+10:
            if (coords_list[1]-5) <= (canvas.coords(character)[1] + character_H) <= (coords_list[3]+5):
                hit = True
                landing_platform = platform
                return platform
        if coords_list[0]-10 <= (canvas.coords(character)[0] + character_W) <= coords_list[2]+10:
            if (coords_list[1]-5) <= (canvas.coords(character)[1] + character_H) <= (coords_list[3]+5):
                hit = True
                landing_platform = platform
                return platform


def gravity():
    global hit
    global gravity_moved
    global jump_platform
    platform = platform_hit()
    if ((canvas.coords(character)[1] + character_H) + 2 + (gravity_moved / 1000)) < HEIGHT and hit is not True:
        canvas.move(character, 0, 2 + (gravity_moved / 10))
        if gravity_moved < 100:
            gravity_moved += 2
        root.after(9, gravity)
    elif hit:
        hit = False
        gravity_moved = 0
        jump()
        help()
        jump_platform = platform
        try:
            if canvas.coords(character)[1] <= 410:
                move = -((canvas.coords(character)[1] + character_H) - 520)
                platform_move(move, platform)
        except IndexError:
            pass
    else:
        canvas.move(character, 0, HEIGHT - (canvas.coords(character)[1] + character_H))
        gravity_moved = 0
        gameover()


def gameover():
    root.unbind('<d>')
    root.unbind('<a>')
    canvas.delete('all')
    canvas.create_image(0, 0, image=background, anchor=NW)
    canvas.create_text(145, 100, text='G A M E  O V E R', fill='#d91919', font=('Arial',20))
    canvas.create_text(145, 190, text=f'SCORE ={score}', fill='#9c19d9', font=('Arial',20))


def help_counter():
    global helps
    if helps == 0:
        gameover()
    else:
        num = int(helps)
        while num > 0:
            num -= 1
            x = num * 20
            y = 0
            Heart(x, y)


def help():
    global jump_platform
    global landing_platform
    global repeat
    global helps
    if jump_platform == landing_platform:
        repeat += 1
        if repeat == 6:
            repeat = 0
            helps -= 1
            canvas.delete('heart')
            spawn_19 = Platform(random.randint(0, WIDTH-platform_W), 315)
            platforms.append(spawn_19)
            help_counter()


def jump():
    global stamina
    try:
        if canvas.coords(character)[1]-(2 + (stamina / 4)) > 0:
            if stamina >= 0 and canvas:
                canvas.move(character, 0, -(2 + (stamina / 4)))
                stamina -= 1
                root.after(13, jump)
            else:
                stamina = 30
                root.after(90, gravity)
        else:
            stamina = 30
            root.after(90, gravity)
    except IndexError:
        pass


def right(event):
    if (canvas.coords(character)[0] + character_W + speed) <= WIDTH:
        canvas.move(character, speed, 0)


def left(event):
    if (canvas.coords(character)[0] - speed) >= 0:
        canvas.move(character, -speed, 0)


gravity()
help_counter()
root.bind('<d>', right)
root.bind('<a>', left)
root.mainloop()
