
from pygame import *
from random import *
from math import*
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.colorchooser import askcolor
import os

init()
inf = display.Info()
w,h = inf.current_w,inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS'] = '40,100'
drawing = "PENCIL"
count = 0
#drawing 1 eraser, 0 pencil, 2 paintbrush
#note for next time make canvas2 a subsurface
colorwheel = image.load("coolimages/colorwheel.png") #loads image
eraser = image.load("coolimages/eraser.png")
paint = image.load("coolimages/paintbucket.png")
brush = image.load("coolimages/paintbrush.png")
undo = image.load("coolimages/undoarrow2.png")
redo = image.load("coolimages/redoarrow2.png")
avnegerlogo = image.load("coolimages/Avenger logo.png")
avengerscale = transform.scale(avnegerlogo, (100, 100))
brushscale = transform.scale(brush, (60, 60))
eraserscale = transform.scale(eraser, (60, 60))
undoscale = transform.scale(undo, (60, 60))
redoscale = transform.scale(redo, (60, 60))
pencil = image.load("coolimages/pencil.jpg")#pencil thumbnail
pencilscaled = transform.scale(pencil, (60, 60))
root = Tk()             # this initializes the Tk engine
root.withdraw()
morecolorchoice = Rect(80, 0, 72, 20)
screen = display.set_mode((1200, 800)) #creates main surface
canvas = screen.subsurface(25, 25, 700, 450)#creates canvas subsurface
canvasrect = Rect(25, 25, 700, 450) #S3et up collision points for options
pencilchoice = Rect(740, 25, 60, 60)#
rectchoice = Rect(820, 25, 30, 60)
filledrectchoice = Rect(850, 25, 30, 60)
circlechoice = Rect(820, 110, 30, 60)
filledcirclechoice = Rect(850, 110, 30, 60)
eraserchoice = Rect(740, 110, 60, 60)#
colorchoice = Rect(25, 525, 252, 233)#
brushchoice = Rect(740, 280, 60, 60)# opaque line
linechoice = Rect(740, 365, 60, 60)
savechoice = Rect(25, 0, 40, 20)
font.init()# initializes font
comicFont = font.Font("Marvel.ttf", 25) #Sets up font
smallcomicFont = font.Font("Marvel.ttf", 20)
undochoice = Rect(820, 195, 60, 60)
redochoice = Rect(740, 195, 60, 60)
color = [100, 100, 100]
textnotyetobliterated = 0
canvas.fill((255, 255, 255))
undolist = [canvas.copy(), 1, 2, 3, 4, 5, 6, 7, 8, 9,0,0,0,0,0,0,0,0,0,0] #allows the user to undo stuff
size = 2
screen.fill((255, 255, 255))
coolcolors = [100, 100, 100]
brushAlpha = Surface((800, 500)).convert()
brushAlpha.fill((255, 255, 255))
brushAlphazoom = Surface((2100, 1350)).convert()
brushAlpha.set_colorkey((255,255,255))
brushAlphazoom.fill((255, 255, 255))
brushAlphazoom.set_colorkey((255,255,255))
destroyeroftext =Surface((140, 20))
destroyeroftext.fill((255, 255, 255)) #Creates surface that will paste over text
dingdong = 0
pointferrect = [0]
colorchooser = Rect(820, 365, 60, 60)
pointtodraw = [0, 0] #sets where to draw a line from
copy = "randumsdnajsbdjab" # sets up the line drawing stuff
sick = False
countferline = 0 #Something related to line
countferrect = 0
texteraser = textpencil =  textundo = textbrush = 0
movement = [0, 0]
zoom = 0
counter = 0
zooms = False
temporaryimagecheck = 0
canvas2 = Surface((2100, 1350))
running = True
oncecanvas = True
once = True
while running:
    for evt in event.get(): 
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 4:
                size += 3
            if  evt.button == 5:
                size -= 3
            if zooms == False:
                pointtodraw = [mx, my]
                pointferellipse = (mx, my)
                pointferrect = [mx, my]
            if zooms:
                pointtodraw = [mx+(1050-canvas2rect.left), my+(675-canvas2rect.top)]
                pointferellipse = (mx+(1050-canvas2rect.left), my+(675-canvas2rect.top))
                pointferrect = [(mx+(1050-canvas2rect.left)), my+(675-canvas2rect.top)]
                print(pointferrect[0], pointferrect[1])
            copy = screen.copy()
            copycanvas2 = canvas2.copy()
            brushAlpha.fill((255, 255, 255))
            brushAlphazoom.fill((255, 255, 255))
            
                
            
        if evt.type == MOUSEBUTTONUP and canvasrect.collidepoint(mx, my):
            if evt.button != 4 and evt.button != 5:
                count += 1
##                    temporaryimagecheck += 1
##                    if temporaryimagecheck == 10:
##                        temporaryimagecheck -= 1
                if count == 20:
                    undolist[0] = undolist[1]
                    undolist[1] = undolist[2]
                    undolist[2] = undolist[3]
                    undolist[3] = undolist[4]
                    undolist[4] = undolist[5]
                    undolist[5] = undolist[6]
                    undolist[6] = undolist[7]
                    undolist[7] = undolist[8]
                    undolist[8] = undolist[9]
                    undolist[9] = undolist[10]
                    undolist[10] = undolist[1]
                    undolist[11] = undolist[12]
                    undolist[12] = undolist[13]
                    undolist[13] = undolist[14]
                    undolist[14] = undolist[15]
                    undolist[15] = undolist[16]
                    undolist[16] = undolist[17]
                    undolist[17] = undolist[18]
                    undolist[18] = undolist[19]
                    count -= 1
                if zooms:
                    undolist[count] = canvas2.copy()
                elif zooms == False:
                    undolist[count] = canvas.copy()
        if evt.type == MOUSEBUTTONUP:
            if savechoice.collidepoint(mx, my):
                #result = "hi.png"
                result = asksaveasfilename()
                if type(result) == str:
                    image.save(canvas, result)
            if morecolorchoice.collidepoint(mx, my):
                result = askcolor()
                color = result[0]
            
        if evt.type == MOUSEBUTTONDOWN and redochoice.collidepoint(mx, my):
## note undo is redo and vice versa since im unwilling to change variable names for change the rects
            if count > 0 and type(undolist[count-1]) != int :
                count -= 1
                if zooms:
                    pic = transform.scale(undolist[count], (2100, 1350))
                    canvas2.blit(pic, (0, 0))
                elif zooms == False:
                    pic = transform.scale(undolist[count], (700, 450))
                    canvas.blit(pic, (0, 0))
                if count == 0:
                    canvas.fill((255, 255, 255))
        if evt.type == MOUSEBUTTONDOWN and undochoice.collidepoint(mx, my):
            if count < 19 and type(undolist[count+1]) != int:
                count += 1
                if zooms:
                    pic = transform.scale(undolist[count], (2100, 1350))
                    canvas2.blit(pic, (0, 0))
                elif zooms == False:
                    pic = transform.scale(undolist[count], (700, 450))
                    canvas.blit(pic, (0, 0))
        if evt.type == KEYDOWN :
            if evt.key == K_UP and canvasrect.collidepoint(mx, my) and zooms:
                movement[1] += 20
            if evt.key == K_RIGHT and canvasrect.collidepoint(mx, my) and zooms:
                movement[0] += 20
            if evt.key == K_LEFT and canvasrect.collidepoint(mx, my) and zooms:
                movement[0] -= 20
            if evt.key == K_DOWN and canvasrect.collidepoint(mx, my) and zooms:
                movement[1] -= 20
            if evt.key == K_p and canvasrect.collidepoint(mx, my):
                if zooms == False:
                    canvas1 = transform.scale(canvas, (2100, 1350))
                    canvas2.blit(canvas1, (0, 0))
                    movement = [mx, my]
                zooms = True
            if evt.key == K_o and canvasrect.collidepoint(mx, my):
                zooms = False
                canvas1 = transform.scale(canvas2, (700, 450))
                canvas.blit(canvas1, (0, 0))
                
    
    if once:
        for x in range(0, 13):
            for y in range(0, 9):
                screen.blit(avengerscale, (0+(100*x), 0+(100*y)))
        if zooms:
            pic = transform.scale(undolist[count], (2100, 1350))
            canvas2.blit(pic, (0, 0))
            draw.rect(screen, (0, 0, 0), (canvasrect[0], canvasrect[1], 700, 450), 2)
        elif zooms == False:
            pic = transform.scale(undolist[count], (700, 450))
            
            canvas.blit(pic, (0, 0))
            draw.rect(screen, (0, 0, 0), (canvasrect[0], canvasrect[1], 700, 450), 2)
    once = False
    
    mx, my = mouse.get_pos()
    brushAlpha.set_alpha(150)
    brushAlphazoom.set_alpha(150)
    draw.circle(brushAlpha, (0, 0, 0, 255), (500, 500), 15)
    draw.circle(brushAlphazoom, (0, 0, 0, 255), (500, 500), 15)
    mb = mouse.get_pressed()
    canvas2rect = Rect((movement[0], movement[1], 2100, 1300))
    
##    for x in range(100):
##        draw.line(canvas2, (color), (25+25*x, 25), (25+25*x, 475), size)
    if pencilchoice.collidepoint(mx, my):
        textpencil = 1
        texts = "PENCIL"
        txtPic = comicFont.render(texts, True, (254, 227, 0), (255, 255, 255))
        screen.blit(txtPic, (740, 5))
    if eraserchoice.collidepoint(mx, my):
        texteraser = 1
        texts = "ERASER"
        txtPic = comicFont.render(texts, True, (254, 227, 0), (255, 255, 255))
        screen.blit(txtPic, (740, 90))
    if brushchoice.collidepoint(mx, my):
        textbrush = 1
        texts = "BRUSH"
        txtPic = comicFont.render(texts, True, (254, 227, 0), (255, 255, 255))
        screen.blit(txtPic, (740, brushchoice[1]-20))
    if redochoice.collidepoint(mx, my):
        textundo = 1
        texts = "UNDO"
        txtPic = comicFont.render(texts, True, (254, 227, 0), (255, 255, 255))
        screen.blit(txtPic, (740, redochoice[1]-20))
    if size < 0:
        size = 0
    if mb[0] == 1 and canvasrect.collidepoint(mx, my):
        screen.set_clip(canvasrect) #clips the canvas
        if drawing == "PENCIL":
            if zooms == False:
                draw.circle(canvas, (color), (mx-25, my-25), size)
                draw.line(canvas, (color), (mx-25, my-25), (oldmx-25, oldmy-25), size*2+1)
            if zooms:
                draw.circle(canvas2, (color), (mx+(1050-canvas2rect.left)-25, my+(675-canvas2rect.top)-25), size)
                draw.line(canvas2, (color), (mx+(1050-canvas2rect.left)-25, my+(675-canvas2rect.top)-25), (oldzoomsx, oldzoomsy), size*2+1)                
        if drawing  == "ERASER" and canvasrect.collidepoint(mx, my):#if mouse on canvas
            if zooms == False:
                draw.circle(canvas, (255, 255, 255), (mx-25, my-25), size)
                draw.line(canvas, (255, 255, 255), (oldmx-25, oldmy-25), (mx-25, my-25), (size*2))
            if zooms:
                draw.circle(canvas2, (255, 255, 255), (mx+(1050-canvas2rect.left)-25, my+(675-canvas2rect.top)-25), size)
                draw.line(canvas2, (255, 255, 255), (mx+(1050-canvas2rect.left)-25, my+(675-canvas2rect.top)-25), (oldzoomsx, oldzoomsy), size*2+1)
        if mb[0] == 1 and drawing == "BRUSH":#
            if zooms == False:
                linetodraw = hypot((mx-oldmx), (my- oldmy))#
                linetodraw = max(1, linetodraw)#
                sx = ((mx-oldmx)/ linetodraw)#
                sy = ((my-oldmy)/ linetodraw)#
                draw.circle(brushAlpha, (color), (mx, my), size)#
                for z in range(int(linetodraw)):#
                    sxdot = (sx*z)#
                    sydot = (sy*z)#
                    draw.circle(brushAlpha, (color), (int(oldmx + sxdot), int(oldmy + sydot)), size*2)
                screen.blit(copy,(0,0))#
                screen.blit(brushAlpha, (0, 0))#
            elif zooms:
                linetodraw = hypot((mx-oldmx), (my-oldmy))#
                linetodraw = max(1, linetodraw)#
                sx = ((mx-oldmx)/ linetodraw)#
                sy = (((my-oldmy)/ linetodraw))#
                draw.circle(brushAlphazoom, (color), (mx+(1050-canvas2rect.left)-25, my+(675-canvas2rect.top)-25), size)#
                for z in range(int(linetodraw)):#
                    sxdot = (sx*z)#
                    sydot = (sy*z)#
                    draw.circle(brushAlphazoom, (color), (int(oldzoomsx + sxdot), int(oldzoomsy + sydot)), size*2)
                canvas2.blit(copycanvas2,(0,0))#
                canvas2.blit(brushAlphazoom, (0, 0))#
        if mb[0] == 1 and drawing == "LINE":
            if zooms == False:
                screen.blit(copy,(0,0))#
                if size == 0:
                    size = 1
                draw.line(screen, (color), (mx, my), (pointtodraw[0], pointtodraw[1]), size)
            elif zooms:
                canvas2.blit(copycanvas2,(0,0))#
                if size == 0:
                    size = 1
                draw.line(canvas2, (color), (mx+(1050-canvas2rect.left)-25, my+(675-canvas2rect.top)-25), (pointtodraw[0]-25, pointtodraw[1]-25), size)
        if mb[0] == 1 and drawing == "RECTFILLED":
            if zooms == False:
                screen.blit(copy,(0,0))#
                changex = -1*(pointferrect[0]-mx)
                changey = -1*(pointferrect[1] - my)
                draw.rect(screen, (color), (pointferrect[0], pointferrect[1], changex, changey))
            if zooms:
                canvas2.blit(copycanvas2, (0, 0))
                changex = -1*(pointferrect[0]- (mx+(1050-canvas2rect.left)))
                changey = -1*(pointferrect[1] - (my+(675-canvas2rect.top)))
                draw.rect(canvas2, (color), (pointferrect[0]-25, pointferrect[1]-25, changex, changey))
        if mb[0] == 1 and drawing == "RECT":
            if zooms == False:
                if size == 0:
                    size = 1
                screen.blit(copy,(0,0))#
                changex = -1*(pointferrect[0]-mx)
                changey = -1*(pointferrect[1] - my)
                draw.rect(screen, (color), (pointferrect[0], pointferrect[1], changex, changey), size)
            if zooms:
                if size == 0:
                    size = 1
                canvas2.blit(copycanvas2, (0, 0))
                changex = -1*(pointferrect[0]- (mx+(1050-canvas2rect.left)))
                changey = -1*(pointferrect[1] - (my+(675-canvas2rect.top)))
                draw.rect(canvas2, (color), (pointferrect[0]-25, pointferrect[1]-25, changex, changey), size)
        if mb[0] == 1 and drawing == "ELLIPSEFILLED":
            if zooms == False:
                screen.blit(copy,(0,0))#
                changex = -1*(pointferellipse[0]-mx)
                changey = -1*(pointferellipse[1] - my)
                drawnstuffs = Rect(pointferellipse[0], pointferellipse[1], changex, changey)
                Rect.normalize(drawnstuffs)
                draw.ellipse(screen, (color), (drawnstuffs))
            if zooms:
                canvas2.blit(copycanvas2,(0,0))#
                changex = -1*(pointferellipse[0]- (mx+(1050-canvas2rect.left)))
                changey = -1*(pointferellipse[1] - (my+(675-canvas2rect.top)))
                drawnstuffs = Rect(pointferellipse[0]-25, pointferellipse[1]-25, changex, changey)
                Rect.normalize(drawnstuffs)
                draw.ellipse(canvas2, (color), (drawnstuffs))
        if mb[0] == 1 and drawing == "ELLIPSE":
            if zooms == False:
                screen.blit(copy,(0,0))#
                changex = -1*(pointferellipse[0]-mx)
                changey = -1*(pointferellipse[1] - my)
                drawnstuffs = Rect(pointferellipse[0], pointferellipse[1], changex, changey)
                Rect.normalize(drawnstuffs)
                if size > drawnstuffs.width/2 or size >drawnstuffs.height/2:
                    draw.ellipse(screen, (color), (drawnstuffs))
                else:
                    draw.ellipse(screen, (color), (drawnstuffs), size)
            if zooms:
                canvas2.blit(copycanvas2,(0,0))#
                changex = -1*(pointferellipse[0]- (mx+(1050-canvas2rect.left)))
                changey = -1*(pointferellipse[1] - (my+(675-canvas2rect.top)))
                drawnstuffs = Rect(pointferellipse[0]-25, pointferellipse[1]-25, changex, changey)
                Rect.normalize(drawnstuffs)
                if size > drawnstuffs.width/2 or size >drawnstuffs.height/2:
                    draw.ellipse(canvas2, (color), (drawnstuffs))
                else:
                    draw.ellipse(canvas2, (23, 85, 112), (drawnstuffs), size)
        if drawing == "COLORFILLED" and canvasrect.collidepoint((mx, my)):
            coolcolors = screen.get_at((mx, my))
            if mb[0] == 1:
                color = coolcolors
        screen.set_clip(None)#declips the canvas
    if mb[0] == 1 and pencilchoice.collidepoint(mx, my): #Gets pencil tool
        drawing = "PENCIL"
    elif mb[0] == 1 and eraserchoice.collidepoint(mx, my): #Gets the eraser tool
        drawing = "ERASER"
    elif mb[0] == 1 and brushchoice.collidepoint(mx, my):
        drawing = "BRUSH"
    elif mb[0] == 1 and colorchoice.collidepoint(mx, my): #Gets color
        coolcolors = screen.get_at((mx, my))
        color = coolcolors
    elif mb[0] == 1 and linechoice.collidepoint(mx, my):
        drawing = "LINE"
        linecopy = canvas.copy()
    elif mb[0] == 1 and rectchoice.collidepoint(mx, my):
        drawing = "RECT"
    elif mb[0] == 1 and filledrectchoice.collidepoint(mx, my):
        drawing = "RECTFILLED"
    elif mb[0] == 1 and circlechoice.collidepoint(mx, my):
        drawing = "ELLIPSE"
    elif mb[0] == 1 and filledcirclechoice.collidepoint(mx, my):
        drawing = "ELLIPSEFILLED"
    elif mb[0] == 1 and colorchooser.collidepoint(mx, my):
        drawing = "COLORFILLED"
    
    
    
    oldmx = mx
    oldmy =  my
    oldzoomsx = mx+(1050-canvas2rect.left)-25
    oldzoomsy = my+(675-canvas2rect.top)-25
    opacityline= hypot((mx - oldmx), (my-oldmy))
    
    screen.blit((smallcomicFont.render("SAVE", True, (132, 132, 255), (255, 255, 255))), (25, 0))
    screen.blit((smallcomicFont.render("MORE COLOURS", True, (132, 132, 255), (255, 255, 255))), (morecolorchoice))
    
    print(canvas2rect.left)
    draw.rect(screen, (0, 0, 0), (830, 35, 40, 40))
    draw.rect(screen, (255, 255, 255), (833, 38, 17, 35))
    draw.circle(screen, (0, 0, 0), (850, 140), 25)
    draw.circle(screen, (0, 0, 0), (850, 140), 25, 1)
    screen.blit(colorwheel, (25, 525))
    screen.blit(pencilscaled, (pencilchoice))
    screen.blit(eraserscale, (eraserchoice))
    screen.blit(brushscale, (brushchoice))
    screen.blit(redoscale, (undochoice))
    screen.blit(undoscale, (redochoice))
    if zooms:
        canvas.blit(canvas2, (movement[0]-1050, movement[1]-675))
    draw.line(screen, (0, 0, 0), (750, 375), (790, 415), 2)
    for x in range(700, 781, 80):
        for y in range(25, 430, 85):
            draw.rect(screen, (0,0,0), (x+40, y, 60, 60), 2)
    if textpencil == 1 and pencilchoice.collidepoint(mx, my) == False:
        once = True
        textpencil = 0
    if texteraser == 1 and eraserchoice.collidepoint(mx, my) == False:
        once = True
        texteraser = 0
    if textbrush == 1 and brushchoice.collidepoint(mx, my) == False:
        once = True
        textbrush = 0
    if textundo == 1 and redochoice.collidepoint(mx, my) == False:
        once = True
        textundo = 0
    draw.rect(screen, (coolcolors), (273, 525, 20, 233))
##    if temporaryimagecheck > 0:
##        for z in range(temporaryimagecheck):
##            tempstuff = undolist[z]
##            tempstuffed = transform.scale(tempstuff, (210, 135))
##            screen.blit(tempstuffed, (910, (25+(z*60))))
    #print(count)
    display.flip()
    
quit()
