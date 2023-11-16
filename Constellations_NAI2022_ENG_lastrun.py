#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on November 16, 2023, at 11:30
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.1.0')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'ConstellationsNAI23'  # from the Builder filename that created this script
expInfo = {'Pseudonym*': '', 'Age': '', 'Gender': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Pseudonym*'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\evaur\\Documents\\faks\\Artificial and natural intellingence\\OnlineEXP_NAI2022-20231102T111413Z-001\\OnlineEXP_NAI2022\\Constellations_NAI2022_ENG_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "intro0"
intro0Clock = core.Clock()
instruction1_2 = visual.ImageStim(
    win=win,
    name='instruction1_2', 
    image='stimuli/intro0.PNG', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse1_2 = event.Mouse(win=win)
x, y = [None, None]
mouse1_2.mouseClock = core.Clock()
button1_2 = visual.Rect(
    win=win, name='button1_2',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.5, -0.65), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_txt1_2 = visual.TextStim(win=win, name='button_txt1_2',
    text='Next',
    font='Open Sans',
    pos=(0.5, -0.65), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "intro1"
intro1Clock = core.Clock()
instruction1 = visual.ImageStim(
    win=win,
    name='instruction1', 
    image='intro1.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse1 = event.Mouse(win=win)
x, y = [None, None]
mouse1.mouseClock = core.Clock()
button1 = visual.Rect(
    win=win, name='button1',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.5, -0.65), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_txt1 = visual.TextStim(win=win, name='button_txt1',
    text='Next',
    font='Open Sans',
    pos=(0.5, -0.65), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "intro2"
intro2Clock = core.Clock()
instruction2 = visual.ImageStim(
    win=win,
    name='instruction2', 
    image='intro2.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse2 = event.Mouse(win=win)
x, y = [None, None]
mouse2.mouseClock = core.Clock()
button2 = visual.Rect(
    win=win, name='button2',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.5, -0.65), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_txt2 = visual.TextStim(win=win, name='button_txt2',
    text='Next',
    font='Open Sans',
    pos=(0.5, -0.65), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "intro3"
intro3Clock = core.Clock()
instruction3 = visual.ImageStim(
    win=win,
    name='instruction3', 
    image='intro3.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse3 = event.Mouse(win=win)
x, y = [None, None]
mouse3.mouseClock = core.Clock()
button3 = visual.Rect(
    win=win, name='button3',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.5, -0.65), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_txt3 = visual.TextStim(win=win, name='button_txt3',
    text='Next',
    font='Open Sans',
    pos=(0.5, -0.65), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "practice_intro"
practice_introClock = core.Clock()
instruction4 = visual.ImageStim(
    win=win,
    name='instruction4', 
    image='intro4.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse4 = event.Mouse(win=win)
x, y = [None, None]
mouse4.mouseClock = core.Clock()
button4 = visual.Rect(
    win=win, name='button4',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.5, -0.65), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_txt4 = visual.TextStim(win=win, name='button_txt4',
    text='Next',
    font='Open Sans',
    pos=(0.5, -0.65), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "practice_trial"
practice_trialClock = core.Clock()
practice_image = visual.ImageStim(
    win=win,
    name='practice_image', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.0), size=(0.65,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practice_brush = visual.Brush(win=win, name='practice_brush',
   lineWidth=3.0,
   lineColor=[1,1,1],
   lineColorSpace='rgb',
   opacity=None,
   buttonRequired=True)
practice_mouse_track = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_track.mouseClock = core.Clock()
practice_instructions_txt = visual.TextStim(win=win, name='practice_instructions_txt',
    text='Draw the first features you think could form the object!',
    font='Open Sans',
    pos=(-0.45, 0.75), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
practice_times_up_txt = visual.TextStim(win=win, name='practice_times_up_txt',
    text="Time's up! If you think you found an object write it here, if not click next to move on.",
    font='Open Sans',
    pos=(-0.45, 0.75), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
practice_button_clear = visual.Rect(
    win=win, name='practice_button_clear',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(-0.2, -0.75), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
practice_clear_txt = visual.TextStim(win=win, name='practice_clear_txt',
    text='Erase',
    font='Open Sans',
    pos=(-0.2, -0.75), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
practice_mouse = event.Mouse(win=win)
x, y = [None, None]
practice_mouse.mouseClock = core.Clock()
practice_button_next = visual.Rect(
    win=win, name='practice_button_next',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.7, -0.75), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
practice_next_txt = visual.TextStim(win=win, name='practice_next_txt',
    text='Next',
    font='Open Sans',
    pos=(0.7, -0.75), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
practice_mouse_end = event.Mouse(win=win)
x, y = [None, None]
practice_mouse_end.mouseClock = core.Clock()
practice_button_done = visual.Rect(
    win=win, name='practice_button_done',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.3,0.6), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='green',
    opacity=None, depth=-12.0, interpolate=True)
practice_done_txt = visual.TextStim(win=win, name='practice_done_txt',
    text='Done!',
    font='Open Sans',
    pos=(0.3,0.6), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
practice_objekt_txt = visual.TextStim(win=win, name='practice_objekt_txt',
    text='What object did you find in the image?',
    font='Open Sans',
    pos=(0.4, 0.55), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
practice_question_textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0.15, 0.5),     letterHeight=0.05,
     size=(0.65,0.4), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None, alignment='center',
     anchor='top-left',
     fillColor='white', borderColor='grey',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='practice_question_textbox',
     autoLog=True,
)

# Initialize components for Routine "practice_rsp"
practice_rspClock = core.Clock()
practice_object = visual.ImageStim(
    win=win,
    name='practice_object', units='height', 
    image='stimuli/practice_first.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, 0.0), size=(0.65,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
practice_outline = visual.ImageStim(
    win=win,
    name='practice_outline', units='height', 
    image='stimuli/solution1.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0.0, 0.0), size=(0.65,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Answer: CAR',
    font='Open Sans',
    pos=(0, 0.7), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
mouse5 = event.Mouse(win=win)
x, y = [None, None]
mouse5.mouseClock = core.Clock()
button5 = visual.Rect(
    win=win, name='button5',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.5, -0.6), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
button_txt5 = visual.TextStim(win=win, name='button_txt5',
    text='Next',
    font='Open Sans',
    pos=(0.5, -0.6), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "exp_intro"
exp_introClock = core.Clock()
instruction4_2 = visual.ImageStim(
    win=win,
    name='instruction4_2', 
    image='intro5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.3, 1.6),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mouse4_2 = event.Mouse(win=win)
x, y = [None, None]
mouse4_2.mouseClock = core.Clock()
button4_2 = visual.Rect(
    win=win, name='button4_2',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.5, -0.65), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
button_txt4_2 = visual.TextStim(win=win, name='button_txt4_2',
    text='Next',
    font='Open Sans',
    pos=(0.5, -0.65), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0.0), size=(0.65,0.65),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
#stim = 0
Version = 0
vrs = str(randint(1,3)) #expInfo['Version (1 or 2)']

print(vrs)
mouse_track = event.Mouse(win=win)
x, y = [None, None]
mouse_track.mouseClock = core.Clock()
brush = visual.Brush(win=win, name='brush',
   lineWidth=3.0,
   lineColor=[1,1,1],
   lineColorSpace='rgb',
   opacity=None,
   buttonRequired=True)
instructions_txt = visual.TextStim(win=win, name='instructions_txt',
    text='Draw the first features you think could form the object!',
    font='Open Sans',
    pos=(-0.45, 0.75), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
times_up_txt = visual.TextStim(win=win, name='times_up_txt',
    text="Time's up! If you think you found an object write it here, if not click next to move on.",
    font='Open Sans',
    pos=(-0.45, 0.75), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
button_clear = visual.Rect(
    win=win, name='button_clear',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(-0.2, -0.75), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
clear_txt = visual.TextStim(win=win, name='clear_txt',
    text='Erase',
    font='Open Sans',
    pos=(-0.2, -0.75), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
button_next = visual.Rect(
    win=win, name='button_next',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.7, -0.75), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
next_txt = visual.TextStim(win=win, name='next_txt',
    text='Next',
    font='Open Sans',
    pos=(0.7, -0.75), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
mouse_end = event.Mouse(win=win)
x, y = [None, None]
mouse_end.mouseClock = core.Clock()
button_done = visual.Rect(
    win=win, name='button_done',
    width=(0.2, 0.1)[0], height=(0.2, 0.1)[1],
    ori=0.0, pos=(0.3,0.6), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='green',
    opacity=None, depth=-13.0, interpolate=True)
done_txt = visual.TextStim(win=win, name='done_txt',
    text='Done!',
    font='Open Sans',
    pos=(0.3,0.6), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
object_txt = visual.TextStim(win=win, name='object_txt',
    text='What object did you find in the image?',
    font='Open Sans',
    pos=(0.4, 0.55), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
question_textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0.15, 0.5),     letterHeight=0.05,
     size=(0.65,0.4), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None, alignment='center',
     anchor='top-left',
     fillColor='white', borderColor='grey',
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='question_textbox',
     autoLog=True,
)

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);



# Initialize components for Routine "end"
endClock = core.Clock()
end_txt = visual.TextStim(win=win, name='end_txt',
    text='The end. Thank you!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro0"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse1_2
mouse1_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
intro0Components = [instruction1_2, mouse1_2, button1_2, button_txt1_2]
for thisComponent in intro0Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro0Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro0"-------
while continueRoutine:
    # get current time
    t = intro0Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro0Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction1_2* updates
    if instruction1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction1_2.frameNStart = frameN  # exact frame index
        instruction1_2.tStart = t  # local t and not account for scr refresh
        instruction1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction1_2, 'tStartRefresh')  # time at next scr refresh
        instruction1_2.setAutoDraw(True)
    # *mouse1_2* updates
    if mouse1_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse1_2.frameNStart = frameN  # exact frame index
        mouse1_2.tStart = t  # local t and not account for scr refresh
        mouse1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse1_2, 'tStartRefresh')  # time at next scr refresh
        mouse1_2.status = STARTED
        mouse1_2.mouseClock.reset()
        prevButtonState = mouse1_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse1_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse1_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([button1_2,])
                    clickableList = [button1_2,]
                except:
                    clickableList = [[button1_2,]]
                for obj in clickableList:
                    if obj.contains(mouse1_2):
                        gotValidClick = True
                        mouse1_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button1_2* updates
    if button1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button1_2.frameNStart = frameN  # exact frame index
        button1_2.tStart = t  # local t and not account for scr refresh
        button1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button1_2, 'tStartRefresh')  # time at next scr refresh
        button1_2.setAutoDraw(True)
    
    # *button_txt1_2* updates
    if button_txt1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_txt1_2.frameNStart = frameN  # exact frame index
        button_txt1_2.tStart = t  # local t and not account for scr refresh
        button_txt1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_txt1_2, 'tStartRefresh')  # time at next scr refresh
        button_txt1_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro0"-------
for thisComponent in intro0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "intro0" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro1"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse1
mouse1.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
intro1Components = [instruction1, mouse1, button1, button_txt1]
for thisComponent in intro1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro1"-------
while continueRoutine:
    # get current time
    t = intro1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction1* updates
    if instruction1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction1.frameNStart = frameN  # exact frame index
        instruction1.tStart = t  # local t and not account for scr refresh
        instruction1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction1, 'tStartRefresh')  # time at next scr refresh
        instruction1.setAutoDraw(True)
    # *mouse1* updates
    if mouse1.status == NOT_STARTED and t >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        mouse1.frameNStart = frameN  # exact frame index
        mouse1.tStart = t  # local t and not account for scr refresh
        mouse1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse1, 'tStartRefresh')  # time at next scr refresh
        mouse1.status = STARTED
        mouse1.mouseClock.reset()
        prevButtonState = mouse1.getPressed()  # if button is down already this ISN'T a new click
    if mouse1.status == STARTED:  # only update if started and not finished!
        buttons = mouse1.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([button1,])
                    clickableList = [button1,]
                except:
                    clickableList = [[button1,]]
                for obj in clickableList:
                    if obj.contains(mouse1):
                        gotValidClick = True
                        mouse1.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button1* updates
    if button1.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button1.frameNStart = frameN  # exact frame index
        button1.tStart = t  # local t and not account for scr refresh
        button1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button1, 'tStartRefresh')  # time at next scr refresh
        button1.setAutoDraw(True)
    
    # *button_txt1* updates
    if button_txt1.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button_txt1.frameNStart = frameN  # exact frame index
        button_txt1.tStart = t  # local t and not account for scr refresh
        button_txt1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_txt1, 'tStartRefresh')  # time at next scr refresh
        button_txt1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro1"-------
for thisComponent in intro1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "intro1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro2"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse2
mouse2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
intro2Components = [instruction2, mouse2, button2, button_txt2]
for thisComponent in intro2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro2"-------
while continueRoutine:
    # get current time
    t = intro2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction2* updates
    if instruction2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction2.frameNStart = frameN  # exact frame index
        instruction2.tStart = t  # local t and not account for scr refresh
        instruction2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction2, 'tStartRefresh')  # time at next scr refresh
        instruction2.setAutoDraw(True)
    # *mouse2* updates
    if mouse2.status == NOT_STARTED and t >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        mouse2.frameNStart = frameN  # exact frame index
        mouse2.tStart = t  # local t and not account for scr refresh
        mouse2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse2, 'tStartRefresh')  # time at next scr refresh
        mouse2.status = STARTED
        mouse2.mouseClock.reset()
        prevButtonState = mouse2.getPressed()  # if button is down already this ISN'T a new click
    if mouse2.status == STARTED:  # only update if started and not finished!
        buttons = mouse2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([button2,])
                    clickableList = [button2,]
                except:
                    clickableList = [[button2,]]
                for obj in clickableList:
                    if obj.contains(mouse2):
                        gotValidClick = True
                        mouse2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button2* updates
    if button2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button2.frameNStart = frameN  # exact frame index
        button2.tStart = t  # local t and not account for scr refresh
        button2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button2, 'tStartRefresh')  # time at next scr refresh
        button2.setAutoDraw(True)
    
    # *button_txt2* updates
    if button_txt2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button_txt2.frameNStart = frameN  # exact frame index
        button_txt2.tStart = t  # local t and not account for scr refresh
        button_txt2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_txt2, 'tStartRefresh')  # time at next scr refresh
        button_txt2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro2"-------
for thisComponent in intro2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "intro2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro3"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse3
mouse3.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
intro3Components = [instruction3, mouse3, button3, button_txt3]
for thisComponent in intro3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
intro3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro3"-------
while continueRoutine:
    # get current time
    t = intro3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=intro3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction3* updates
    if instruction3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction3.frameNStart = frameN  # exact frame index
        instruction3.tStart = t  # local t and not account for scr refresh
        instruction3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction3, 'tStartRefresh')  # time at next scr refresh
        instruction3.setAutoDraw(True)
    # *mouse3* updates
    if mouse3.status == NOT_STARTED and t >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        mouse3.frameNStart = frameN  # exact frame index
        mouse3.tStart = t  # local t and not account for scr refresh
        mouse3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse3, 'tStartRefresh')  # time at next scr refresh
        mouse3.status = STARTED
        mouse3.mouseClock.reset()
        prevButtonState = mouse3.getPressed()  # if button is down already this ISN'T a new click
    if mouse3.status == STARTED:  # only update if started and not finished!
        buttons = mouse3.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([button3,])
                    clickableList = [button3,]
                except:
                    clickableList = [[button3,]]
                for obj in clickableList:
                    if obj.contains(mouse3):
                        gotValidClick = True
                        mouse3.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button3* updates
    if button3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button3.frameNStart = frameN  # exact frame index
        button3.tStart = t  # local t and not account for scr refresh
        button3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button3, 'tStartRefresh')  # time at next scr refresh
        button3.setAutoDraw(True)
    
    # *button_txt3* updates
    if button_txt3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button_txt3.frameNStart = frameN  # exact frame index
        button_txt3.tStart = t  # local t and not account for scr refresh
        button_txt3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_txt3, 'tStartRefresh')  # time at next scr refresh
        button_txt3.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in intro3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro3"-------
for thisComponent in intro3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "intro3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_intro"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse4
mouse4.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
practice_introComponents = [instruction4, mouse4, button4, button_txt4]
for thisComponent in practice_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_intro"-------
while continueRoutine:
    # get current time
    t = practice_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction4* updates
    if instruction4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction4.frameNStart = frameN  # exact frame index
        instruction4.tStart = t  # local t and not account for scr refresh
        instruction4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction4, 'tStartRefresh')  # time at next scr refresh
        instruction4.setAutoDraw(True)
    # *mouse4* updates
    if mouse4.status == NOT_STARTED and t >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        mouse4.frameNStart = frameN  # exact frame index
        mouse4.tStart = t  # local t and not account for scr refresh
        mouse4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse4, 'tStartRefresh')  # time at next scr refresh
        mouse4.status = STARTED
        mouse4.mouseClock.reset()
        prevButtonState = mouse4.getPressed()  # if button is down already this ISN'T a new click
    if mouse4.status == STARTED:  # only update if started and not finished!
        buttons = mouse4.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([button4,])
                    clickableList = [button4,]
                except:
                    clickableList = [[button4,]]
                for obj in clickableList:
                    if obj.contains(mouse4):
                        gotValidClick = True
                        mouse4.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button4* updates
    if button4.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button4.frameNStart = frameN  # exact frame index
        button4.tStart = t  # local t and not account for scr refresh
        button4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button4, 'tStartRefresh')  # time at next scr refresh
        button4.setAutoDraw(True)
    
    # *button_txt4* updates
    if button_txt4.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button_txt4.frameNStart = frameN  # exact frame index
        button_txt4.tStart = t  # local t and not account for scr refresh
        button_txt4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_txt4, 'tStartRefresh')  # time at next scr refresh
        button_txt4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_intro"-------
for thisComponent in practice_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "practice_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_trial"-------
continueRoutine = True
# update component parameters for each repeat
practice_image.setImage('stimuli/practice_first.jpg')
practice_brush.reset()
# setup some python lists for storing info about the practice_mouse_track
practice_mouse_track.x = []
practice_mouse_track.y = []
practice_mouse_track.leftButton = []
practice_mouse_track.midButton = []
practice_mouse_track.rightButton = []
practice_mouse_track.time = []
gotValidClick = False  # until a click is received
practice_show_next_btn = False
practice_show_done_btn = True

# setup some python lists for storing info about the practice_mouse
practice_mouse.clicked_name = []
gotValidClick = False  # until a click is received
# setup some python lists for storing info about the practice_mouse_end
practice_mouse_end.clicked_name = []
gotValidClick = False  # until a click is received
practice_question_textbox.reset()
practice_question_textbox.setText('')
# keep track of which components have finished
practice_trialComponents = [practice_image, practice_brush, practice_mouse_track, practice_instructions_txt, practice_times_up_txt, practice_button_clear, practice_clear_txt, practice_mouse, practice_button_next, practice_next_txt, practice_mouse_end, practice_button_done, practice_done_txt, practice_objekt_txt, practice_question_textbox]
for thisComponent in practice_trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_trial"-------
while continueRoutine:
    # get current time
    t = practice_trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_image* updates
    if practice_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_image.frameNStart = frameN  # exact frame index
        practice_image.tStart = t  # local t and not account for scr refresh
        practice_image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_image, 'tStartRefresh')  # time at next scr refresh
        practice_image.setAutoDraw(True)
    
    # *practice_brush* updates
    if practice_brush.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_brush.frameNStart = frameN  # exact frame index
        practice_brush.tStart = t  # local t and not account for scr refresh
        practice_brush.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_brush, 'tStartRefresh')  # time at next scr refresh
        practice_brush.setAutoDraw(True)
    if practice_brush.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice_brush.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            practice_brush.tStop = t  # not accounting for scr refresh
            practice_brush.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_brush, 'tStopRefresh')  # time at next scr refresh
            practice_brush.setAutoDraw(False)
    # *practice_mouse_track* updates
    if practice_mouse_track.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_mouse_track.frameNStart = frameN  # exact frame index
        practice_mouse_track.tStart = t  # local t and not account for scr refresh
        practice_mouse_track.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_mouse_track, 'tStartRefresh')  # time at next scr refresh
        practice_mouse_track.status = STARTED
        practice_mouse_track.mouseClock.reset()
        prevButtonState = practice_mouse_track.getPressed()  # if button is down already this ISN'T a new click
    if practice_mouse_track.status == STARTED:  # only update if started and not finished!
        x, y = practice_mouse_track.getPos()
        practice_mouse_track.x.append(x)
        practice_mouse_track.y.append(y)
        buttons = practice_mouse_track.getPressed()
        practice_mouse_track.leftButton.append(buttons[0])
        practice_mouse_track.midButton.append(buttons[1])
        practice_mouse_track.rightButton.append(buttons[2])
        practice_mouse_track.time.append(practice_mouse_track.mouseClock.getTime())
    # Done button click
    if practice_show_done_btn and practice_button_done.contains(practice_mouse) and practice_mouse.getPressed()[0]:
        practice_show_next_btn = True
        practice_show_done_btn = False
        
    # Clear button click
    if practice_show_done_btn and practice_button_clear.contains(practice_mouse) and practice_mouse.getPressed()[0] == 1:
        brush.reset()
        practice_brush.reset()
    
    
    # *practice_instructions_txt* updates
    if practice_instructions_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_instructions_txt.frameNStart = frameN  # exact frame index
        practice_instructions_txt.tStart = t  # local t and not account for scr refresh
        practice_instructions_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_instructions_txt, 'tStartRefresh')  # time at next scr refresh
        practice_instructions_txt.setAutoDraw(True)
    if practice_instructions_txt.status == STARTED:
        if bool(practice_show_next_btn):
            # keep track of stop time/frame for later
            practice_instructions_txt.tStop = t  # not accounting for scr refresh
            practice_instructions_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_instructions_txt, 'tStopRefresh')  # time at next scr refresh
            practice_instructions_txt.setAutoDraw(False)
    
    # *practice_times_up_txt* updates
    if practice_times_up_txt.status == NOT_STARTED and practice_show_next_btn:
        # keep track of start time/frame for later
        practice_times_up_txt.frameNStart = frameN  # exact frame index
        practice_times_up_txt.tStart = t  # local t and not account for scr refresh
        practice_times_up_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_times_up_txt, 'tStartRefresh')  # time at next scr refresh
        practice_times_up_txt.setAutoDraw(True)
    
    # *practice_button_clear* updates
    if practice_button_clear.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_button_clear.frameNStart = frameN  # exact frame index
        practice_button_clear.tStart = t  # local t and not account for scr refresh
        practice_button_clear.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_button_clear, 'tStartRefresh')  # time at next scr refresh
        practice_button_clear.setAutoDraw(True)
    
    # *practice_clear_txt* updates
    if practice_clear_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_clear_txt.frameNStart = frameN  # exact frame index
        practice_clear_txt.tStart = t  # local t and not account for scr refresh
        practice_clear_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_clear_txt, 'tStartRefresh')  # time at next scr refresh
        practice_clear_txt.setAutoDraw(True)
    # *practice_mouse* updates
    if practice_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_mouse.frameNStart = frameN  # exact frame index
        practice_mouse.tStart = t  # local t and not account for scr refresh
        practice_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_mouse, 'tStartRefresh')  # time at next scr refresh
        practice_mouse.status = STARTED
        practice_mouse.mouseClock.reset()
        prevButtonState = practice_mouse.getPressed()  # if button is down already this ISN'T a new click
    
    # *practice_button_next* updates
    if practice_button_next.status == NOT_STARTED and practice_show_next_btn:
        # keep track of start time/frame for later
        practice_button_next.frameNStart = frameN  # exact frame index
        practice_button_next.tStart = t  # local t and not account for scr refresh
        practice_button_next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_button_next, 'tStartRefresh')  # time at next scr refresh
        practice_button_next.setAutoDraw(True)
    
    # *practice_next_txt* updates
    if practice_next_txt.status == NOT_STARTED and practice_show_next_btn:
        # keep track of start time/frame for later
        practice_next_txt.frameNStart = frameN  # exact frame index
        practice_next_txt.tStart = t  # local t and not account for scr refresh
        practice_next_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_next_txt, 'tStartRefresh')  # time at next scr refresh
        practice_next_txt.setAutoDraw(True)
    # *practice_mouse_end* updates
    if practice_mouse_end.status == NOT_STARTED and practice_show_next_btn:
        # keep track of start time/frame for later
        practice_mouse_end.frameNStart = frameN  # exact frame index
        practice_mouse_end.tStart = t  # local t and not account for scr refresh
        practice_mouse_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_mouse_end, 'tStartRefresh')  # time at next scr refresh
        practice_mouse_end.status = STARTED
        practice_mouse_end.mouseClock.reset()
        prevButtonState = practice_mouse_end.getPressed()  # if button is down already this ISN'T a new click
    if practice_mouse_end.status == STARTED:  # only update if started and not finished!
        buttons = practice_mouse_end.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter(practice_button_next)
                    clickableList = practice_button_next
                except:
                    clickableList = [practice_button_next]
                for obj in clickableList:
                    if obj.contains(practice_mouse_end):
                        gotValidClick = True
                        practice_mouse_end.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *practice_button_done* updates
    if practice_button_done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_button_done.frameNStart = frameN  # exact frame index
        practice_button_done.tStart = t  # local t and not account for scr refresh
        practice_button_done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_button_done, 'tStartRefresh')  # time at next scr refresh
        practice_button_done.setAutoDraw(True)
    if practice_button_done.status == STARTED:
        if bool(practice_show_next_btn):
            # keep track of stop time/frame for later
            practice_button_done.tStop = t  # not accounting for scr refresh
            practice_button_done.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_button_done, 'tStopRefresh')  # time at next scr refresh
            practice_button_done.setAutoDraw(False)
    
    # *practice_done_txt* updates
    if practice_done_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_done_txt.frameNStart = frameN  # exact frame index
        practice_done_txt.tStart = t  # local t and not account for scr refresh
        practice_done_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_done_txt, 'tStartRefresh')  # time at next scr refresh
        practice_done_txt.setAutoDraw(True)
    if practice_done_txt.status == STARTED:
        if bool(practice_show_next_btn):
            # keep track of stop time/frame for later
            practice_done_txt.tStop = t  # not accounting for scr refresh
            practice_done_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_done_txt, 'tStopRefresh')  # time at next scr refresh
            practice_done_txt.setAutoDraw(False)
    
    # *practice_objekt_txt* updates
    if practice_objekt_txt.status == NOT_STARTED and practice_show_next_btn:
        # keep track of start time/frame for later
        practice_objekt_txt.frameNStart = frameN  # exact frame index
        practice_objekt_txt.tStart = t  # local t and not account for scr refresh
        practice_objekt_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_objekt_txt, 'tStartRefresh')  # time at next scr refresh
        practice_objekt_txt.setAutoDraw(True)
    
    # *practice_question_textbox* updates
    if practice_question_textbox.status == NOT_STARTED and practice_show_next_btn:
        # keep track of start time/frame for later
        practice_question_textbox.frameNStart = frameN  # exact frame index
        practice_question_textbox.tStart = t  # local t and not account for scr refresh
        practice_question_textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_question_textbox, 'tStartRefresh')  # time at next scr refresh
        practice_question_textbox.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_trial"-------
for thisComponent in practice_trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('practice_mouse_track.x', practice_mouse_track.x)
thisExp.addData('practice_mouse_track.y', practice_mouse_track.y)
thisExp.addData('practice_mouse_track.leftButton', practice_mouse_track.leftButton)
thisExp.addData('practice_mouse_track.midButton', practice_mouse_track.midButton)
thisExp.addData('practice_mouse_track.rightButton', practice_mouse_track.rightButton)
thisExp.addData('practice_mouse_track.time', practice_mouse_track.time)
thisExp.nextEntry()
#H1_textbox_2.refresh()
practice_brush.reset()


thisExp.addData('practice_times_up_txt.started', practice_times_up_txt.tStartRefresh)
thisExp.addData('practice_times_up_txt.stopped', practice_times_up_txt.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
thisExp.addData('practice_button_done.started', practice_button_done.tStartRefresh)
thisExp.addData('practice_button_done.stopped', practice_button_done.tStopRefresh)
thisExp.addData('practice_question_textbox.text',practice_question_textbox.text)
# the Routine "practice_trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_rsp"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse5
mouse5.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
practice_rspComponents = [practice_object, practice_outline, text_2, mouse5, button5, button_txt5]
for thisComponent in practice_rspComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_rspClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_rsp"-------
while continueRoutine:
    # get current time
    t = practice_rspClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_rspClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *practice_object* updates
    if practice_object.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        practice_object.frameNStart = frameN  # exact frame index
        practice_object.tStart = t  # local t and not account for scr refresh
        practice_object.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_object, 'tStartRefresh')  # time at next scr refresh
        practice_object.setAutoDraw(True)
    if practice_object.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > practice_object.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            practice_object.tStop = t  # not accounting for scr refresh
            practice_object.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practice_object, 'tStopRefresh')  # time at next scr refresh
            practice_object.setAutoDraw(False)
    
    # *practice_outline* updates
    if practice_outline.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        practice_outline.frameNStart = frameN  # exact frame index
        practice_outline.tStart = t  # local t and not account for scr refresh
        practice_outline.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(practice_outline, 'tStartRefresh')  # time at next scr refresh
        practice_outline.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    # *mouse5* updates
    if mouse5.status == NOT_STARTED and t >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        mouse5.frameNStart = frameN  # exact frame index
        mouse5.tStart = t  # local t and not account for scr refresh
        mouse5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse5, 'tStartRefresh')  # time at next scr refresh
        mouse5.status = STARTED
        mouse5.mouseClock.reset()
        prevButtonState = mouse5.getPressed()  # if button is down already this ISN'T a new click
    if mouse5.status == STARTED:  # only update if started and not finished!
        buttons = mouse5.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([button5,])
                    clickableList = [button5,]
                except:
                    clickableList = [[button5,]]
                for obj in clickableList:
                    if obj.contains(mouse5):
                        gotValidClick = True
                        mouse5.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button5* updates
    if button5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button5.frameNStart = frameN  # exact frame index
        button5.tStart = t  # local t and not account for scr refresh
        button5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button5, 'tStartRefresh')  # time at next scr refresh
        button5.setAutoDraw(True)
    
    # *button_txt5* updates
    if button_txt5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button_txt5.frameNStart = frameN  # exact frame index
        button_txt5.tStart = t  # local t and not account for scr refresh
        button_txt5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_txt5, 'tStartRefresh')  # time at next scr refresh
        button_txt5.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_rspComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_rsp"-------
for thisComponent in practice_rspComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('practice_object.started', practice_object.tStartRefresh)
thisExp.addData('practice_object.stopped', practice_object.tStopRefresh)
thisExp.addData('practice_outline.started', practice_outline.tStartRefresh)
thisExp.addData('practice_outline.stopped', practice_outline.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "practice_rsp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "exp_intro"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse4_2
mouse4_2.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
exp_introComponents = [instruction4_2, mouse4_2, button4_2, button_txt4_2]
for thisComponent in exp_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
exp_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "exp_intro"-------
while continueRoutine:
    # get current time
    t = exp_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=exp_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction4_2* updates
    if instruction4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction4_2.frameNStart = frameN  # exact frame index
        instruction4_2.tStart = t  # local t and not account for scr refresh
        instruction4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction4_2, 'tStartRefresh')  # time at next scr refresh
        instruction4_2.setAutoDraw(True)
    # *mouse4_2* updates
    if mouse4_2.status == NOT_STARTED and t >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        mouse4_2.frameNStart = frameN  # exact frame index
        mouse4_2.tStart = t  # local t and not account for scr refresh
        mouse4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse4_2, 'tStartRefresh')  # time at next scr refresh
        mouse4_2.status = STARTED
        mouse4_2.mouseClock.reset()
        prevButtonState = mouse4_2.getPressed()  # if button is down already this ISN'T a new click
    if mouse4_2.status == STARTED:  # only update if started and not finished!
        buttons = mouse4_2.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter([button4_2,])
                    clickableList = [button4_2,]
                except:
                    clickableList = [[button4_2,]]
                for obj in clickableList:
                    if obj.contains(mouse4_2):
                        gotValidClick = True
                        mouse4_2.clicked_name.append(obj.name)
                if gotValidClick:  
                    continueRoutine = False  # abort routine on response
    
    # *button4_2* updates
    if button4_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button4_2.frameNStart = frameN  # exact frame index
        button4_2.tStart = t  # local t and not account for scr refresh
        button4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button4_2, 'tStartRefresh')  # time at next scr refresh
        button4_2.setAutoDraw(True)
    
    # *button_txt4_2* updates
    if button_txt4_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        button_txt4_2.frameNStart = frameN  # exact frame index
        button_txt4_2.tStart = t  # local t and not account for scr refresh
        button_txt4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_txt4_2, 'tStartRefresh')  # time at next scr refresh
        button_txt4_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exp_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exp_intro"-------
for thisComponent in exp_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "exp_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trial_online.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(stim)
    #if vrs == '1':
    #    stim = stim1
    #elif vrs == '2':
    #    stim = stim2
        
    #print(stim)
    
    # setup some python lists for storing info about the mouse_track
    mouse_track.x = []
    mouse_track.y = []
    mouse_track.leftButton = []
    mouse_track.midButton = []
    mouse_track.rightButton = []
    mouse_track.time = []
    gotValidClick = False  # until a click is received
    brush.reset()
    is_first_frame = True
    trial_start_time = 0.0
    trial_time_limit = 5.0
    
    show_next_btn = False
    show_done_btn = True
    
    mouse_track.xdraw = []
    mouse_track.ydraw = []
    clear = []
    
    
    # setup some python lists for storing info about the mouse
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # setup some python lists for storing info about the mouse_end
    mouse_end.clicked_name = []
    gotValidClick = False  # until a click is received
    question_textbox.reset()
    question_textbox.setText('')
    # keep track of which components have finished
    trialComponents = [image, mouse_track, brush, instructions_txt, times_up_txt, button_clear, clear_txt, mouse, button_next, next_txt, mouse_end, button_done, done_txt, object_txt, question_textbox]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        # *mouse_track* updates
        if mouse_track.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_track.frameNStart = frameN  # exact frame index
            mouse_track.tStart = t  # local t and not account for scr refresh
            mouse_track.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_track, 'tStartRefresh')  # time at next scr refresh
            mouse_track.status = STARTED
            mouse_track.mouseClock.reset()
            prevButtonState = mouse_track.getPressed()  # if button is down already this ISN'T a new click
        if mouse_track.status == STARTED:  # only update if started and not finished!
            x, y = mouse_track.getPos()
            mouse_track.x.append(x)
            mouse_track.y.append(y)
            buttons = mouse_track.getPressed()
            mouse_track.leftButton.append(buttons[0])
            mouse_track.midButton.append(buttons[1])
            mouse_track.rightButton.append(buttons[2])
            mouse_track.time.append(mouse_track.mouseClock.getTime())
        
        # *brush* updates
        if brush.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            brush.frameNStart = frameN  # exact frame index
            brush.tStart = t  # local t and not account for scr refresh
            brush.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(brush, 'tStartRefresh')  # time at next scr refresh
            brush.setAutoDraw(True)
        if brush.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > brush.tStartRefresh + 30.0-frameTolerance:
                # keep track of stop time/frame for later
                brush.tStop = t  # not accounting for scr refresh
                brush.frameNStop = frameN  # exact frame index
                win.timeOnFlip(brush, 'tStopRefresh')  # time at next scr refresh
                brush.setAutoDraw(False)
        # Mouse position recordnig
        if mouse_track.getPressed()[0] == 1:
            mouse_track.xdraw.append(mouse_track.getPos()[0])
            mouse_track.ydraw.append(mouse_track.getPos()[1])
        
        # Check if trial time limit reached
        if is_first_frame:
            trial_start_time = tThisFlipGlobal
            is_first_frame = False
                    
        if tThisFlipGlobal > trial_start_time + trial_time_limit - frameTolerance:
            show_next_btn = True
            show_done_btn = False
        
        # Done button click
        if show_done_btn and button_done.contains(mouse) and mouse.getPressed()[0]:
            show_next_btn = True
            show_done_btn = False
            
        # Clear button click
        if show_done_btn and button_clear.contains(mouse) and mouse.getPressed()[0] == 1:
            buttons, times = mouse.getPressed(getTime=True)
            location = mouse_track.getPos()
            clear.append(location)
            clear.append(times[0])
            clear.append("clear")
            brush.reset()
        
        # *instructions_txt* updates
        if instructions_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_txt.frameNStart = frameN  # exact frame index
            instructions_txt.tStart = t  # local t and not account for scr refresh
            instructions_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_txt, 'tStartRefresh')  # time at next scr refresh
            instructions_txt.setAutoDraw(True)
        if instructions_txt.status == STARTED:
            if bool(show_next_btn):
                # keep track of stop time/frame for later
                instructions_txt.tStop = t  # not accounting for scr refresh
                instructions_txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instructions_txt, 'tStopRefresh')  # time at next scr refresh
                instructions_txt.setAutoDraw(False)
        
        # *times_up_txt* updates
        if times_up_txt.status == NOT_STARTED and show_next_btn:
            # keep track of start time/frame for later
            times_up_txt.frameNStart = frameN  # exact frame index
            times_up_txt.tStart = t  # local t and not account for scr refresh
            times_up_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(times_up_txt, 'tStartRefresh')  # time at next scr refresh
            times_up_txt.setAutoDraw(True)
        
        # *button_clear* updates
        if button_clear.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_clear.frameNStart = frameN  # exact frame index
            button_clear.tStart = t  # local t and not account for scr refresh
            button_clear.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_clear, 'tStartRefresh')  # time at next scr refresh
            button_clear.setAutoDraw(True)
        
        # *clear_txt* updates
        if clear_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clear_txt.frameNStart = frameN  # exact frame index
            clear_txt.tStart = t  # local t and not account for scr refresh
            clear_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clear_txt, 'tStartRefresh')  # time at next scr refresh
            clear_txt.setAutoDraw(True)
        # *mouse* updates
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        
        # *button_next* updates
        if button_next.status == NOT_STARTED and show_next_btn:
            # keep track of start time/frame for later
            button_next.frameNStart = frameN  # exact frame index
            button_next.tStart = t  # local t and not account for scr refresh
            button_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_next, 'tStartRefresh')  # time at next scr refresh
            button_next.setAutoDraw(True)
        
        # *next_txt* updates
        if next_txt.status == NOT_STARTED and show_next_btn:
            # keep track of start time/frame for later
            next_txt.frameNStart = frameN  # exact frame index
            next_txt.tStart = t  # local t and not account for scr refresh
            next_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_txt, 'tStartRefresh')  # time at next scr refresh
            next_txt.setAutoDraw(True)
        # *mouse_end* updates
        if mouse_end.status == NOT_STARTED and show_done_btn:
            # keep track of start time/frame for later
            mouse_end.frameNStart = frameN  # exact frame index
            mouse_end.tStart = t  # local t and not account for scr refresh
            mouse_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_end, 'tStartRefresh')  # time at next scr refresh
            mouse_end.status = STARTED
            mouse_end.mouseClock.reset()
            prevButtonState = mouse_end.getPressed()  # if button is down already this ISN'T a new click
        if mouse_end.status == STARTED:  # only update if started and not finished!
            buttons = mouse_end.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(button_next)
                        clickableList = button_next
                    except:
                        clickableList = [button_next]
                    for obj in clickableList:
                        if obj.contains(mouse_end):
                            gotValidClick = True
                            mouse_end.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # *button_done* updates
        if button_done.status == NOT_STARTED and show_done_btn:
            # keep track of start time/frame for later
            button_done.frameNStart = frameN  # exact frame index
            button_done.tStart = t  # local t and not account for scr refresh
            button_done.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_done, 'tStartRefresh')  # time at next scr refresh
            button_done.setAutoDraw(True)
        if button_done.status == STARTED:
            if bool(show_next_btn):
                # keep track of stop time/frame for later
                button_done.tStop = t  # not accounting for scr refresh
                button_done.frameNStop = frameN  # exact frame index
                win.timeOnFlip(button_done, 'tStopRefresh')  # time at next scr refresh
                button_done.setAutoDraw(False)
        
        # *done_txt* updates
        if done_txt.status == NOT_STARTED and show_done_btn:
            # keep track of start time/frame for later
            done_txt.frameNStart = frameN  # exact frame index
            done_txt.tStart = t  # local t and not account for scr refresh
            done_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(done_txt, 'tStartRefresh')  # time at next scr refresh
            done_txt.setAutoDraw(True)
        if done_txt.status == STARTED:
            if bool(show_next_btn):
                # keep track of stop time/frame for later
                done_txt.tStop = t  # not accounting for scr refresh
                done_txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(done_txt, 'tStopRefresh')  # time at next scr refresh
                done_txt.setAutoDraw(False)
        
        # *object_txt* updates
        if object_txt.status == NOT_STARTED and show_next_btn:
            # keep track of start time/frame for later
            object_txt.frameNStart = frameN  # exact frame index
            object_txt.tStart = t  # local t and not account for scr refresh
            object_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(object_txt, 'tStartRefresh')  # time at next scr refresh
            object_txt.setAutoDraw(True)
        
        # *question_textbox* updates
        if question_textbox.status == NOT_STARTED and show_next_btn:
            # keep track of start time/frame for later
            question_textbox.frameNStart = frameN  # exact frame index
            question_textbox.tStart = t  # local t and not account for scr refresh
            question_textbox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_textbox, 'tStartRefresh')  # time at next scr refresh
            question_textbox.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('image.started', image.tStartRefresh)
    trials.addData('image.stopped', image.tStopRefresh)
    thisExp.addData('Version ' + str(vrs), Version)
    # store data for trials (TrialHandler)
    trials.addData('mouse_track.x', mouse_track.x)
    trials.addData('mouse_track.y', mouse_track.y)
    trials.addData('mouse_track.leftButton', mouse_track.leftButton)
    trials.addData('mouse_track.midButton', mouse_track.midButton)
    trials.addData('mouse_track.rightButton', mouse_track.rightButton)
    trials.addData('mouse_track.time', mouse_track.time)
    ## Salvesta joonistus
    thisExp.addData('mouse1.x_draw', mouse_track.xdraw)
    thisExp.addData('mouse1.y_draw', mouse_track.ydraw)
    thisExp.addData('Clear pressed', clear)
    
    print(clear)
    #luup = 1
    #print("luup 1")
    
    KI = expInfo['Pseudonym*']
    
    #file="KI"+KI+"_"+str(stim[8:11])+"-"+".png"
    #rep = loop_1.thisRepN + 1
    
    kk = trials.thisN + 1
    #file="ID"+KI+"_"+str(kk)+"_"+str(ID1)+"-"+str(rep)+".png"
    
    #print(file)
    #win.saveMovieFrames(file,clearFrames=True)
    
    #SEE LAHTI KOMMENTEERIDA VB
    #H1_textbox.refresh()
    brush.reset()
    
    
    trials.addData('times_up_txt.started', times_up_txt.tStartRefresh)
    trials.addData('times_up_txt.stopped', times_up_txt.tStopRefresh)
    # store data for trials (TrialHandler)
    # store data for trials (TrialHandler)
    trials.addData('button_done.started', button_done.tStartRefresh)
    trials.addData('button_done.stopped', button_done.tStopRefresh)
    trials.addData('question_textbox.text',question_textbox.text)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "pause"-------
continueRoutine = True
routineTimer.add(0.300000)
# update component parameters for each repeat
brush.reset()


# keep track of which components have finished
pauseComponents = [text]
for thisComponent in pauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pause"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = pauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pause"-------
for thisComponent in pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_txt]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_txt* updates
    if end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_txt.frameNStart = frameN  # exact frame index
        end_txt.tStart = t  # local t and not account for scr refresh
        end_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_txt, 'tStartRefresh')  # time at next scr refresh
        end_txt.setAutoDraw(True)
    if end_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_txt.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            end_txt.tStop = t  # not accounting for scr refresh
            end_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_txt, 'tStopRefresh')  # time at next scr refresh
            end_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='semicolon')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
