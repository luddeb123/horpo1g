import pygame

def main():
    path = """???"""
    Highscore = open(path, 'r')
    highscore = Highscore.read()
    buttonWidth = 256
    buttonWidth2 = 262
    buttonHight = 64
    buttonHight2 = 70
    screenHight = 480
    screenWidth = 640
    pygame.init()
    font = pygame.font.SysFont('vgasys', 50)
    clock = pygame.time.Clock()
    fps = 60
    size = [screenWidth, screenHight]

    screen = pygame.display.set_mode(size)

    button1 = pygame.Rect((screenWidth/2)-(buttonWidth/2),(screenHight/4)*2, buttonWidth, buttonHight)
    button1_1 = pygame.Rect((screenWidth/2)-(buttonWidth2/2),((screenHight/4)*2)-3, buttonWidth2, buttonHight2)
    button2 = pygame.Rect((screenWidth/2)-(buttonWidth/2),(screenHight/4)*3, buttonWidth,buttonHight)
    button2_1 = pygame.Rect((screenWidth/2)-(buttonWidth2/2),((screenHight/4)*3)-3, buttonWidth2, buttonHight2)

    # creates a rect object
    # The rect method is similar to a list but with a few added perks
    # for example if you want the position of the button you can simpy type
    # button.x or button.y or if you want size you can type button.width or
    # height. you can also get the top, left, right and bottom of an object
    # with button.right, left, top, and bottom

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() # gets mouse position

                # checks if mouse position is over the button
                # note this method is constantly looking for collisions
                # the only reason you dont see an evet activated when you
                # hover over the button is because the method is bellow the
                # mousedown event if it were outside it would be called the
                # the moment the mouse hovers over the button

                if button1.collidepoint(mouse_pos): # play button
                    # pritns current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                if button2.collidepoint(mouse_pos): # exit button
                    pygame.quit()
                    # pritns current location of mouse
                    print('button was pressed at {0} \n '.format(mouse_pos))

        pygame.draw.rect(screen, [255, 255, 255], button1_1)
        pygame.draw.rect(screen, [0, 0, 0], button1) # draw objects down here
        pygame.draw.rect(screen, [255,255,255], button2_1)
        pygame.draw.rect(screen, [0,0,0], button2)
        screen.blit(font.render('PLAY', True, (255, 255, 255)), ((screenWidth/2)-45, (screenHight/4)*2+15))
        screen.blit(font.render('EXIT', True, (255, 255, 255)), ((screenWidth/2)-45, (screenHight/4)*3+15))
        screen.blit(font.render('HIGHSCORE: {0}'.format(highscore), False, (255, 255, 255)), (50, 50))

        pygame.display.update()
        clock.tick(fps)

if __name__ == '__main__':
    main()
