'''
Survive 15-112 (Rated R for (I Will Be) Retaking This Class)

You are a 15-112 student. Kosbie is eternal. The void will claim all.

Intended features (as of 15/04/2026) (this is liable to change drastically):
- Scene 1: Dorm Room (sleep or face your fate)
- Sccene 2: Lecture Quiz (darkness is closing in)
- Scene 3: Lecture (doze off at your own peril)
- Scene 4: Gradescope (underworld 15-112 TAs grade lecture quizzes with freakish speed)
- Scene 5: FACE VOID-KOSBIE

Grading shortcuts: beats me dawg !! to be determined
'''

from cmu_graphics import *


# super awesome GLOBAL variables
width = 800
height = 600

# scene names
scene_dorm = 'dorm'
scene_quiz = 'quiz'
scene_lecture = 'lecture'
scene_gradescope = 'gradescope'
scene_boss = 'boss'
scene_dead = 'dead'
scene_win = 'win'

# colors
color_background = rgb(10, 5, 15)
color_blood_red = rgb(180, 10, 20)
color_void = rgb(20, 0, 40)
color_sickly = rgb(80, 180, 80)
color_bone = rgb(220, 210, 185)
color_eye = rgb(255, 200, 0)

# mvc
# oh brother
def onAppStart(app):
    app.width = width
    app.height = height
    app.stepsPerSecond = 60
    app.backgroundColor = rgb(10, 5, 15)
    app.bloodColor = rgb(180, 10, 20)
    app.voidColor = rgb(20, 0, 40)
    app.sicklyColor = rgb(80, 180, 80)
    app.boneColor = rgb(220, 210, 185)
    app.eyeColor = rgb(255, 200, 0)
    resetApp(app)

def resetApp(app):
    app.scene = scene_dorm
    app.mouseX = 0
    app.mouseY = 0
    app.deathMessage = []

def onStep(app):
    pass

def redrawAll(app):
    # background
    drawRect(0, 0, width, height, fill = app.backgroundColor)
    # placeholder for debugging
    drawLabel(f'Current scene: {app.scene}', width // 2, height // 2, size = 20, fill = app.boneColor, font = 'monospace')

def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onMousePress(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onKeyPress(app, key):
    # grading shortcuts once they are determined
    pass

# RUN !!!!!!!!!!!!
print("I am actually doing something this time...")
runApp(width = width, height = height)
