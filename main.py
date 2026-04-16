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
    app.gradescopeScene = 'assets/notification_scene.png'
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

# scene 4: gradescope
def resetGradescope(app):
    app.gsPhase = 0 # 0 = notification, 1 = score, 2 = comment
    app.gsTimer = 0 # counts up to trigger phases

def gradescopeOnStep(app):
    app.gsTimer += 1
    # reveal a new phrase every 90 steps (1.5 sceonds)
    if app.gsTimer % 90 == 0 and app.gsPhase < 2:
        app.gsPhase += 1

def gradescopeDraw(app):
    drawBackground(app, app.gradescopeScene)
    drawUnpleasantTitle(app, 'NEW NOTIFICATION', width//2, 45, size = 26)

    # phone frame
    drawRect(width//2 - 160, 80, 320, 420, fill = rgb(12, 8, 20), border = rgb(60, 40, 80), borderWidth = 4)
    drawRect(width//2 - 148, 95, 296, 390, fill=rgb(8, 4, 16))

    # gradescope header  
    drawLabel('Gradescope', width//2, 125, size = 18, fill = rgb(240, 120, 60), bold = True, font = 'Georgia')
    drawLine(width//2 - 110, 140, width//2 + 110, 140, fill = rgb(60, 40, 40))

    # phase 0: assignment name
    drawLabel('Assignment graded:', width//2, 165, size = 13, fill = app.boneColor, font = 'Georgia')
    drawLabel('HW #42: The Final Reckoning', width//2, 188, size = 12, fill = rgb(200, 180, 160), font = 'Georgia')

    # phase 1: the score
    if app.gsPhase >= 1:
        drawLabel('Your Score:', width//2, 230, size = 14, fill = app.boneColor, bold = True, font = 'Georgia')
        drawUnpleasantTitle(app, '-5,000,000,000 / 100', width//2, 268, size = 20)
        drawLabel('(-5 billion points deducted for', width//2, 300, size = 11, fill = rgb(180, 100, 100), font = 'Georgia')
        drawLabel('"crimes against recursion")', width//2, 318, size = 11, fill = rgb(180, 100, 100), font = 'Georgia')

    # phase 2: grader comment + proceed button
    if app.gsPhase >= 2:
        drawLine(width//2-110, 340, width//2 + 110, 340, fill = rgb(60, 40, 40))
        drawLabel('Grader comment:', width//2, 362, size = 12, fill = app.boneColor, font = 'Georgia')
        drawUnpleasantTitle(app, '"Your end is nigh." - K', width//2, 392, size = 14)
        drawButton(app, width//2, 490, 260, 44, 'Face your fate')

def gradescopeOnMousePress(app, mouseX, mouseY):
    if app.gsPhase >= 2:
        if isHovered(app, width//2, 490, 260, 44, mouseX, mouseY):
            resetBoss(app)
            app.scene = bossScene

def resetBoss(app):
    pass

# scene 5: boss battle !!!!!!!!!!!!!!
playerMax = 100
bossMax = 200

def resetBoss(app):
    app.playerHp = playerMax
    app.bossHp = bossMax
    app.bossX = width//2
    app.bossY = 180
    app.bossVx = 2.0
    app.bossVy = 0.8
    app.playerX = width//2
    app.playerY = height - 120
    app.projectiles = [] # [x, y, vx, vy]
    app.spawnTimer = 0
    app.playerHitTimer = 0 # flashes player on hit
    app.bossHitTimer = 0 # flashes boss on hit
    app.bossOver = False

def bossOnStep(app):
    if app.bossOver:
        return
    
    # kosbie drifts around upper half of screen
    app.bossX += app.bossVx
    app.bossY += app.bossVy
    if app.bossX < 100 or app.bossX > width - 100:
        app.bossVx *= -1
    if app.bossY < 80 or app.bossY > 280:
        app.bossVy *= -1
    
    # phase 2: faster when below half hp
    speed = 3.5 if app.bossHp < bossMax//2 else 2.0
    app.bossVx = speed * (1 if app.bossVx > 0 else -1)

    # spawn projectiles aimed at player
    app.spawnTimer += 1
    spawnRate = 30 if app.bossHp < bossMax//2 else 55
    if app.spawnTimer >= spawnRate:
        app.spawnTimer = 0
        dx = app.playerX - app.bossX
        dy = app.playerY - app.bossY
        dist = math.sqrt(dx**2 + dy**2) or 1
        speed = 4
        app.projectiles.append([app.bossX, app.bossY, dx/dist * speed, dy/dist * speed])

    # move projectiles and check for collision
    surviving = []
    for p in app.projectiles:
        p[0] += p[2]
        p[1] += p[3]
        hitPlayer = math.sqrt((p[0] - app.playerX)**2 + (p[1]-app.playerY)**2) < 25
        onScreen = 0 <= p[0] <= width and 0 <= p[1] <= height
        if hitPlayer:
            app.playerHp -= 12
            app.playerHitTimer = 10
        elif onScreen:
            surviving.append(p)
    app.projectiles = surviving

    # tick hit flash timers
    if app.playerHitTimer > 0: app.playerHitTimer -= 1
    if app.bossHitTimer > 0: app.bossHitTimer -= 1

    # check win/lose
    if app.playerHp <= 0:
        app.deathMessage = [
            'YOU HAVE BEEN ABSORBED',
            '',
            'Your final grade: Empty set',
            'Your transcript reads only:',
            '"STUDENT HAS BEEN CLAIMED BY THE INFINITE."',
            '',
            'GAME OVER.'
        ]
        app.bossOver = True
        app.scene = deadScene
    elif app.bossHp <= 0:
        app.bossOver = True
        app.scene = winScene

def bossDraw(app):
    drawBackground(app, app.bossScene)

    # kosbie flashes white when hit
    drawKosbie(app, int(app.bossX), int(app.bossY) + floatOffset(app, speed = 0.04, magnitude = 8), angry = True)
    if app.bossHitTimer > 0:
        drawCircle(int(app.bossX), int(app.bossY), 80, fill = 'white', opacity = 40)
    
    # projectiles
    for p in app.projectiles:
        drawProjectile(app, int(p[0]), int(p[1]))
    
    # player flashes red when hit
    playerColor = app.bloodColor if app.playerHitTimer > 0 else None
    drawStudent(app, int(app.playerX), int(app.playerY), hit = (app.playerHitTimer >0))
    if playerColor:
        drawCircle(int(app.playerX), int(app.playerY), 40, fill = app.bloodColor, opacity = 30)

    # HUD
    # background strip
    drawRect(0, height - 55, width, 55, fill=rgb(10, 5, 15), opacity=85)

    # player HP bar 
    drawLabel('YOU', 80, height - 38, size=12, fill=app.boneColor, 
          bold=True, font='Georgia')
    drawHealthBar(app, 80, height - 20, 140, 18, 
              app.playerHp, playerMax, app.sicklyColor)

    # phase label
    phase = 2 if app.bossHp < bossMax//2 else 1
    phaseColor = app.eyeColor if phase == 2 else app.boneColor
    drawLabel(f'PHASE {phase}', width//2, height - 28, size=16, fill=phaseColor, bold=True, font='Georgia')

    # boss HP bar - right side
    drawLabel('KOSBIE', width - 80, height - 38, size=12, fill=app.boneColor, bold=True, font='Georgia')
    drawHealthBar(app, width - 80, height - 20, 140, 18, app.bossHp, bossMax, app.bloodColor)

    # instruction
    drawLabel('Click near Kosbie to attack — dodge the orbs', width//2, height - 8, size=10, fill=rgb(120, 100, 100), font='Georgia')

def bossOnMousePress(app, mouseX, mouseY):
    if app.bossOver:
        return
    # move player to click position
    app.playerX = mouseX
    app.playerY = mouseY
    # attack if click is close enough to boss
    dist = math.sqrt((mouseX - app.bossX)**2 + (mouseY - app.bossY)**2)
    if dist < 140:
        damage = 15 if app.bossHp > bossMax//2 else 10
        app.bossHp = max(0, app.bossHp - damage)
        app.bossHitTimer = 8

# win scene !!!!!!!!!!! HUZZAH !!!
def winDraw(app):
    drawRect(0, 0, width, height, fill = rgb(5, 0, 15))
    drawUnpleasantTitle(app, 'YOU WIN?!', width//2, 100, size = 48)
    lines = [
        'The darkness retreats.',
        'Your grade updates on Gradescope.',
        '',
        'Score: 101/100',
        '(+1 for surviving the unspeakable)',
        '',
        'Prof. Kosbie sends you an email:',
        '"Passable work."',
        '"See you next semester."'
    ]
    for i, line in enumerate(lines):
        drawLabel(line, width//2, 170 + i * 28, size= 14, fill = app.boneColor, font = 'Georgia')
    drawButton(app, width//2, height - 60, 200, 44, 'Back for more?')

def winOnMousePress(app, mouseX, mouseY):
    if isHovered(app, width//2, height - 60, 200, 44, mouseX, mouseY):
        resetApp(app)

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
    resetLecture(app)
    resetGradescope(app)
    resetBoss(app)

def onStep(app):
    app.stepCount += 1
    if app.scene == quizScene: quizOnStep(app)
    elif app.scene == lectureScene: lectureOnStep(app)
    elif app.scene == gradescopeScene: gradescopeOnStep(app)
    elif app.scene == bossScene: bossOnStep(app)

def redrawAll(app):
    if app.scene == dormScene: dormDraw(app)
    elif app.scene == quizScene: quizDraw(app)
    elif app.scene == lectureScene: lectureDraw(app)
    elif app.scene == gradescopeScene: gradescopeDraw(app)
    elif app.scene == bossScene: bossDraw(app)
    elif app.scene == deadScene: deadDraw(app)
    elif app.scene == winScene: winDraw(app)
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
    elif app.scene == gradescopeScene: gradescopeOnMousePress(app, mouseX, mouseY)
    elif app.scene == bossScene: bossOnMousePress(app, mouseX, mouseY)
    elif app.scene == deadScene: deadOnMousePress(app, mouseX, mouseY)
    elif app.scene == winScene: winOnMousePress(app, mouseX, mouseY)

def onKeyPress(app, key):
    if   key == '1': app.scene = dormScene
    elif key == '2': 
        resetQuiz(app)
        app.scene = quizScene
    elif key == '3':
        resetLecture(app)
        app.scene = lectureScene
    elif key == '4':
        resetGradescope(app)
        app.scene = gradescopeScene
    elif key == '5':
        resetBoss(app)
        app.scene = bossScene
    elif key == 'r': resetApp(app)

# RUN !!!!!!!!!!!!
runApp(width = width, height = height)
