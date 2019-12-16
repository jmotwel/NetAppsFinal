import pygame
pygame.init()
import pika
import json
import sys
# Rabbitmq setup
ip=''
if(len(sys.argv)==2):
    ip = str(sys.argv[1])
else:
    print('wrong inputs')
credentials = pika.PlainCredentials('repo-pi','netapps')
connection = pika.BlockingConnection(pika.ConnectionParameters(ip,
                                                               5672,
                                                               '/',
                                                               credentials));
channel = connection.channel()
channel.exchange_declare(exchange='Pokemon',
                         exchange_type='direct',
                         durable=False)


#while (1):
#    curVal = channel.basic_get(queue='Score', auto_ack=True)
#    if curVal != (None, None, None):
#        dataForTori = curVal[2]
#        print(dataForTori.decode("utf-8"))
font=pygame.font.Font('freesansbold.ttf',32)
text = font.render('Leaderboard', True, (0,0,0),(255,255,255))
textRect=text.get_rect()
textRect.center=(500,20)

font1=pygame.font.Font('freesansbold.ttf',32)
text1 = font1.render('First Place', True, (0,0,0),(255,255,255))
textRect1=text1.get_rect()
textRect1.center=(85,150)

font2=pygame.font.Font('freesansbold.ttf',32)
text2 = font2.render('Second Place', True, (0,0,0),(255,255,255))
textRect2=text2.get_rect()
textRect2.center=(105,250)

font3=pygame.font.Font('freesansbold.ttf',32)
text3 = font3.render('Third Place', True, (0,0,0),(255,255,255))
textRect3=text3.get_rect()
textRect3.center=(90,350)

font10=pygame.font.Font('freesansbold.ttf',20)
text10 = font10.render('Score', True, (0,0,0),(255,255,255))
textRect10=text10.get_rect()
textRect10.center=(285,100)

font4=pygame.font.Font('freesansbold.ttf',20)
text4 = font4.render('Pokemon 1', True, (0,0,0),(255,255,255))
textRect4=text4.get_rect()
textRect4.center=(385,100)

font5=pygame.font.Font('freesansbold.ttf',20)
text5 = font5.render('Pokemon 2', True, (0,0,0),(255,255,255))
textRect5=text5.get_rect()
textRect5.center=(500,100)

font6=pygame.font.Font('freesansbold.ttf',20)
text6 = font6.render('Pokemon 3', True, (0,0,0),(255,255,255))
textRect6=text6.get_rect()
textRect6.center=(615,100)

font7=pygame.font.Font('freesansbold.ttf',20)
text7 = font7.render('Pokemon 4', True, (0,0,0),(255,255,255))
textRect7=text7.get_rect()
textRect7.center=(730,100)

font8=pygame.font.Font('freesansbold.ttf',20)
text8 = font8.render('Pokemon 5', True, (0,0,0),(255,255,255))
textRect8=text8.get_rect()
textRect8.center=(845,100)

font9=pygame.font.Font('freesansbold.ttf',20)
text9 = font9.render('Pokemon 6', True, (0,0,0),(255,255,255))
textRect9=text9.get_rect()
textRect9.center=(960,100)


display_width=1025
display_height=800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Leaderboard')

black=(0,0,0)
white=(255,255,255)

clock=pygame.time.Clock()
def firstplace(score,im1, im2, im3, im4, im5, im6):
    font11=pygame.font.Font('freesansbold.ttf',20)
    text11 = font11.render(score, True, (0,0,0),(255,255,255))
    textRect11=text11.get_rect()
    textRect11.center=(285,185)
    gameDisplay.blit(text11,textRect11)
    imag1=pygame.image.load(im1)
    gameDisplay.blit(pygame.transform.scale(imag1,(125,125)), (330,100))
    imag2=pygame.image.load(im2)
    gameDisplay.blit(pygame.transform.scale(imag2,(125,125)), (430,100))
    imag3=pygame.image.load(im3)
    gameDisplay.blit(pygame.transform.scale(imag3,(125,125)), (550,100))
    imag4=pygame.image.load(im4)
    gameDisplay.blit(pygame.transform.scale(imag4,(125,125)), (670,100))
    imag5=pygame.image.load(im5)
    gameDisplay.blit(pygame.transform.scale(imag5,(125,125)), (790,100))
    imag6=pygame.image.load(im6)
    gameDisplay.blit(pygame.transform.scale(imag6,(125,125)), (910,100))
    
    
    
    
def secondplace(score,im1, im2, im3, im4, im5, im6):
    font12=pygame.font.Font('freesansbold.ttf',20)
    text12 = font12.render(score, True, (0,0,0),(255,255,255))
    textRect12=text12.get_rect()
    textRect12.center=(285,285)
    gameDisplay.blit(text12,textRect12)
    imag1=pygame.image.load(im1)
    gameDisplay.blit(pygame.transform.scale(imag1,(125,125)), (330,200))
    imag2=pygame.image.load(im2)
    gameDisplay.blit(pygame.transform.scale(imag2,(125,125)), (430,200))
    imag3=pygame.image.load(im3)
    gameDisplay.blit(pygame.transform.scale(imag3,(125,125)), (550,200))
    imag4=pygame.image.load(im4)
    gameDisplay.blit(pygame.transform.scale(imag4,(125,125)), (670,200))
    imag5=pygame.image.load(im5)
    gameDisplay.blit(pygame.transform.scale(imag5,(125,125)), (790,200))
    imag6=pygame.image.load(im6)
    gameDisplay.blit(pygame.transform.scale(imag6,(125,125)), (910,200))
    
    
def thirdplace(score,im1, im2, im3, im4, im5, im6):
    font14=pygame.font.Font('freesansbold.ttf',20)
    text14 = font14.render(score, True, (0,0,0),(255,255,255))
    textRect14=text14.get_rect()
    textRect14.center=(285,385)
    gameDisplay.blit(text14,textRect14)
    imag1=pygame.image.load(im1)
    gameDisplay.blit(pygame.transform.scale(imag1,(125,125)), (330,300))
    imag2=pygame.image.load(im2)
    gameDisplay.blit(pygame.transform.scale(imag2,(125,125)), (430,300))
    imag3=pygame.image.load(im3)
    gameDisplay.blit(pygame.transform.scale(imag3,(125,125)), (550,300))
    imag4=pygame.image.load(im4)
    gameDisplay.blit(pygame.transform.scale(imag4,(125,125)), (670,300))
    imag5=pygame.image.load(im5)
    gameDisplay.blit(pygame.transform.scale(imag5,(125,125)), (790,300))
    imag6=pygame.image.load(im6)
    gameDisplay.blit(pygame.transform.scale(imag6,(125,125)), (910,300))
    
    
no=1
score=0
score1=0
score2=0
score3=0
pok11='1.png'
pok12='1.png'
pok13='1.png'
pok14='1.png'
pok15='1.png'
pok16='1.png'
pok21='1.png'
pok22='1.png'
pok23='1.png'
pok24='1.png'
pok25='1.png'
pok26='1.png'
pok31='1.png'
pok32='1.png'
pok33='1.png'
pok34='1.png'
pok35='1.png'
pok36='1.png'
num=0
dataForTori=''
while (1):
    gameDisplay.fill(white)
    gameDisplay.blit(text,textRect)
    gameDisplay.blit(text1,textRect1)
    gameDisplay.blit(text2,textRect2)
    gameDisplay.blit(text3,textRect3)
    gameDisplay.blit(text4,textRect4)
    gameDisplay.blit(text5,textRect5)
    gameDisplay.blit(text6,textRect6)
    gameDisplay.blit(text7,textRect7)
    gameDisplay.blit(text8,textRect8)
    gameDisplay.blit(text9,textRect9)
    gameDisplay.blit(text10,textRect10)
    pygame.draw.line(gameDisplay, (0,0,0), (0,50),(1025,50),3)
    pygame.draw.line(gameDisplay, (0,0,0), (0,120),(1025,120),3)
    pygame.draw.line(gameDisplay, (0,0,0), (250,50),(250,800),3)
    pygame.draw.line(gameDisplay, (0,0,0), (0,200),(1025,200),3)
    pygame.draw.line(gameDisplay, (0,0,0), (0,300),(1025,300),3)
    pygame.draw.line(gameDisplay, (0,0,0), (0,400),(1025,400),3)
    
    curVal = channel.basic_get(queue='Score', auto_ack=True)
    if curVal != (None, None, None):
        dataForTori = curVal[2]
        num=0
        json1=json.loads(dataForTori.decode("utf-8"))
        score=json1['total']
        if(json1['pokemon1']['score']>5000):
            pok1='./shiny/' + str(json1['pokemon1']['id'])+'.png'
        else:
            pok1=str(json1['pokemon1']['id'])+'.png'
        if(json1['pokemon2']['score']>5000):
            pok2='./shiny/' + str(json1['pokemon2']['id'])+'.png'
        else:
            pok2=str(json1['pokemon2']['id'])+'.png'
        if(json1['pokemon3']['score']>5000):
            pok3='./shiny/' + str(json1['pokemon3']['id'])+'.png'
        else:
            pok3=str(json1['pokemon3']['id'])+'.png'
        if(json1['pokemon4']['score']>5000):
            pok4='./shiny/' + str(json1['pokemon4']['id'])+'.png'
        else:
            pok4=str(json1['pokemon4']['id'])+'.png'
        if(json1['pokemon5']['score']>5000):
            pok5='./shiny/' + str(json1['pokemon5']['id'])+'.png'
        else:
            pok5=str(json1['pokemon5']['id'])+'.png'
        if(json1['pokemon6']['score']>5000):
            pok6='./shiny/' + str(json1['pokemon6']['id'])+'.png'
        else:
            pok6=str(json1['pokemon6']['id'])+'.png'
    if((score>score1)and(num==0)):
        score3=score2
        pok31=pok21
        pok32=pok22
        pok33=pok23
        pok34=pok24
        pok35=pok25
        pok36=pok26
        score2=score1
        pok21=pok11
        pok22=pok12
        pok23=pok13
        pok24=pok14
        pok25=pok15
        pok26=pok16
        score1=score
        pok11=pok1
        pok12=pok2
        pok13=pok3
        pok14=pok4
        pok15=pok5
        pok16=pok6
        num=1
    elif((score>score2)and(num==0)):
        score3=score2
        pok31=pok21
        pok32=pok22
        pok33=pok23
        pok34=pok24
        pok35=pok25
        pok36=pok26
        score2=score
        pok21=pok1
        pok22=pok2
        pok23=pok3
        pok24=pok4
        pok25=pok5
        pok26=pok6
        num=1
    elif((score>score3)and(num==0)):
        score3=score
        pok31=pok1
        pok32=pok2
        pok33=pok3
        pok34=pok4
        pok35=pok5
        pok36=pok6
        num=1
    
    firstplace(str(score1),pok11,pok12,pok13,pok14,pok15,pok16)
    secondplace(str(score2),pok21,pok22,pok23,pok24,pok25,pok26)
    thirdplace(str(score3),pok31,pok32,pok33,pok34,pok35,pok36)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()