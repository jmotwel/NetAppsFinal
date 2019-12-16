import pygame
pygame.init()
import pika
import json
import sys
ip=''
if(len(sys.argv)==2):
    ip = str(sys.argv[1])
else:
    print('wrong inputs')
# Rabbitmq setup
credentials = pika.PlainCredentials('repo-pi','netapps')
connection = pika.BlockingConnection(pika.ConnectionParameters(ip,
                                                               5672,
                                                               '/',
                                                               credentials));
channel = connection.channel()

channel.exchange_declare(exchange='Pokemon',
                         exchange_type='direct',
                         durable=False)

display_width=1000
display_height=700

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Recent Pokemon')

black=(0,0,0)
white=(255,255,255)

clock=pygame.time.Clock()
imag=pygame.image.load('15.png')
num=1
name1='1.png'
def im(name):
    imag=pygame.image.load(name)
    gameDisplay.blit(pygame.transform.scale(imag,(800,800)), (100,-100))
    pygame.display.update()
    
dataForTori=''
while (1):
    gameDisplay.fill(white)
    curVal = channel.basic_get(queue='ID', auto_ack=True)
    if curVal != (None, None, None):
        dataForTori = curVal[2]
        json1=json.loads(dataForTori.decode("utf-8"))
        if(json1['score']>5000):
            name1='./shiny/' + str(json1['id'])+'.png'
        else:
            name1=str(json1['id'])+'.png'
    im(name1)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()