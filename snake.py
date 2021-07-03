import pygame
import time
import random
# Initialize pygame modules
pygame.init()

# Create a screen
screen_width=600
screen_height=400
screen=pygame.display.set_mode((screen_width,screen_height))

#Update the screen
pygame.display.update()

pygame.display.set_caption("Welcome to Snake Game")

# Declare colors
snake_color=(101,53,15)
food_color=(210,20,4)
word_color=(49,51,48)
background_color=(150,255,152)

# Declare speed and size of snake 
snake_size=10
snake_speed=15

clock=pygame.time.Clock()

font=pygame.font.SysFont('mistral',30)

# Message to display whether player lost or won
def message(msg,color):
    a = font.render(msg, True, color)
    screen.blit(a, [screen_width/6, screen_height/3])


def snake(snake_size,snake_list):
    for i in snake_list:
        # Create a snake: Using draw.rect(surface,color,[x-coordinate,y-coordinate,length,breadth]]) function
        pygame.draw.rect(screen,snake_color,[i[0],i[1],snake_size,snake_size])

# To display the score on screen
def score(length):
    a = font.render("Your score: {}".format(length-1), True, word_color)
    screen.blit(a, [0,0])


def game():
    game_over=False
    game_close=False
    
    # Position of snake
    #Initial posiiton of snake
    x=200
    y=100
    #Change in position
    x1=0
    y1=0

    # Define a snake
    snake_list=[]
    length=1

    # Add food
    food_x=round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
    food_y=round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0

    while not game_over:
        # To play again
        while game_close==True:
            screen.fill(background_color)
            message("Game Over! Press Q to Quit or P to Play Again",word_color)
            pygame.display.update()

            for i in pygame.event.get():
                # To quit or continue the game
                if i.type==pygame.KEYDOWN:
                    if i.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if i.key==pygame.K_p:
                        game()
    
        for i in pygame.event.get():
            # To close the screen when we click Quit 
            if i.type==pygame.QUIT:
                game_over=True
            # To move the snake using keys
            if i.type==pygame.KEYDOWN:
                if i.key==pygame.K_LEFT:
                    x1=-snake_size
                    y1=0  
                elif i.key==pygame.K_RIGHT:
                    x1=snake_size
                    y1=0
                elif i.key==pygame.K_UP:
                    x1=0
                    y1=-snake_size
                elif i.key==pygame.K_DOWN:
                    x1=0
                    y1=snake_size

        # If snake hits the boundaries            
        if x<0 or x>=screen_width or y<0 or y>=screen_height:
            game_close=True

        x=x+x1
        y=y+y1

        screen.fill(background_color)
        pygame.draw.rect(screen,food_color,[food_x,food_y,snake_size,snake_size])
        #pygame.draw.rect(screen,green,[x,y,snake_size,snake_size])
        
        snake_head=[]
        snake_head.append(x)
        snake_head.append(y)

        snake_list.append(snake_head)

        if len(snake_list)> length:
            del snake_list[0]


        # If snake's head touch its body
        for i in snake_list[:-1]:
            if i== snake_head:
                game_close=True
        
        snake(snake_size,snake_list)
        score(length)
        pygame.display.update()

        if x==food_x and y==food_y:
            # When snake eats food. Add a new food in different location
            food_x=round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
            food_y=round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
            #message("Yummy:)",word_color)
            length=length+1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game()
