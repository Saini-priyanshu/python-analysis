import pgzrun

music.play('bgm')
music.set_volume(5)

b=Rect((50,50),(50,25))
vx,vy=3,2

def draw():
    screen.fill('purple')
    screen.draw.filled_rect(b,'pink')

def update():
    global vx,vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx= -vx
        sounds.s1.play()
    if b.bottom > 600 or b.top < 0:
        vy= -vy
        sounds.s1.play()

pgzrun.go()