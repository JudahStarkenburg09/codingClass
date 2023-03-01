    #obstacle7
    if obstacle7OnScreen == False:
        obstacle7OnScreen = True
    
    if obstacle7OnScreen == True:
        if obstacle7posy == -200:
            laneChosen7 = random.choice(lanes)
            speedobstacle7 = random.choice(possibleObstacleSpeeds)
        screen.blit(obstacle7, (laneChosen7, obstacle7posy))
        obstacle7R = obstacle7.get_rect(left=(laneChosen7 + 15), top=(obstacle7posy + 17), width=(obstacle7.get_width() - 30), height=(obstacle7.get_height() - 30))
        obstacle7R0 = obstacle7.get_rect(left=laneChosen7, top=obstacle7posy, width=obstacle7.get_width(), height=obstacle7.get_height())
        obstacle7posy += roadSpeed - speedobstacle7

    if obstacle7posy > 750:
        obstacle7OnScreen = False
        obstacle7posy = -200