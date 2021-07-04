import pygame, sys, random, os

def ball_animation():
        global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
	
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        #ceiling and floor
        if ball.top <= 0 or ball.bottom >= screen_height:
                ball_speed_y *= -1
                pygame.mixer.Sound.play(plob_sound)

       
	#Player Score
        if ball.left <=0:
                score_time = pygame.time.get_ticks()
                player_score +=1
                pygame.mixer.Sound.play(score_sound)


        #Opponent Score
        if ball.right >= screen_width:
                pygame.mixer.Sound.play(score_sound)
                score_time = pygame.time.get_ticks()
                opponent_score +=1


        if ball.colliderect(player) and ball_speed_x > 0:
                pygame.mixer.Sound.play(plob_sound)
                if abs(ball.right - player.left) < 10:
                        ball_speed_x *= -1
                elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
                        ball_speed_y *= -1
                elif abs(ball.top - player.bottom) < 10 or ball_speed_y < 0:
                        ball_speed_y *= -1
                        


        if ball.colliderect(opponent) and ball_speed_x < 0:
                pygame.mixer.Sound.play(plob_sound)
                if abs(ball.left - opponent.right) < 10:
                        ball_speed_x *= -1
                elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
                        ball_speed_y *= -1
                elif abs(ball.top - player.bottom) < 10 and ball_speed_y > 0:
                        ball_speed_y *= -1
                                


def player_animation():
        player.y += player_speed

        if player.top <= 0:
                player.top = 0
        if player.bottom >= screen_height:
                player.bottom = screen_height

def opponent_ai():
        if opponent.top < ball.y:
                opponent.y += opponent_speed
        if opponent.bottom > ball.y:
                opponent.y -= opponent_speed

        if opponent.top <= 0:
                opponent.top = 0
        if opponent.bottom >= screen_height:
                opponent.bottom = screen_height

def ball_start1():
        global ball_speed_x, ball_speed_y, ball_moving, score_time

        ball.center = (screen_width//2, screen_height//2)
        current_time = pygame.time.get_ticks()


        second3 = 4500
        second2 = 6000
        second1 = 7500
        #Countdown1
        if current_time - score_time < second3:
                number_three = basic_font.render("3",False,light_grey)
                screen.blit(number_three,(screen_width//2 - 10, screen_height//2 - 70))
        if second3 < current_time - score_time < second2:
                number_two = basic_font.render("2",False,light_grey)
                screen.blit(number_two,(screen_width//2 - 10, screen_height//2 - 70))
        if second2 < current_time - score_time < second1:
                number_one = basic_font.render("1",False,light_grey)
                screen.blit(number_one,(screen_width//2 - 10, screen_height//2 - 70))
        if current_time - score_time < second1:
                ball_speed_y, ball_speed_x = 0,0

        else:
                ball_speed_x = 7 * random.choice((1,-1))
                ball_speed_y = 7 * random.choice((1,-1))
                score_time = None

                

def ball_start2():
        global ball_speed_x, ball_speed_y, ball_moving, score_time

        ball.center = (screen_width//2, screen_height//2)
        current_time = pygame.time.get_ticks()
        
        #Countdown2
        if current_time - score_time < 700:
                number_three = basic_font.render("3",False,light_grey)
                screen.blit(number_three,(screen_width//2 - 10, screen_height//2 - 70))
        if 700 < current_time - score_time < 1400:
                number_two = basic_font.render("2",False,light_grey)
                screen.blit(number_two,(screen_width//2 - 10, screen_height//2 - 70))
        if 1400 < current_time - score_time < 2100:
                number_one = basic_font.render("1",False,light_grey)
                screen.blit(number_one,(screen_width//2 - 10, screen_height//2 - 70))

        if current_time - score_time < 2100:
                ball_speed_y, ball_speed_x = 0,0
        else:
                ball_speed_x = 7 * random.choice((1,-1))
                ball_speed_y = 7 * random.choice((1,-1))
                score_time = None

                
def win_screen():
        global win_text, screen_width, screen_height
        
        ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
        player = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10,140)
        opponent = pygame.Rect(10, screen_height // 2 - 70, 10,140)

        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))
        screen.blit(win_text,(screen_width//2 - 125, screen_height//3 ))


        
def lose_screen():
        global win_text, screen_width, screen_height
        
        ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
        player = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10,140)
        opponent = pygame.Rect(10, screen_height // 2 - 70, 10,140)

        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width // 2, 0),(screen_width // 2, screen_height))
        screen.blit(lose_text,(screen_width//2 - 195, screen_height//3 ))





# General setup
pygame.mixer.pre_init(44100,-16,2,512)

screen_width = 1535
screen_height = 650
pos_x = 0
pos_y = screen_height//5
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (pos_x,pos_y)
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')


# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

# Game Rectangles
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height // 2 - 70, 10,140)

# Game Variables
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
ball_moving = False
score_time = True
end = False


#Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)
large_font = pygame.font.Font('freesansbold.ttf', 64)
win_text = large_font.render("You Win",False,light_grey)
lose_text = large_font.render("Game Over",False,light_grey)

# sound 
plob_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")


start_counter = 0
#Big loop
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                                player_speed -= 6
                        if event.key == pygame.K_DOWN:
                                player_speed += 6
                if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                                player_speed += 6
                        if event.key == pygame.K_DOWN:
                                player_speed -= 6
	
	#Game Logic
        ball_animation()
        player_animation()
        opponent_ai()

        # Visuals 
        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (screen_width // 2, 0),(screen_width // 2, screen_height))
        
        if score_time:
                if player_score < 1 and opponent_score < 1:
                                ball_start1()
                elif player_score < 10 and opponent_score < 10:
                                ball_start2()
                                
                else:
                        end = True
                        if player_score >= 10:
                                win_screen()
                        elif opponent_score >= 10:
                                lose_screen()
                        else:
                                win_screen()
                        
                        
        
        player_text = basic_font.render(f'{player_score}', False, light_grey)
        screen.blit(player_text, (screen_width//2 + 30,470))

        opponent_text = basic_font.render(f'{opponent_score}', False, light_grey)
        screen.blit(opponent_text, (screen_width//2 - 45,470))

        pygame.display.flip()
        clock.tick(60)

        

        while end:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        
                




        
