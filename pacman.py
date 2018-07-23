import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 576))  # display update #1366 X 768
done = False
x = 0  # pacman x coordinate
y = 0  # pacman y coor.

frame_list = [pygame.transform.scale(pygame.image.load("frame1.png"), (30, 30)),
              pygame.transform.scale(pygame.image.load("frame2.png"), (30, 30)),
              pygame.transform.scale(pygame.image.load("frame3.png"), (30, 30))]
# pacman의 사진들

# 변수 = pygame.transform.scale(image, (x, y))

current_frame = 0  	# the frame we're currently displaying
num_frames = 3  	# number of frames in the animation

def update():
    global current_frame
    global num_frames
    global pacman
    pacman = frame_list[current_frame]  # set the current frame
    current_frame = (current_frame + 1) % num_frames

def right():
    global x
    x += 10

while not done:  # 게임이 돌아갈 때 한 프레임을 보여준다
    # 4 프레임 : 1초 4번 화면 업데이트
    # -> 0.25초에 한번씩 화면 업데이트

    pygame.time.delay(150)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(pygame.Color("black"))
    right()  # move right
    update()  # pacman animation
    screen.blit(pacman, (x, y))  # image draw
    pygame.display.flip()  # update the display