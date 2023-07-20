import pygame
import random
pygame.init()
white =(255,255,255)
red =(255,0,0)
blue =(25,123,100)
gameWindow = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake by Ayan")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen( text, color, x, y):
    screen_text =font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list , snake_size):
    for x,y in snk_list :
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((100,200,225))
        text_screen("Welcome to Snakes",blue,230,250)
        text_screen("Press space bar to play", blue, 200, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open ("highscore.txt", "r") as f:
        highscore =f.read()
    food_x = random.randint(20, 600 / 2)
    food_y = random.randint(20, 400 / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            text_screen("Game over! press Enter To Continue", red, 90, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                     welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                       velocity_x = init_velocity
                       velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(20, 600/2)
                food_y = random.randint(20, 400/2)
                snk_length +=5
                if score>int(highscore):
                    highscore = score

            gameWindow.fill(white)
            text_screen("Score: " + str(score) + "  highscore: "+ str(highscore), (205,145,225), 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append( snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length :
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>600 or snake_y<0 or snake_y>400:
                game_over = True
            plot_snake(gameWindow, blue, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()


