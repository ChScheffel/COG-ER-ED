﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Juni 15, 2021, at 13:07
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import random # for randomization of comparison order

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'ValueIterationTest'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\josep\\Documents\\04_Projekte\\01_COG-ED_Revision\\CogEmotED\\01_Paradigms\\COG-ED\\ValueIterationTest.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "InstructionED"
InstructionEDClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Nun beginnt der zweite Teil.\n\nDie unterschiedlichen Level, die Sie gerade absolviert haben, werden nun nacheinander gegenübergestellt.\nAuf dem Bildschirm erscheint die Frage "Welche Bezahlung würden Sie eher für welches Level annehmen?". Darunter befinden sich zwei Textfelder, zum Beispiel "1,00€ für das rote Level" und "1,00€ für das schwarze Level". Sie können die Frage beantworten, indem Sie mit der Maus (mit einem einfachen Klick) auf eins der beiden Felder klicken. Dabei geht es nicht um Schnelligkeit. Nachdem Sie geklickt haben, werden sich die Geldbeträge verändern und Sie können sich erneut entscheiden. Auf diese Weise werden alle Level miteinander verglichen werden.\n\nDrücken Sie die Leertaste, um zu beginnen.',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Necessary lists of variable names for the loops to refer to
EDlevcompList = ['schwarze', 'rote',
'rote', 'blaue',
'blaue', 'grüne',
'schwarze', 'grüne',
'rote', 'grüne',
'schwarze', 'blaue'] # these are all the comparison pairs that will be done
EDlevcolorList = ['black', 'darkred',
'darkred', 'darkblue',
'darkblue', 'darkgreen',
'black', 'darkgreen',
'darkred', 'darkgreen',
'black', 'darkblue']
EDroundList = ['EDround1', 'EDround2', 'EDround3', 'EDround4', 'EDround5', 'EDround6']
EDroundthisList = ['thisEDround1', 'thisEDround2', 'thisEDround3', 'thisEDround4', 'thisEDround5', 'thisEDround6']
EDroundclockList = ['EDround1Clock', 'EDround2Clock', 'EDround3Clock', 'EDround4Clock', 'EDround5Clock', 'EDround6Clock']
EDroundcompoList = ['EDround1Components', 'EDround2Components', 'EDround3Components', 'EDround4Components', 'EDround5Components', 'EDround6Components']
EDleftbuttonList = ['EDleftbutton1', 'EDleftbutton2', 'EDleftbutton3', 'EDleftbutton4', 'EDleftbutton5', 'EDleftbutton6']
EDrightbuttonList = ['EDrightbutton1', 'EDrightbutton2', 'EDrightbutton3', 'EDrightbutton4', 'EDrightbutton5', 'EDrightbutton6']
EDclickList = ['EDclick1', 'EDclick2', 'EDclick3', 'EDclick4', 'EDclick5', 'EDclick6']
EDsteps = [1,1,0.5,0.25,0.125,0.0625,0.03125,0.015625]
EDfix = [2]

# Create array corresponding to rounds of effort discounting aka the list elements
EDrounds = list(range(6))

# Create array corresponding to rounds of effort discounting within each comparison aka the list elements
EDmoney = list(range(7))

# Create array corresponding to every second element in the list of comparisons (which will be randomized in the loop for every participant)
EDcomps = [0,2,4,6,8,10]

# Initialize components for Routine "round" with a loop

random.shuffle(EDcomps)

for edx in EDrounds:
    globals()[EDroundclockList[edx]] = core.Clock()
    question = visual.TextStim(win=win, name='question',
        text='Welche Bezahlung würden Sie eher für welches Level annehmen?',
        font='Open Sans',
        pos=[0,0.1], height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    globals()[EDclickList[edx]] = event.Mouse(win=win)
    x, y = [None, None]
    globals()[EDclickList[edx]].mouseClock = core.Clock()
    globals()[EDleftbuttonList[edx]] = visual.ButtonStim(win, 
       text= '', font='Open Sans',
       pos=[-0.3,-0.15],units='height',
       letterHeight=0.03,
       size=[0.5,0.1], borderWidth=0.0,
       fillColor='darkgrey', borderColor=None,
       color=EDlevcolorList[EDcomps[edx]], colorSpace='rgb',
       opacity=None,
       bold=True, italic=False,
       padding=0.03,
       anchor='center',
       name=EDleftbuttonList[edx])
    globals()[EDleftbuttonList[edx]].buttonClock = core.Clock()
    globals()[EDrightbuttonList[edx]] = visual.ButtonStim(win, 
       text= '', font='Open Sans',
       pos=[0.3,-0.15],units='height',
       letterHeight=0.03,
       size=[0.5,0.1], borderWidth=0.0,
       fillColor='darkgrey', borderColor=None,
       color=EDlevcolorList[EDcomps[edx]+1], colorSpace='rgb',
       opacity=None,
       bold=True, italic=False,
       padding=0.03,
       anchor='center',
       name=EDrightbuttonList[edx])
    globals()[EDrightbuttonList[edx]].buttonClock = core.Clock()

# Initialize components for Routine "Goodbye"
GoodbyeClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Sie haben es geschafft!\n\nDas Experiment ist nun beendet. Bitte wenden Sie sich an die Versuchsleitung.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "InstructionED"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionEDComponents = [text, key_resp]
for thisComponent in InstructionEDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionEDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InstructionED"-------
while continueRoutine:
    # get current time
    t = InstructionEDClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionEDClock)
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
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionEDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InstructionED"-------
for thisComponent in InstructionEDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "InstructionED" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# -----------------------------
# Loop for the 6 comparisons
# -----------------------------

for edx in EDrounds:

    # set up handler to look after randomisation of conditions etc
    globals()[EDroundList[edx]] = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('..\\\\..\\\\..\\\\Stimuli\\\\Moneyvalues.xlsx'),
        seed=None, name=EDroundList[edx])
    thisExp.addLoop(globals()[EDroundList[edx]])  # add the loop to the experiment
    globals()[EDroundthisList[edx]] = globals()[EDroundList[edx]].trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if globals()[EDroundthisList[edx]] != None:
        for paramName in globals()[EDroundthisList[edx]]:
            vari = ['{} = ' + str(EDroundthisList[edx]) + '[paramName]']
            exec(vari[0].format(paramName))

    for globals()[EDroundthisList[edx]] in globals()[EDroundList[edx]]:
        currentLoop = globals()[EDroundList[edx]]
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if globals()[EDroundthisList[edx]] != None:
            for paramName in globals()[EDroundthisList[edx]]:
                vari = ['{} = ' + str(EDroundthisList[edx]) + '[paramName]']
                exec(vari[0].format(paramName))

        # ------Prepare to start Routine -------
        continueRoutine = True
        # update component parameters for each repeat
        if Currentstep == 0:
            # in the beginning, both buttons offer 1€ for both levels
            LB = str(format(EDsteps[0],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]]) + ' Level'
            RB = str(format(EDsteps[0],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]+1]) + ' Level'
        else:
            if lastLeftButton == 1:
            # if the participant chose the left button in the beginning, proceed as follows
            # the right button value is fixed to 2€
                RB = str(format(EDfix[0],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]+1]) + ' Level'
                # now adapt the value of the left button depending on the previous choice
                if Currentstep == 1:
                    # set the left button to 1€ (because this does not fit in with the iteration process yet)
                    LB = str(format(EDsteps[1],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]]) + ' Level' 
                    oldvalue = EDsteps[1]
                # iteration process
                else:
                    # if the cheaper option was chosen, lower that options value by the current EDsteps value
                    if lastLeftButton == 1:
                        newvalue = oldvalue - EDsteps[Currentstep]
                    # if the pricier option was chosen, raise the other options value by the current EDsteps value
                    else:
                        newvalue = oldvalue + EDsteps[Currentstep]
                    LB = str(format(newvalue,'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]]) + ' Level'
                    oldvalue = newvalue
            else:
            # if the participant chose the right button in the beginning, proceed as follows
            # the left button value is fixed to 2€
                LB = str(format(EDfix[0],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]+1]) + ' Level'
                # now adapt the value of the right button depending on the previous choice
                if Currentstep == 1:
                    # set the right button to 1€ (because this does not fit in with the iteration process yet)
                    RB = str(format(EDsteps[1],'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]]) + ' Level' 
                    oldvalue = EDsteps[1]
                # iteration process
                else:
                    # if the cheaper option was chosen, lower that options value by the current EDsteps value
                    if lastRightButton == 1:
                        newvalue = oldvalue - EDsteps[Currentstep]
                    # if the pricier option was chosen, raise the other options value by the current EDsteps value
                    else:
                        newvalue = oldvalue + EDsteps[Currentstep]
                    RB = str(format(newvalue,'.2f')) + '€ für das ' + str(EDlevcompList[EDcomps[edx]]) + ' Level'
                    oldvalue = newvalue
        
        globals()[EDleftbuttonList[edx]].setText(LB)
        globals()[EDrightbuttonList[edx]].setText(RB)
        # setup some python lists for storing info about the response click
        globals()[EDclickList[edx]].clicked_name = []
        gotValidClick = False  # until a click is received
        # keep track of which components have finished
        globals()[EDroundcompoList[edx]] = [question, globals()[EDclickList[edx]], globals()[EDleftbuttonList[edx]], globals()[EDrightbuttonList[edx]]]
        for thisComponent in globals()[EDroundcompoList[edx]]:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        globals()[EDroundclockList[edx]].reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine -------
        while continueRoutine:
            # get current time
            t = globals()[EDroundclockList[edx]].getTime()
            tThisFlip = win.getFutureFlipTime(clock=globals()[EDroundclockList[edx]])
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *question* updates
            if question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                question.frameNStart = frameN  # exact frame index
                question.tStart = t  # local t and not account for scr refresh
                question.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(question, 'tStartRefresh')  # time at next scr refresh
                question.setAutoDraw(True)
            # *response click* updates
            if globals()[EDclickList[edx]].status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                globals()[EDclickList[edx]].frameNStart = frameN  # exact frame index
                globals()[EDclickList[edx]].tStart = t  # local t and not account for scr refresh
                globals()[EDclickList[edx]].tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(globals()[EDclickList[edx]], 'tStartRefresh')  # time at next scr refresh
                globals()[EDclickList[edx]].status = STARTED
                globals()[EDclickList[edx]].mouseClock.reset()
                prevButtonState = globals()[EDclickList[edx]].getPressed()  # if button is down already this ISN'T a new click
            if globals()[EDclickList[edx]].status == STARTED:  # only update if started and not finished!
                buttons = globals()[EDclickList[edx]].getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        for obj in [globals()[EDleftbuttonList[edx]],globals()[EDrightbuttonList[edx]]]:
                            if obj.contains(globals()[EDclickList[edx]]):
                                gotValidClick = True
                                globals()[EDclickList[edx]].clicked_name.append(obj.name)
                        if gotValidClick:  # abort routine on response
                            continueRoutine = False
            
            # *LeftButton* updates
            if globals()[EDleftbuttonList[edx]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                globals()[EDleftbuttonList[edx]].frameNStart = frameN  # exact frame index
                globals()[EDleftbuttonList[edx]].tStart = t  # local t and not account for scr refresh
                globals()[EDleftbuttonList[edx]].tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(globals()[EDleftbuttonList[edx]], 'tStartRefresh')  # time at next scr refresh
                globals()[EDleftbuttonList[edx]].setAutoDraw(True)
            if globals()[EDleftbuttonList[edx]].status == STARTED:
                # check whether LeftButton has been pressed
                if globals()[EDleftbuttonList[edx]].isClicked:
                    if not globals()[EDleftbuttonList[edx]].wasClicked:
                        globals()[EDleftbuttonList[edx]].timesOn.append(globals()[EDleftbuttonList[edx]].buttonClock.getTime()) # store time of first click
                        globals()[EDleftbuttonList[edx]].timesOff.append(globals()[EDleftbuttonList[edx]].buttonClock.getTime()) # store time clicked until
                    else:
                        globals()[EDleftbuttonList[edx]].timesOff[-1] = globals()[EDleftbuttonList[edx]].buttonClock.getTime() # update time clicked until
                    if not globals()[EDleftbuttonList[edx]].wasClicked:
                        continueRoutine = False  # end routine when LeftButton is clicked
                        None
                    globals()[EDleftbuttonList[edx]].wasClicked = True  # if LeftButton is still clicked next frame, it is not a new click
                else:
                    globals()[EDleftbuttonList[edx]].wasClicked = False  # if LeftButton is clicked next frame, it is a new click
            else:
                globals()[EDleftbuttonList[edx]].buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
                globals()[EDleftbuttonList[edx]].wasClicked = False  # if LeftButton is clicked next frame, it is a new click
            
            # *RightButton* updates
            if globals()[EDrightbuttonList[edx]].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                globals()[EDrightbuttonList[edx]].frameNStart = frameN  # exact frame index
                globals()[EDrightbuttonList[edx]].tStart = t  # local t and not account for scr refresh
                globals()[EDrightbuttonList[edx]].tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(globals()[EDrightbuttonList[edx]], 'tStartRefresh')  # time at next scr refresh
                globals()[EDrightbuttonList[edx]].setAutoDraw(True)
            if globals()[EDrightbuttonList[edx]].status == STARTED:
                # check whether RightButton has been pressed
                if globals()[EDrightbuttonList[edx]].isClicked:
                    if not globals()[EDrightbuttonList[edx]].wasClicked:
                        globals()[EDrightbuttonList[edx]].timesOn.append(globals()[EDrightbuttonList[edx]].buttonClock.getTime()) # store time of first click
                        globals()[EDrightbuttonList[edx]].timesOff.append(globals()[EDrightbuttonList[edx]].buttonClock.getTime()) # store time clicked until
                    else:
                        globals()[EDrightbuttonList[edx]].timesOff[-1] = globals()[EDrightbuttonList[edx]].buttonClock.getTime() # update time clicked until
                    if not globals()[EDrightbuttonList[edx]].wasClicked:
                        continueRoutine = False  # end routine when RightButton is clicked
                        None
                    globals()[EDrightbuttonList[edx]].wasClicked = True  # if RightButton is still clicked next frame, it is not a new click
                else:
                    globals()[EDrightbuttonList[edx]].wasClicked = False  # if RightButton is clicked next frame, it is a new click
            else:
                globals()[EDrightbuttonList[edx]].buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
                globals()[EDrightbuttonList[edx]].wasClicked = False  # if RightButton is clicked next frame, it is a new click
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in globals()[EDroundcompoList[edx]]:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine-------
        for thisComponent in globals()[EDroundcompoList[edx]]:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        globals()[EDroundList[edx]].addData('question.started', question.tStartRefresh)
        globals()[EDroundList[edx]].addData('question.stopped', question.tStopRefresh)
        # store data for rounds (TrialHandler)
        x, y = globals()[EDclickList[edx]].getPos()
        buttons = globals()[EDclickList[edx]].getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            for obj in [globals()[EDleftbuttonList[edx]],globals()[EDrightbuttonList[edx]]]:
                if obj.contains(globals()[EDclickList[edx]]):
                    gotValidClick = True
                    globals()[EDclickList[edx]].clicked_name.append(obj.name)
        globals()[EDroundList[edx]].addData(str(EDclickList[edx]) + '.leftButton', buttons[0])
        globals()[EDroundList[edx]].addData(str(EDclickList[edx]) + '.midButton', buttons[1])
        globals()[EDroundList[edx]].addData(str(EDclickList[edx]) + '.rightButton', buttons[2])
        # store the last response in variables to be able to use them in the iteration process
        lastLeftButton = buttons[0]
        lastRightButton = buttons[2]
        if len(globals()[EDclickList[edx]].clicked_name):
            globals()[EDroundList[edx]].addData(str(EDclickList[edx]) + '.clicked_name', globals()[EDclickList[edx]].clicked_name[0])
        globals()[EDroundList[edx]].addData(str(EDleftbuttonList[edx]) + '.numClicks', globals()[EDleftbuttonList[edx]].numClicks)
        globals()[EDroundList[edx]].addData(str(EDrightbuttonList[edx]) + '.numClicks', globals()[EDrightbuttonList[edx]].numClicks)
        # open up the next row for more data
        thisExp.nextEntry()

    # the Routine was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()    
        
    
    
# completed 1.0 repeats of 'EDrounds'


# ------Prepare to start Routine "Goodbye"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GoodbyeComponents = [text_2]
for thisComponent in GoodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
GoodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Goodbye"-------
while continueRoutine:
    # get current time
    t = GoodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=GoodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GoodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Goodbye"-------
for thisComponent in GoodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# the Routine "Goodbye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
