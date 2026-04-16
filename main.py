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
import math


# super awesome GLOBAL variables
width = 800
height = 600

# scene names
dormScene = 'dorm'
quizScene = 'quiz'
lectureScene = 'lecture'
gradescopeScene = 'gradescope'
bossScene = 'boss'
deadScene = 'dead'
winScene = 'win'

def loadAssets(app):
    app.dormScene = 'assets/dorm_scene.png'
    app.lectureQuizScene = 'assets/lecture_quiz.png'
    app.lectureScene = 'assets/lecture_scene.png'
    app.gradescopeScene = 'assets/notfication_scene.png'
    app.bossScene = 'assets/battle_arena.png'

    app.idleKosbie = 'assets/kosbie_idle.png'
    app.angryKosbie = 'assets/kosbie_angry.png'
    app.kosbieAttack = 'assets/kosbie_attack.png'
    app.studentHit = 'assets/student_hit.png'
    app.studentIdle = 'assets/student_idle.png'
    app.voidCreature = 'assets/void_creature.png'

    app.projectile = 'assets/projectile.png'
    app.jolt = 'assets/jolt.png'

    app.backgroundSize = (800, 600)
    app.kosbieSize = (300, 300)
    app.studentSize = (300, 300)
    app.voidSize = (300, 300)
    app.projectileSize = (24, 24)
    app.joltSize = (40, 40)

def drawBackground(app, img):
    # stretches all my poorly sized background images to fit window
    drawImage(img, 0, 0, width = app.backgroundSize[0], height = app.backgroundSize[1])

def drawKosbie(app, cx, cy, angry = False):
    # I think the function name should give it away
    # angry = evil deity emerges
    img = app.angryKosbie if angry else app.idleKosbie
    width, height = app.kosbieSize
    drawImage(img, cx, cy, align = 'center', width = width, height = height)

    # nametag
    name = 'David Kosbie, Master of Darkness' if angry else 'Prof. Kosbie'
    drawLabel(name, cx, cy + height//2 + 5, size = 15, fill = app.boneColor, bold = True, font = 'monospace')

def drawStudent(app, cx, cy, hit = False):
    # draw player centered at (cx, cy)
    img = app.studentHit if hit else app.studentIdle
    width, height = app.studentSize
    drawImage(img, cx, cy, align = 'center', width = width, height = height)

def drawVoidCreature(app, cx, cy):
    width, height = app.voidSize
    drawImage(app.voidCreature, cx, cy, align = 'center', width = width, height = height)

def drawProjectile(app, cx, cy):
    width, height = app.projectileSize
    drawImage(app.projectile, cx, cy, align = 'center', width = width, height = height)

def drawJolt(app, cx, cy):
    width, height = app.joltSize
    drawImage(app.jolt, cx, cy, align = 'center', width = width, height = height)

def isHovered(app, cx, cy, width, height, mouseX = None, mouseY = None):
    # returns True if mouse is inside rectangle at (cx, cy)
    x = app.mouseX if mouseX is None else mouseX
    y = app.mouseY if mouseY is None else mouseY
    return (cx - width//2 <= x <= cx + width//2 and cy - height//2 <= y <= cy + height//2)

def floatOffset(app, speed = 0.05, magnitude = 6):
    # smooth up-down offset using sine wave
    # ai consultation
    return int(magnitude * math.sin(app.stepCount * speed))

def drawButton(app, cx, cy, width, height, label):
    # button that glows red on hover
    hovered = isHovered(app, cx, cy, width, height)
    borderColor = app.bloodColor if hovered else rgb(100, 20, 20)
    backgroundColor = rgb(40, 10, 10) if hovered else rgb(20, 5, 5)
    drawRect(cx - width//2, cy - height//2, width, height,
             fill=backgroundColor, border=borderColor, borderWidth=2)
    drawLabel(label, cx, cy, size=16, fill=app.boneColor,
              bold=True, font='Georgia')

def drawUnpleasantTitle(app, text, cx, cy, size=32):
    # title text with red shadow offset for dramatic effect
    drawLabel(text, cx+3, cy+3, size=size, fill=app.bloodColor,
              bold=True, font='Georgia')
    drawLabel(text, cx, cy, size=size, fill=app.boneColor,
              bold=True, font='Georgia')

def drawHealthBar(app, cx, cy, width, height, current, maxVal, color, label = ''):
    drawRect(cx - width//2, cy - height//2, width, height, fill=rgb(20, 5, 5), border=rgb(80, 20, 20), borderWidth=2)
    fillW = int(width * max(0, current) / maxVal)
    if fillW > 0:
        drawRect(cx - width//2, cy - height//2, fillW, height, fill=color)
    if label:
        drawLabel(f'{label}: {current}/{maxVal}', cx, cy,
                  size=12, fill=app.boneColor, font='monospace')
        
def drawVignette(app, opacity):
    # dark edges that close in as your hopes of survival slip away
    if opacity <= 0:
        return
    drawRect(0, 0, 120, height, fill=app.voidColor, opacity=opacity)
    drawRect(width - 120, 0, 120, height, fill=app.voidColor, opacity=opacity)
    drawRect(0, 0, width,  80,  fill=app.voidColor, opacity=opacity)
    drawRect(0, height - 80, width,  80,  fill=app.voidColor, opacity=opacity)


# SCENE 1: DORM ROOM !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def dormDraw(app):
    drawBackground(app, app.dormScene)

    #time/flavor text
    drawUnpleasantTitle(app, '3:47 AM', width//2, 50, size = 24)
    drawLabel('Your 15-112 homework is due in 4 hours.', width//2, 85, size = 13, fill = app.boneColor, font = 'Georgia')
    drawLabel('You should probably get up, huh?', width//2, 108, size = 13, fill = app.boneColor, font = 'Georgia')

    # student in bed
    drawStudent(app, width//2, 270 + floatOffset(app))

    # choice prompt
    drawUnpleasantTitle(app, 'WHAT DO YOU DO?', width//2, 450, size = 22)
    drawButton(app, width//2 - 160, 520, 240, 48, 'Keep sleeping')
    drawButton(app, width//2 + 160, 520, 240, 48, 'Get your ass to lecture')

def dormOnMousePress(app, mouseX, mouseY):
    # sleep is the cousin of death
    # do you like all my magic numbers
    if isHovered(app, width//2 - 160, 520, 220, 48, mouseX, mouseY):
        app.deathMessage = [
            'YOU CHOSE SLEEP.',
            '',
            'A shadow descends from the ceiling.',
            'It smells faintly of chalk and despair.',
            '',
            '"OFFICE HOURS were YESTERDAY," he (it?) intones.'
            '',
            'Your QPA becomes a complex number.',
            '',
            'GAME OVER.'
        ]
        app.scene = deadScene
    elif isHovered(app, width//2 + 160, 520, 240, 48, mouseX, mouseY):
        app.scene = quizScene

# DEAD SCENE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def deadDraw(app):
    drawRect(0, 0, width, height, fill = 'black')
    drawUnpleasantTitle(app, 'INSTANT DEATH', width//2, 70, size = 70)
    # this function written with AI
    for i, line in enumerate(app.deathMessage):
        color = app.bloodColor if i == 0 else app.boneColor
        size = 22 if i == 0 else 14
        drawLabel(line, width//2, 150 + i * 32, size = size, fill = color, bold = (i == 0), font = 'Georgia')
    # end of AI slop
    drawButton(app, width//2, height - 60, 240, 44, 'Try again (good luck)')

def deadOnMousePress(app, mouseX, mouseY):
    if isHovered(app, width//2, height - 60, 240, 44, mouseX, mouseY):
        resetApp(app)

# SCENE 2: PRE-LECTURE QUIZ !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# questions: (question, [choices], correct index)
quizQuestions = [ 
    ("What does MVC stand for?",
    ["Model View Controller", "My Very (Bad Grade in this) Class", "My Variable Crashed", "Mysterious Void Calls"], 0),
    ("Time complexity of linear search?",
     ["O(1)", "O(log n)", "O(n)", "O(n^2)"], 2),
    ("What is the radius of the sun?", ["432,288 miles", "432,289 miles", "432,290 miles", "432,291 miles"], 0),
    ("Which keyword defines a function?", ["function", "makeFunction", "makeFunctionPlease", "def"], 3),
    ("What prevents infinite recursion?", ["Global, single-letter variables", "A well-placed magic number", "A base case", "More RAM"], 2),
    ("What does len([1, 2, 3]) return?", ["ion even know zlawg", "3", "2", "Immediate crash"], 1)
]

# button positions for 4 answer choices (might need to adjust for long question)
answerPositions = [(230, 320), (570, 320), (230, 400), (570, 400)]

def resetQuiz(app):
    app.quizIndex = 0
    app.quizWrong = 0
    app.quizFeedback = ''
    app.quizFeedbackTimer = 0

def quizOnStep(app):
    if app.quizFeedbackTimer > 0:
        app.quizFeedbackTimer -= 1

def quizDraw(app):
    drawBackground(app, app.lectureQuizScene)

    # vignette closes in with each wrong answer
    drawVignette(app, min(90, app.quizWrong * 22))

    # void creatures appear in corners as wrong answers accumulate
    for i in range(app.quizWrong):
        cx = 60 if i % 2 == 0 else width - 60
        cy = 80 if i < 2 else height - 80
        drawVoidCreature(app, cx, cy + floatOffset(app, speed = 0.04 + i * 0.01))
    
    drawUnpleasantTitle(app, 'PRE-LECTURE QUIZ', width //2, 35, size = 26)
    drawLabel('With every wrong answer, they draw nearer.', width //2, 68, size = 12, fill = rgb(180, 100, 100), font = 'Georgia')

    # once done
    if app.quizIndex >= len(quizQuestions):
        drawRect(100, height//2-50, 600, 120, fill = rgb(10, 5, 20), border = app.bloodColor, borderWidth = 2, opacity = 90)
        message = ("You answered everything correctly! The beast retreats for the time being."
        if app.quizWrong == 0 else f'You got {app.quizWrong} wrong. It is watching.')
        drawLabel(message, width//2, height//2, size = 30, fill = app.bloodColor, font = 'Georgia')
        drawButton(app, width//2, height//2+60, 280, 48, 'Time to go to lecture!')
        return
    
    # current question
    question, choices, correctIndex = quizQuestions[app.quizIndex]
    drawRect(80, 90, 640, 90, fill = rgb(15, 8, 28), border = rgb(80, 40, 80), borderWidth = 2)
    drawLabel(f'Q{app.quizIndex + 1}: {question}', width//2, 135, size = 15, fill = app.boneColor, font = 'Georgia')

    # answer buttons ughghghhghghghghgh I'm so tired of this
    # ai consulted for enumerate function
    for i, (cx, cy) in enumerate(answerPositions):
        drawButton(app, cx, cy, 300, 50, choices[i])
    
    # feedback flash
    if app.quizFeedback == 'correct':
        drawLabel('Correct! You live to die another day.', width//2, 480, size=16, fill=app.sicklyColor, bold=True, font='Georgia')
    elif app.quizFeedback == 'wrong':
        drawLabel('Wrong. Something stirs in the dark.', width//2, 480,
                  size=16, fill=app.bloodColor, bold=True, font='Georgia')
    
    # progress
    drawLabel(f'Question {app.quizIndex + 1} of {len(quizQuestions)}', width //2, 500, size = 12, fill = rgb(100, 80, 90), font = 'Georgia')

def quizOnMousePress(app, mouseX, mouseY):
    # waiting for feedback to clear
    if app.quizFeedbackTimer > 0:
        return
 
    # continue to lecture button 
    if app.quizIndex >= len(quizQuestions):
        if isHovered(app, width//2, height//2 + 60, 280, 48, mouseX, mouseY):
            resetLecture(app)
            app.scene = lectureScene
        return
 
    # check which answer was clicked
    question, choices, correctIndex = quizQuestions[app.quizIndex]
    for i, (cx, cy) in enumerate(answerPositions):
        if isHovered(app, cx, cy, 300, 50, mouseX, mouseY):
            if i == correctIndex:
                app.quizFeedback = 'correct'
            else:
                app.quizFeedback = 'wrong'
                app.quizWrong += 1
            app.quizFeedbackTimer = 50
            app.quizIndex += 1
            break

# scene 3: lecture !!!!!!! (stay awake!!)
lectureDuration = 20 * 60
sleepMax = 100

def resetLecture(app):
    app.sleepMeter = 0
    app.lectureTimer = lectureDuration
    app.clickSparks = []
    app.lectureDone = False

def resetGradescope(app):
    pass

def lectureOnStep(app):
    if app.lectureDone:
        return
    
    # sleep meter rises passively each step
    app.sleepMeter = min(sleepMax, app.sleepMeter + 0.15)
    app.lectureTimer -= 1

    # age and clean up sparks
    app.clickSparks = [(x, y, age+1) for (x, y, age) in app.clickSparks if age < 25]

    # fell asleep
    if app.sleepMeter >= sleepMax:
        app.deathMessage = [
            'YOU FELL ASLEEP IN LECTURE.',
            '',
            'You wake up briefly — just long enough',
            'to see your Gradescope notification.',
            '',
            '"MISSING: 47 assignments"',
            '"GRADE: Infintesimally small"',
            '',
            'GAME OVER.',
        ]
        app.scene = deadScene
        return
    
    # survived whole lecture
    if app.lectureTimer <= 0:
        app.lectureDone = True
    
def lectureDraw(app):
    drawBackground(app, app.lectureScene)

    # Kosbie at front; gets angry as you get sleepier
    drawKosbie(app, width//2, 180 + floatOffset(app, speed = 0.03, magnitude = 4), angry = (app.sleepMeter > 70))

    # vignette darkens as sleep meter fills
    drawVignette(app, int(app.sleepMeter * 0.7))

    # sleep meter HUD
    drawLabel('CONSCIOUSNESS', 140, 555, size = 13, fill = app.boneColor, font = 'Georgia')
    drawHealthBar(app, 420, 555, 340, 22, int(sleepMax - app.sleepMeter), sleepMax, app.sicklyColor, 'Awake')

    # countdown timer !
    secsLeft = app.lectureTimer // 60
    drawLabel(f'Time remaining: {secsLeft}s', width - 80, 25, size = 12, fill = rgb(120, 100, 100), font = 'Georgia')

    # click sparks
    for (x, y, age) in app.clickSparks:
        opacity = max(0, 100 - age * 4)
        drawJolt(app, x, y - age * 2)
    if app.lectureDone:
        drawRect(150, 220, 500, 160, fill=rgb(10, 5, 20),
                 border=app.bloodColor, borderWidth=3)
        drawLabel('You survived the lecture.', width//2, 270,
                  size=18, fill=app.boneColor, bold=True, font='Georgia')
        drawLabel('Your phone buzzes.', width//2, 305,
                  size=14, fill=rgb(180, 150, 150), font='Georgia')
        drawLabel("It's a Gradescope notification.", width//2, 330,
                  size=14, fill=app.bloodColor, font='Georgia')
        drawButton(app, width//2, 375, 260, 44, 'Check Gradescope (sorry)')   
    else:
        # prompt pulses red when danger is high
        promptColor = app.bloodColor if app.sleepMeter > 60 else rgb(120, 80, 80)
        drawLabel('CLICK ANYWHERE TO STAY AWAKE', width//2, height - 20,
                  size=14, fill=promptColor, bold=(app.sleepMeter > 60),
                  font='Georgia')
        
def lectureOnMousePress(app, mouseX, mouseY):
    if app.lectureDone:
        if isHovered(app, width//2, 375, 260, 44, mouseX, mouseY):
            resetGradescope(app)
            app.scene = gradescopeScene
        return
 
    # clicking reduces sleep meter & spawns a jolt spark
    app.sleepMeter  = max(0, app.sleepMeter - 20)
    app.clickSparks.append((mouseX, mouseY, 0))         

# mvc
# oh brother

def onAppStart(app):
    app.width = width
    app.height = height
    app.stepsPerSecond = 60
    app.stepCount = 0
    app.backgroundColor = rgb(10, 5, 15)
    app.bloodColor = rgb(180, 10, 20)
    app.voidColor = rgb(20, 0, 40)
    app.sicklyColor = rgb(80, 180, 80)
    app.boneColor = rgb(240, 235, 225)
    app.eyeColor = rgb(255, 200, 0)
    loadAssets(app)
    resetApp(app)

def resetApp(app):
    app.scene = dormScene
    app.mouseX = 0
    app.mouseY = 0
    app.deathMessage = []
    app.quizIndex = 0
    app.quizWrong = 0
    resetQuiz(app)

def onStep(app):
    app.stepCount += 1
    if app.scene == quizScene: quizOnStep(app)
    elif app.scene == lectureScene: lectureOnStep(app)

def redrawAll(app):
    if app.scene == dormScene: dormDraw(app)
    elif app.scene == quizScene: quizDraw(app)
    elif app.scene == lectureScene: lectureDraw(app)
    elif app.scene == deadScene: deadDraw(app)
    else:
        # I have not made these scenes whoops
        drawRect(0, 0, width, height, fill = 'black')
        drawLabel(f'scene {app.scene} coming soon !! hang tight', width//2, height//2, size = 20, fill = app.boneColor, font = 'monospace')

def onMouseMove(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY

def onMousePress(app, mouseX, mouseY):
    app.mouseX = mouseX
    app.mouseY = mouseY
    if app.scene ==  dormScene: dormOnMousePress(app, mouseX, mouseY)
    elif app.scene == quizScene: quizOnMousePress(app, mouseX, mouseY)
    elif app.scene == lectureScene: lectureOnMousePress(app, mouseX, mouseY)
    elif app.scene == deadScene: deadOnMousePress(app, mouseX, mouseY)

def onKeyPress(app, key):
    # grading shortcuts once they are determined
    pass

# RUN !!!!!!!!!!!!
runApp(width = width, height = height)
