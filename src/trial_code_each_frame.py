## Hiire joonistus
if mouse_track.getPressed()[0] == 1:
    mouse_track.xdraw.append(mouse_track.getPos()[0])
    mouse_track.ydraw.append(mouse_track.getPos()[1])

if button_yes.contains(mouse) and mouse.getPressed()[0]:
    Yes = 1
    Nupp = 1
 
if button_hint.contains(mouse) and mouse.getPressed()[0]:
    Vihje = 1
    Nupp = 1

    
#check that participant has answered all Qs
if Yes == 1:
    if RSP_ahhaa.getRating() != None and H1_textbox.text != '' and RSP_sudden.getRating() != None and RSP_pleasant.getRating() != None:
        Valmis = 1
elif Vihje == 1:
    #if RSP_ahhaa.getRating() != None and RSP_sudden.getRating() != None and RSP_pleasant.getRating() != None:
    Valmis = 1
#else:
#    Valmis = 0

#if RSP == 2 and RSP_ahhaa.getRating() != None:
        
#oldMouseIsDown = False

## continue
if button_next.contains(mouse_end) and mouse_end.getPressed()[0] == 1:
    mouseIsDown1 = True
    #mouseIsDown = mouse2.getPressed()[0]
        #mouse2.clickReset()
    if mouseIsDown1 and not oldMouseIsDown:
        #win.getMovieFrame()
        oldMouseIsDown = True
        #luup = 1
        #print("luup 1")
    #loop_1.finished = True
else:
    mouseIsDown1 = False
    #continueRoutine = True
    
## clear brush:
if button_clear.contains(mouse) and mouse.getPressed()[0] == 1:
    mouseIsDown = True
    buttons, times = mouse.getPressed(getTime=True)
    location = mouse_track.getPos()
    if mouseIsDown and not oldMouseIsDown:
        
        clear.append(location)
        clear.append(times[0])
        clear.append("clear")
        #win.getMovieFrame()
        #win.flip()
        brush.reset()
    #attempt += 1
        

#######
## restart

    
    
if mouseIsDown2 == True:
    frames += 1
    #print(frames)
    if frames < 10:
        oldMouseIsDown = True
    else:
        mouseIsDown2 = False
        oldMouseIsDown = False
        frames = 0

if mouseIsDown1 == True:
    frames += 1
    #print(frames)
    if frames < 10:
        oldMouseIsDown = True
    else:
        mouseIsDown1 = False
        oldMouseIsDown = False
        frames = 0

if mouseIsDown == True:
    frames += 1
    #print(frames)
    if frames < 10:
        oldMouseIsDown = True
    else:
        mouseIsDown = False
        oldMouseIsDown = False
        frames = 0
        
#else:
#    mouseIsDown = False
#if mouseIsDown2 and not oldMouseIsDown:#save data
#        attempt += 1
#        print(attempt)
#        oldMouseIsDown = True
 
#if RSP_yesno.getRating()=='Ei':
#    Valmis = 1
#elif RSP_yesno.getRating()=='Jah':
#    if RSP_ahhaa.getRating() != None: #and Q2.text != '>':
#        Valmis = 1
#    else:
#        Valmis = 0
#else:
#    Valmis = 0

