#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on Wed 15 Nov 2023 08:16:43 PM EET
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'ConstellationsNAI23'  # from the Builder filename that created this script
expInfo = {
    'Pseudonym*': '',
    'Age': '',
    'Gender': '',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['Pseudonym*'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='/home/herman/projects/ANI_PROJECT/Constellations_NAI2022_ENG.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='norm'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'norm'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
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
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "exp_intro" ---
    instruction4_2 = visual.ImageStim(
        win=win,
        name='instruction4_2', 
        image='stimuli/intro5.PNG', mask=None, anchor='center',
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
    
    # --- Initialize components for Routine "trial" ---
    image = visual.ImageStim(
        win=win,
        name='image', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.4, 0.0), size=(0.65,0.65),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    # Run 'Begin Experiment' code from code_6
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
       buttonRequired=True,
       depth=-3
    )
    instructions_txt = visual.TextStim(win=win, name='instructions_txt',
        text='Trace the contours to find an object!',
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
        text='What did you find in the image?',
        font='Open Sans',
        pos=(0.4, 0.55), height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-15.0);
    H1_textbox = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Open Sans',
         pos=(0.15, 0.5),     letterHeight=0.05,
         size=(0.65,0.4), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=None, alignment='center',
         anchor='top-left', overflow='visible',
         fillColor='white', borderColor='grey',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='H1_textbox',
         depth=-16, autoLog=True,
    )
    RSP_ahhaa = visual.Slider(win=win, name='RSP_ahhaa',
        startValue=None, size=(0.5, 0.06), pos=(0.5, -0.05), units=win.units,
        labels=['Very uncertain', 'Very certain'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='Black', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.04,
        flip=False, ori=0.0, depth=-17, readOnly=False)
    ahhaa_txt = visual.TextStim(win=win, name='ahhaa_txt',
        text='How certain are you that your answer is correct?',
        font='Open Sans',
        pos=(0.51, 0.05), height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-18.0);
    RSP_sudden = visual.Slider(win=win, name='RSP_sudden',
        startValue=None, size=(0.5, 0.06), pos=(0.5, -0.3), units=win.units,
        labels=['Very gradually', 'Very suddenly'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='Black', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.04,
        flip=False, ori=0.0, depth=-19, readOnly=False)
    sudden_txt = visual.TextStim(win=win, name='sudden_txt',
        text='How suddenly did the final answer arrive?',
        font='Open Sans',
        pos=(0.42, -0.2), height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-20.0);
    RSP_pleasant = visual.Slider(win=win, name='RSP_pleasant',
        startValue=None, size=(0.5, 0.06), pos=(0.5, -0.55), units=win.units,
        labels=['Very easy', 'Very difficult'],ticks=None, granularity=1,
        style='radio', styleTweaks=(), opacity=None,
        labelColor='Black', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.04,
        flip=False, ori=0.0, depth=-21, readOnly=False)
    pleasant_txt = visual.TextStim(win=win, name='pleasant_txt',
        text='How difficult was it to find a solution?',
        font='Open Sans',
        pos=(0.42, -0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-22.0);
    
    # --- Initialize components for Routine "pause" ---
    text = visual.TextStim(win=win, name='text',
        text=None,
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from code_4
    
    
    
    # --- Initialize components for Routine "end" ---
    end_txt = visual.TextStim(win=win, name='end_txt',
        text='The end. Thank you!',
        font='Open Sans',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "exp_intro" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('exp_intro.started', globalClock.getTime())
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
    frameN = -1
    
    # --- Run Routine "exp_intro" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction4_2* updates
        
        # if instruction4_2 is starting this frame...
        if instruction4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction4_2.frameNStart = frameN  # exact frame index
            instruction4_2.tStart = t  # local t and not account for scr refresh
            instruction4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction4_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            instruction4_2.status = STARTED
            instruction4_2.setAutoDraw(True)
        
        # if instruction4_2 is active this frame...
        if instruction4_2.status == STARTED:
            # update params
            pass
        # *mouse4_2* updates
        
        # if mouse4_2 is starting this frame...
        if mouse4_2.status == NOT_STARTED and t >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            mouse4_2.frameNStart = frameN  # exact frame index
            mouse4_2.tStart = t  # local t and not account for scr refresh
            mouse4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse4_2, 'tStartRefresh')  # time at next scr refresh
            # update status
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
                    clickableList = environmenttools.getFromNames([button4_2,], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse4_2):
                            gotValidClick = True
                            mouse4_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # end routine on response
        
        # *button4_2* updates
        
        # if button4_2 is starting this frame...
        if button4_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            button4_2.frameNStart = frameN  # exact frame index
            button4_2.tStart = t  # local t and not account for scr refresh
            button4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button4_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            button4_2.status = STARTED
            button4_2.setAutoDraw(True)
        
        # if button4_2 is active this frame...
        if button4_2.status == STARTED:
            # update params
            pass
        
        # *button_txt4_2* updates
        
        # if button_txt4_2 is starting this frame...
        if button_txt4_2.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            button_txt4_2.frameNStart = frameN  # exact frame index
            button_txt4_2.tStart = t  # local t and not account for scr refresh
            button_txt4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_txt4_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            button_txt4_2.status = STARTED
            button_txt4_2.setAutoDraw(True)
        
        # if button_txt4_2 is active this frame...
        if button_txt4_2.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_intro" ---
    for thisComponent in exp_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('exp_intro.stopped', globalClock.getTime())
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
            globals()[paramName] = thisTrial[paramName]
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        image.setImage(stim)
        # Run 'Begin Routine' code from code_6
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
        # Run 'Begin Routine' code from code
        #luup = 0
        #print("luup 0")
        
        RSP = 0
        Valmis = 0
        Yes = 0
        Vihje = 0
        Nupp = 0
        frames = 0
        buttons = 0
        times = 0
        location = 0
        
        show_next_btn = False
        show_done_btn = True
        
        mouseIsDown = False
        mouseIsDown1 = False
        mouseIsDown2 = False
        oldMouseIsDown = False
        
        mouse_track.xdraw = []
        mouse_track.ydraw = []
        clear = []
        
        
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # setup some python lists for storing info about the mouse_end
        mouse_end.clicked_name = []
        gotValidClick = False  # until a click is received
        H1_textbox.reset()
        H1_textbox.setText('')
        RSP_ahhaa.reset()
        RSP_sudden.reset()
        RSP_pleasant.reset()
        # keep track of which components have finished
        trialComponents = [image, mouse_track, brush, instructions_txt, times_up_txt, button_clear, clear_txt, mouse, button_next, next_txt, mouse_end, button_done, done_txt, object_txt, H1_textbox, RSP_ahhaa, ahhaa_txt, RSP_sudden, sudden_txt, RSP_pleasant, pleasant_txt]
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
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            # *mouse_track* updates
            
            # if mouse_track is starting this frame...
            if mouse_track.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_track.frameNStart = frameN  # exact frame index
                mouse_track.tStart = t  # local t and not account for scr refresh
                mouse_track.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_track, 'tStartRefresh')  # time at next scr refresh
                # update status
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
            
            # if brush is starting this frame...
            if brush.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                brush.frameNStart = frameN  # exact frame index
                brush.tStart = t  # local t and not account for scr refresh
                brush.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(brush, 'tStartRefresh')  # time at next scr refresh
                # update status
                brush.status = STARTED
                brush.setAutoDraw(True)
            
            # if brush is active this frame...
            if brush.status == STARTED:
                # update params
                pass
            
            # if brush is stopping this frame...
            if brush.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > brush.tStartRefresh + 30.0-frameTolerance:
                    # keep track of stop time/frame for later
                    brush.tStop = t  # not accounting for scr refresh
                    brush.frameNStop = frameN  # exact frame index
                    # update status
                    brush.status = FINISHED
                    brush.setAutoDraw(False)
            # Run 'Each Frame' code from code
            ## Mouse position recordnig
            if mouse_track.getPressed()[0] == 1:
                mouse_track.xdraw.append(mouse_track.getPos()[0])
                mouse_track.ydraw.append(mouse_track.getPos()[1])
            
            if show_done_btn and button_done.contains(mouse) and mouse.getPressed()[0]:
                show_next_btn = True
                show_done_btn = False
                
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
            if show_next_btn and button_next.contains(mouse_end) and mouse_end.getPressed()[0] == 1:
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
            
            
            # *instructions_txt* updates
            
            # if instructions_txt is starting this frame...
            if instructions_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructions_txt.frameNStart = frameN  # exact frame index
                instructions_txt.tStart = t  # local t and not account for scr refresh
                instructions_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructions_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                instructions_txt.status = STARTED
                instructions_txt.setAutoDraw(True)
            
            # if instructions_txt is active this frame...
            if instructions_txt.status == STARTED:
                # update params
                pass
            
            # if instructions_txt is stopping this frame...
            if instructions_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > instructions_txt.tStartRefresh + 5.0-frameTolerance:
                    # keep track of stop time/frame for later
                    instructions_txt.tStop = t  # not accounting for scr refresh
                    instructions_txt.frameNStop = frameN  # exact frame index
                    # update status
                    instructions_txt.status = FINISHED
                    instructions_txt.setAutoDraw(False)
            
            # *times_up_txt* updates
            
            # if times_up_txt is starting this frame...
            if times_up_txt.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                times_up_txt.frameNStart = frameN  # exact frame index
                times_up_txt.tStart = t  # local t and not account for scr refresh
                times_up_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(times_up_txt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'times_up_txt.started')
                # update status
                times_up_txt.status = STARTED
                times_up_txt.setAutoDraw(True)
            
            # if times_up_txt is active this frame...
            if times_up_txt.status == STARTED:
                # update params
                pass
            
            # *button_clear* updates
            
            # if button_clear is starting this frame...
            if button_clear.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                button_clear.frameNStart = frameN  # exact frame index
                button_clear.tStart = t  # local t and not account for scr refresh
                button_clear.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_clear, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_clear.status = STARTED
                button_clear.setAutoDraw(True)
            
            # if button_clear is active this frame...
            if button_clear.status == STARTED:
                # update params
                pass
            
            # *clear_txt* updates
            
            # if clear_txt is starting this frame...
            if clear_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                clear_txt.frameNStart = frameN  # exact frame index
                clear_txt.tStart = t  # local t and not account for scr refresh
                clear_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clear_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                clear_txt.status = STARTED
                clear_txt.setAutoDraw(True)
            
            # if clear_txt is active this frame...
            if clear_txt.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            
            # *button_next* updates
            
            # if button_next is starting this frame...
            if button_next.status == NOT_STARTED and show_next_btn:
                # keep track of start time/frame for later
                button_next.frameNStart = frameN  # exact frame index
                button_next.tStart = t  # local t and not account for scr refresh
                button_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_next, 'tStartRefresh')  # time at next scr refresh
                # update status
                button_next.status = STARTED
                button_next.setAutoDraw(True)
            
            # if button_next is active this frame...
            if button_next.status == STARTED:
                # update params
                pass
            
            # *next_txt* updates
            
            # if next_txt is starting this frame...
            if next_txt.status == NOT_STARTED and show_next_btn:
                # keep track of start time/frame for later
                next_txt.frameNStart = frameN  # exact frame index
                next_txt.tStart = t  # local t and not account for scr refresh
                next_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(next_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                next_txt.status = STARTED
                next_txt.setAutoDraw(True)
            
            # if next_txt is active this frame...
            if next_txt.status == STARTED:
                # update params
                pass
            # *mouse_end* updates
            
            # if mouse_end is starting this frame...
            if mouse_end.status == NOT_STARTED and show_done_btn:
                # keep track of start time/frame for later
                mouse_end.frameNStart = frameN  # exact frame index
                mouse_end.tStart = t  # local t and not account for scr refresh
                mouse_end.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_end, 'tStartRefresh')  # time at next scr refresh
                # update status
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
                        clickableList = environmenttools.getFromNames(button_next, namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_end):
                                gotValidClick = True
                                mouse_end.clicked_name.append(obj.name)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # *button_done* updates
            
            # if button_done is starting this frame...
            if button_done.status == NOT_STARTED and show_done_btn:
                # keep track of start time/frame for later
                button_done.frameNStart = frameN  # exact frame index
                button_done.tStart = t  # local t and not account for scr refresh
                button_done.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_done, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_done.started')
                # update status
                button_done.status = STARTED
                button_done.setAutoDraw(True)
            
            # if button_done is active this frame...
            if button_done.status == STARTED:
                # update params
                pass
            
            # if button_done is stopping this frame...
            if button_done.status == STARTED:
                if bool(show_next_btn):
                    # keep track of stop time/frame for later
                    button_done.tStop = t  # not accounting for scr refresh
                    button_done.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'button_done.stopped')
                    # update status
                    button_done.status = FINISHED
                    button_done.setAutoDraw(False)
            
            # *done_txt* updates
            
            # if done_txt is starting this frame...
            if done_txt.status == NOT_STARTED and show_done_btn:
                # keep track of start time/frame for later
                done_txt.frameNStart = frameN  # exact frame index
                done_txt.tStart = t  # local t and not account for scr refresh
                done_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(done_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                done_txt.status = STARTED
                done_txt.setAutoDraw(True)
            
            # if done_txt is active this frame...
            if done_txt.status == STARTED:
                # update params
                pass
            
            # if done_txt is stopping this frame...
            if done_txt.status == STARTED:
                if bool(show_next_btn):
                    # keep track of stop time/frame for later
                    done_txt.tStop = t  # not accounting for scr refresh
                    done_txt.frameNStop = frameN  # exact frame index
                    # update status
                    done_txt.status = FINISHED
                    done_txt.setAutoDraw(False)
            
            # *object_txt* updates
            
            # if object_txt is starting this frame...
            if object_txt.status == NOT_STARTED and Yes == 1:
                # keep track of start time/frame for later
                object_txt.frameNStart = frameN  # exact frame index
                object_txt.tStart = t  # local t and not account for scr refresh
                object_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(object_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                object_txt.status = STARTED
                object_txt.setAutoDraw(True)
            
            # if object_txt is active this frame...
            if object_txt.status == STARTED:
                # update params
                pass
            
            # *H1_textbox* updates
            
            # if H1_textbox is starting this frame...
            if H1_textbox.status == NOT_STARTED and Yes == 1:
                # keep track of start time/frame for later
                H1_textbox.frameNStart = frameN  # exact frame index
                H1_textbox.tStart = t  # local t and not account for scr refresh
                H1_textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(H1_textbox, 'tStartRefresh')  # time at next scr refresh
                # update status
                H1_textbox.status = STARTED
                H1_textbox.setAutoDraw(True)
            
            # if H1_textbox is active this frame...
            if H1_textbox.status == STARTED:
                # update params
                pass
            
            # *RSP_ahhaa* updates
            
            # if RSP_ahhaa is starting this frame...
            if RSP_ahhaa.status == NOT_STARTED and Yes == 1:
                # keep track of start time/frame for later
                RSP_ahhaa.frameNStart = frameN  # exact frame index
                RSP_ahhaa.tStart = t  # local t and not account for scr refresh
                RSP_ahhaa.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSP_ahhaa, 'tStartRefresh')  # time at next scr refresh
                # update status
                RSP_ahhaa.status = STARTED
                RSP_ahhaa.setAutoDraw(True)
            
            # if RSP_ahhaa is active this frame...
            if RSP_ahhaa.status == STARTED:
                # update params
                pass
            
            # *ahhaa_txt* updates
            
            # if ahhaa_txt is starting this frame...
            if ahhaa_txt.status == NOT_STARTED and Yes == 1:
                # keep track of start time/frame for later
                ahhaa_txt.frameNStart = frameN  # exact frame index
                ahhaa_txt.tStart = t  # local t and not account for scr refresh
                ahhaa_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ahhaa_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                ahhaa_txt.status = STARTED
                ahhaa_txt.setAutoDraw(True)
            
            # if ahhaa_txt is active this frame...
            if ahhaa_txt.status == STARTED:
                # update params
                pass
            
            # *RSP_sudden* updates
            
            # if RSP_sudden is starting this frame...
            if RSP_sudden.status == NOT_STARTED and Yes == 1:
                # keep track of start time/frame for later
                RSP_sudden.frameNStart = frameN  # exact frame index
                RSP_sudden.tStart = t  # local t and not account for scr refresh
                RSP_sudden.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSP_sudden, 'tStartRefresh')  # time at next scr refresh
                # update status
                RSP_sudden.status = STARTED
                RSP_sudden.setAutoDraw(True)
            
            # if RSP_sudden is active this frame...
            if RSP_sudden.status == STARTED:
                # update params
                pass
            
            # *sudden_txt* updates
            
            # if sudden_txt is starting this frame...
            if sudden_txt.status == NOT_STARTED and Yes == 1:
                # keep track of start time/frame for later
                sudden_txt.frameNStart = frameN  # exact frame index
                sudden_txt.tStart = t  # local t and not account for scr refresh
                sudden_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(sudden_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                sudden_txt.status = STARTED
                sudden_txt.setAutoDraw(True)
            
            # if sudden_txt is active this frame...
            if sudden_txt.status == STARTED:
                # update params
                pass
            
            # *RSP_pleasant* updates
            
            # if RSP_pleasant is starting this frame...
            if RSP_pleasant.status == NOT_STARTED and Yes == 1:
                # keep track of start time/frame for later
                RSP_pleasant.frameNStart = frameN  # exact frame index
                RSP_pleasant.tStart = t  # local t and not account for scr refresh
                RSP_pleasant.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RSP_pleasant, 'tStartRefresh')  # time at next scr refresh
                # update status
                RSP_pleasant.status = STARTED
                RSP_pleasant.setAutoDraw(True)
            
            # if RSP_pleasant is active this frame...
            if RSP_pleasant.status == STARTED:
                # update params
                pass
            
            # *pleasant_txt* updates
            
            # if pleasant_txt is starting this frame...
            if pleasant_txt.status == NOT_STARTED and Yes == 1:
                # keep track of start time/frame for later
                pleasant_txt.frameNStart = frameN  # exact frame index
                pleasant_txt.tStart = t  # local t and not account for scr refresh
                pleasant_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pleasant_txt, 'tStartRefresh')  # time at next scr refresh
                # update status
                pleasant_txt.status = STARTED
                pleasant_txt.setAutoDraw(True)
            
            # if pleasant_txt is active this frame...
            if pleasant_txt.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # Run 'End Routine' code from code_6
        thisExp.addData('Version ' + str(vrs), Version)
        # store data for trials (TrialHandler)
        trials.addData('mouse_track.x', mouse_track.x)
        trials.addData('mouse_track.y', mouse_track.y)
        trials.addData('mouse_track.leftButton', mouse_track.leftButton)
        trials.addData('mouse_track.midButton', mouse_track.midButton)
        trials.addData('mouse_track.rightButton', mouse_track.rightButton)
        trials.addData('mouse_track.time', mouse_track.time)
        # Run 'End Routine' code from code
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
        
        
        # store data for trials (TrialHandler)
        # store data for trials (TrialHandler)
        trials.addData('H1_textbox.text',H1_textbox.text)
        trials.addData('RSP_ahhaa.response', RSP_ahhaa.getRating())
        trials.addData('RSP_ahhaa.rt', RSP_ahhaa.getRT())
        trials.addData('RSP_ahhaa.history', RSP_ahhaa.getHistory())
        trials.addData('RSP_sudden.response', RSP_sudden.getRating())
        trials.addData('RSP_sudden.rt', RSP_sudden.getRT())
        trials.addData('RSP_sudden.history', RSP_sudden.getHistory())
        trials.addData('RSP_pleasant.response', RSP_pleasant.getRating())
        trials.addData('RSP_pleasant.rt', RSP_pleasant.getRT())
        trials.addData('RSP_pleasant.history', RSP_pleasant.getHistory())
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'trials'
    
    
    # --- Prepare to start Routine "pause" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('pause.started', globalClock.getTime())
    # Run 'Begin Routine' code from code_4
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
    frameN = -1
    
    # --- Run Routine "pause" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.3:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "pause" ---
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('pause.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.300000)
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
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
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_txt* updates
        
        # if end_txt is starting this frame...
        if end_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_txt.frameNStart = frameN  # exact frame index
            end_txt.tStart = t  # local t and not account for scr refresh
            end_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_txt.status = STARTED
            end_txt.setAutoDraw(True)
        
        # if end_txt is active this frame...
        if end_txt.status == STARTED:
            # update params
            pass
        
        # if end_txt is stopping this frame...
        if end_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_txt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                end_txt.tStop = t  # not accounting for scr refresh
                end_txt.frameNStop = frameN  # exact frame index
                # update status
                end_txt.status = FINISHED
                end_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='semicolon')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
