import pygame, random, time
from pygame.locals import *

LARGURA=692
ALTURA=600
TAMANHO_DO_DOG=110
ALTURA_DO_DOG=110
X=400
Y=400
SPEED=10
V=460
Z=230
n=0
oo=0
oo1=1
TAMANHO_DO_icone_musica1=205
altura_DO_icone_musica1=205
vetor=400
a=-600
b=-600
aa=-600
bb=-600
aaa=-600
bbb=-600
c=-600
d=-600
ff=2
fm=[]
lm=2
f1=[]
j=0
volte=False
na=0
jo=4
ll=5000
jj=1
deu=0
tomada=False
jj1=1
cm=0
lk=20
tio=-600
tia=-600
resultado1=0
gaga=4
resposta=""
trocs1=390
trocs2=90
abrir=10
aaaa=-600
bbbb=-600
sorte=0
meleca=False
tn=4
ok=False
tn1=0
alfaA=-600
betaA=350
alfaG=-600
betaG=350
betaA2=350
alfaA2=-600
betaU=350
alfaU=-600
betaH=350
alfaH=-600
betaN=350
alfaN=-600
betaI=350
alfaI=-600
betaI2=350
alfaI2=-600
betaL=350
alfaL=-600
betaP=350
alfaP=-600
betaO=350
alfaO=-600
betaR=350
alfaR=-600
betaR2=350
alfaR2=-600
betaC=350
alfaC=-600
betaC2=350
alfaC2=-600
betaO2=350
alfaO2=-600
betaL=350
alfaL=-600
betaT=350
alfaT=-600
betaM=350
alfaM=-600
betaB=350
alfaB=-600
alfaE=-600
betaE=350
guta=0
fed=21
cena=0
kei=0
lixta=""
letra1=""
letra2="" 
letra3=""
letra4=""
letra5=""
letra6=""
letra7=""
letra8=""
confere1=-600
confere2=-600
errado1=-600
errado2=-600
epa=False
alfapor=-600
betapor=-600
kal=-1
qek=True
alfamate=-600
betamate=-600
ulti=-1
tim=3
class balão(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        

        self.images = [pygame.image.load('cliqueesquedo.png').convert_alpha(),
                       pygame.image.load('oimeunome.png').convert_alpha(),
                       pygame.image.load('Escolher.png').convert_alpha()]
        self.current_image = 0
        self.speed = SPEED

        self.image = pygame.image.load('cliqueesquedo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.mask = pygame.mask.from_surface(self.image)

        

        self.rect = self.image.get_rect()
        self.rect[0] = V
        self.rect[1] = Z
    def tirar (self):
        self.rect[0] = -600
        self.rect[1] = -600
    def adicionar(self):
        self.image = self.images[n+1]
        self.image = pygame.transform.scale(self.image, (200, 200))      
class acertou(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        

        self.images = [pygame.image.load('acertou.png').convert_alpha(),
                       pygame.image.load('errou.png').convert_alpha(),
                       pygame.image.load('clique.png').convert_alpha(),
                       pygame.image.load('primeiro.png').convert_alpha(),
                       pygame.image.load('segundo.png').convert_alpha(),
                       pygame.image.load('terceiro.png').convert_alpha(),
                       pygame.image.load('quarto.png').convert_alpha(),
                       pygame.image.load('quinto.png').convert_alpha(),
                       pygame.image.load('explicação1.png').convert_alpha(),
                       pygame.image.load('memorize.png').convert_alpha(),
                       pygame.image.load('espaço.png').convert_alpha()]
                       
        self.current_image = 0
        self.speed = SPEED

        self.image = pygame.image.load('acertou.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.mask = pygame.mask.from_surface(self.image)

        

        self.rect = self.image.get_rect()
        self.rect[0] = 500
        self.rect[1] = 250
    def tirar (self):
        self.rect[0] = -600
        self.rect[1] = -600  
    def adicionar(self): 
        self.image = self.images[na+1]
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect[0] = 500
        self.rect[1] = 250       
class dançando(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [pygame.image.load('frame-1.gif').convert_alpha(),
                       pygame.image.load('frame-2.gif').convert_alpha(),
                       pygame.image.load('frame-3.gif').convert_alpha(),
                       pygame.image.load('frame-4.gif').convert_alpha(),
                       pygame.image.load('frame-5.gif').convert_alpha()]

        self.speed = SPEED

        self.current_image = 0

        self.image = pygame.image.load('frame-1.gif').convert_alpha()
        self.image = pygame.transform.scale(self.image, (TAMANHO_DO_DOG, ALTURA_DO_DOG))

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = -600
        self.rect[1] = -600

    def update(self):
        self.current_image = (self.current_image + 1) % 3
        self.image = self.images[ self.current_image ]
        self.image = pygame.transform.scale(self.image, (TAMANHO_DO_DOG, ALTURA_DO_DOG))
    def trocaa(self):
        self.rect[0] = 475
        self.rect[1] = 450
    def tirar(self):
        self.rect[0] = -600
        self.rect[1] = -600                         
class vetorazul(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      

        self.image = pygame.image.load('azul.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = 65
    def aumentar(self):
        self.image = pygame.image.load('azul.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = 65 
    def diminuir(self):
        self.image = pygame.image.load('azul.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect[0] = 180
        self.rect[1] = 120       
class vetorrosa(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      

        self.image = pygame.image.load('corRosa.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 30
    def aumentar(self):
        self.image = pygame.image.load('corRosa.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 30   
    def diminuir(self):
        self.image = pygame.image.load('corRosa.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect[0] = 70
        self.rect[1] = 45          
class vetormarinho(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      

        self.image = pygame.image.load('botoes cores.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = 30
    def aumentar(self):
        self.image = pygame.image.load('botoes cores.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = 30 
    def diminuir(self):
        self.image = pygame.image.load('botoes cores.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect[0] = 180
        self.rect[1] = 50    
class vetorvermelho(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      

        self.image = pygame.image.load('corvermelho.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 65
    def aumentar(self):
        self.image = pygame.image.load('corvermelho.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 65
    def diminuir(self):
        self.image = pygame.image.load('corvermelho.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect[0] = 80
        self.rect[1] = 120                      
class vetorlaranja(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      

        self.image = pygame.image.load('vetorlaranja.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 100
    def aumentar(self):
        self.image = pygame.image.load('vetorlaranja.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 100
    def diminuir(self):
        self.image = pygame.image.load('vetorlaranja.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect[0] = 80
        self.rect[1] = 200
class vetoramarelo(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      

        self.image = pygame.image.load('vetoramarelo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 135
    def aumentar(self):
        self.image = pygame.image.load('vetoramarelo.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = 135
    def diminuir(self):
        self.image = pygame.image.load('vetoramarelo.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect[0] = 80
        self.rect[1] = 280
class vetorroxo(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      

        self.image = pygame.image.load('vetorroxo.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = 100
    def aumentar(self):
        self.image = pygame.image.load('vetorroxo.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = 100 
    def diminuir(self):
        self.image = pygame.image.load('vetorroxo.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect[0] = 180
        self.rect[1] = 200
class vetormarrom(pygame.sprite.Sprite):    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
      

        self.image = pygame.image.load('vetormarrom.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = 135
    def aumentar(self):
        self.image = pygame.image.load('vetormarrom.png')
        self.image = pygame.transform.scale(self.image, (vetor, vetor))
        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = 135 
    def diminuir(self):
        self.image = pygame.image.load('vetormarrom.png')
        self.image = pygame.transform.scale(self.image, (300, 200))
        self.rect = self.image.get_rect()
        self.rect[0] = 180
        self.rect[1] = 280    
class numeros(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        

        self.images = [pygame.image.load('numerozero.png').convert_alpha(),
                       pygame.image.load('numero01 (1).png').convert_alpha(),
                       pygame.image.load('numero2 (1).png').convert_alpha(),
                       pygame.image.load('numero3 (1).png').convert_alpha(),
                       pygame.image.load('numero4 (1).png').convert_alpha(),
                       pygame.image.load('numero5 (1).png').convert_alpha(),
                       pygame.image.load('numero6 (1).png').convert_alpha(),
                       pygame.image.load('numero7 (1).png').convert_alpha(),
                       pygame.image.load('numero8 (1).png').convert_alpha(),
                       pygame.image.load('numero9 (1).png').convert_alpha(),
                       pygame.image.load('branco.jpg').convert_alpha()]
        self.current_image = 0
        self.speed = SPEED

        self.image = pygame.image.load('numero01.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.mask = pygame.mask.from_surface(self.image)

        

        self.rect = self.image.get_rect()
        self.rect[0] = -600
        self.rect[1] = -600
    def tirar (self):
        self.rect[0] = -600
        self.rect[1] = -600
    def adicionar(self):
        self.image = self.images[nt1]
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect[0] = 190
        self.rect[1] = 90
class sinal(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        

        self.images = [pygame.image.load('soma.png').convert_alpha(),
                       pygame.image.load('diminuir.png').convert_alpha(),
                       pygame.image.load('vezes.png').convert_alpha(),
                       pygame.image.load('branco.jpg').convert_alpha()]
        self.current_image = 0
        self.speed = SPEED

        self.image = pygame.image.load('soma.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.mask = pygame.mask.from_surface(self.image)

        

        self.rect = self.image.get_rect()
        self.rect[0] = -600
        self.rect[1] = -600
    def tirar (self):
        self.rect[0] = -600
        self.rect[1] = -600
    def adicionar(self):
        self.image = self.images[nt3]
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect[0] = 310
        self.rect[1] = 124
class numeros1(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        

        self.images = [pygame.image.load('numerozero.png').convert_alpha(),
                       pygame.image.load('numero01 (1).png').convert_alpha(),
                       pygame.image.load('numero2 (1).png').convert_alpha(),
                       pygame.image.load('numero3 (1).png').convert_alpha(),
                       pygame.image.load('numero4 (1).png').convert_alpha(),
                       pygame.image.load('numero5 (1).png').convert_alpha(),
                       pygame.image.load('numero6 (1).png').convert_alpha(),
                       pygame.image.load('numero7 (1).png').convert_alpha(),
                       pygame.image.load('numero8 (1).png').convert_alpha(),
                       pygame.image.load('numero9 (1).png').convert_alpha(),
                       pygame.image.load('branco.jpg').convert_alpha()]
        self.current_image = 0
        self.speed = SPEED

        self.image = pygame.image.load('numero2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.mask = pygame.mask.from_surface(self.image)

        

        self.rect = self.image.get_rect()
        self.rect[0] = -600
        self.rect[1] = -600
    def tirar (self):
        self.rect[0] = -600
        self.rect[1] = -600
    def adicionar(self, trocs1, trocs2):
        self.image = self.images[nt2]
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect[0] = trocs1
        self.rect[1] = trocs2

    

pygame.init()
screen=pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Aprenda com Ozzy')

BACKGROUND=pygame.image.load("primeiraimagem(2) (1).jpg")
BACKGROUND=pygame.transform.scale(BACKGROUND, (LARGURA, ALTURA))
calculadora=pygame.image.load("calculadora.png")
calculadora=pygame.transform.scale(calculadora, (325, 325))
iconemusica=pygame.image.load("musicaicone (1).png")
iconemusica=pygame.transform.scale(iconemusica, (TAMANHO_DO_icone_musica1, altura_DO_icone_musica1))
iconepor=pygame.image.load("livro_icon2.png")
iconepor=pygame.transform.scale(iconepor, (170, 170))
rect=iconemusica.get_rect()
OZZY=pygame.image.load("cachorro_dançando.gif")
OZZY=pygame.transform.scale(OZZY, (TAMANHO_DO_DOG, ALTURA_DO_DOG))
iconematematica=pygame.image.load("Vetormatematica.png")
iconematematica=pygame.transform.scale(iconematematica, (170, 170))
animal=pygame.image.load("galinha.png")
animal=pygame.transform.scale(animal, (170, 170))
letraA=pygame.image.load("letrasA.png")
letraA=pygame.transform.scale(letraA, (50, 50))
letraA2=pygame.image.load("letrasA.png")
letraA2=pygame.transform.scale(letraA2, (50, 50))
letraG=pygame.image.load("letrasG.png")
letraG=pygame.transform.scale(letraG, (50, 50))
letraL=pygame.image.load("letrasL.png")
letraL=pygame.transform.scale(letraL, (50, 50))
letraI=pygame.image.load("letrasI.png")
letraI=pygame.transform.scale(letraI, (50, 50))
letraI2=pygame.image.load("letrasI.png")
letraI2=pygame.transform.scale(letraI2, (50, 50))
letraN=pygame.image.load("letrasN.png")
letraN=pygame.transform.scale(letraN, (50, 50))
letraH=pygame.image.load("letrasH.png")
letraH=pygame.transform.scale(letraH, (50, 50))
letraU=pygame.image.load("letrasU.png")
letraU=pygame.transform.scale(letraU, (50, 50))
letraP=pygame.image.load("letrasP.png")
letraP=pygame.transform.scale(letraP, (50, 50))
letraO=pygame.image.load("letrasO.png")
letraO=pygame.transform.scale(letraO, (50, 50))
letraR=pygame.image.load("letrasR.png")
letraR=pygame.transform.scale(letraR, (50, 50))
letraR2=pygame.image.load("letrasR.png")
letraR2=pygame.transform.scale(letraR2, (50, 50))
letraC=pygame.image.load("letrasC.png")
letraC=pygame.transform.scale(letraC, (50, 50))
letraC2=pygame.image.load("letrasC.png")
letraC2=pygame.transform.scale(letraC2, (50, 50))
letraO2=pygame.image.load("letrasO.png")
letraO2=pygame.transform.scale(letraO2, (50, 50))
letraT=pygame.image.load("letrasT.png")
letraT=pygame.transform.scale(letraT, (50, 50))
letraM=pygame.image.load("letrasM.png")
letraM=pygame.transform.scale(letraM, (50, 50))
letraB=pygame.image.load("letrasB.png")
letraB=pygame.transform.scale(letraB, (50, 50))
letraE=pygame.image.load("letrasE.png")
letraE=pygame.transform.scale(letraE, (50, 50))
confere=pygame.image.load("acertoumatematica.png")
confere=pygame.transform.scale(confere, (200, 200))
errado=pygame.image.load("erroumatematica.png")
errado=pygame.transform.scale(errado, (200, 200))
balãopor=pygame.image.load("portugues1.png")
balãopor=pygame.transform.scale(balãopor, (200, 200))
balãomate=pygame.image.load("matematica1.png")
balãomate=pygame.transform.scale(balãomate, (200, 200))

audio1=pygame.mixer.Sound("audio1.mp3")
audio2=pygame.mixer.Sound("audio2.wav")
audio3=pygame.mixer.Sound("audio3.wav")
audio4=pygame.mixer.Sound("audio4ok.wav")
audio5=pygame.mixer.Sound("audio5.wav")
audio6=pygame.mixer.Sound("audio6.wav")
audio7=pygame.mixer.Sound("audio7.wav")
audio8=pygame.mixer.Sound("audio8.flac")
louse=iconematematica.get_rect()
mousepocição=pygame.mouse.get_pos()
balão_group = pygame.sprite.Group()
balão = balão()
balão_group.add(balão)
 
dançando_group = pygame.sprite.Group()
dançando = dançando()
dançando_group.add(dançando)

vetorrosa_group = pygame.sprite.Group()
vetorrosa = vetorrosa()
vetorrosa_group.add(vetorrosa)

vetormarinho_group = pygame.sprite.Group()
vetormarinho = vetormarinho()
vetormarinho_group.add(vetormarinho)

vetorvermelho_group = pygame.sprite.Group()
vetorvermelho = vetorvermelho()
vetorvermelho_group.add(vetorvermelho)

vetorazul_group = pygame.sprite.Group()
vetorazul = vetorazul()
vetorazul_group.add(vetorazul)

vetorlaranja_group = pygame.sprite.Group()
vetorlaranja = vetorlaranja()
vetorlaranja_group.add(vetorlaranja)

vetoramarelo_group = pygame.sprite.Group()
vetoramarelo = vetoramarelo()
vetoramarelo_group.add(vetoramarelo)

vetorroxo_group = pygame.sprite.Group()
vetorroxo = vetorroxo()
vetorroxo_group.add(vetorroxo)

vetormarrom_group = pygame.sprite.Group()
vetormarrom = vetormarrom()
vetormarrom_group.add(vetormarrom)

acertou_group = pygame.sprite.Group()
acertou = acertou()
acertou_group.add(acertou)

numeros_group = pygame.sprite.Group()
numeros = numeros()
numeros_group.add(numeros)

numeros1_group = pygame.sprite.Group()
numeros1 = numeros1()
numeros1_group.add(numeros1)

sinal_group = pygame.sprite.Group()
sinal = sinal()
sinal_group.add(sinal)






Clock= pygame.time.Clock()
while True:
    mouse=pygame.mouse.get_pos()
    Clock.tick(8)
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
    if event.type==pygame.MOUSEBUTTONDOWN and oo<2:
        balão.adicionar()
        n=n+1
        oo=oo+1
        oo1=oo1+1
    #if event.type==pygame.MOUSEBUTTONDOWN and 477<mouse[0]<554 and 450<mouse[1]<576
#===================================================================================menus==================================================#
    elif event.type==pygame.MOUSEBUTTONDOWN and oo1==3 or event.type==pygame.MOUSEBUTTONDOWN and 477<mouse[0]<554 and 450<mouse[1]<576 and oo1>=2:
        balão.tirar()
        numeros.tirar()
        numeros1.tirar()
        sinal.tirar()
        acertou.tirar() 
        BACKGROUND=pygame.image.load("back_final menugame - Cópia.png")
        BACKGROUND=pygame.transform.scale(BACKGROUND, (LARGURA, ALTURA))
        X=-400
        Y=-400
        oo=oo+500
        a=50
        b=45
        aa=450
        bb=60
        aaa=70
        bbb=370
        oo1=oo1+500
        ff=0
        dançando.trocaa()
        tio=-600
        tia=-600
        errado1=-600
        errado2=-600
        confere2=-600
        confere1=-600
        lk=20
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        aaaa=-600
        bbbb=-600
        epa=False
        jo=4
        cena=0
        guta=9
        qek=True
        alfapor=-600
        betapor=-600
        kal=-1
        balãopor=pygame.image.load("portugues1.png")
        balãopor=pygame.transform.scale(balãopor, (200, 200))
        ulti=-1
        alfamate=-600
        betamate=-600
        balãomate=pygame.image.load("matematica1.png")
        balãomate=pygame.transform.scale(balãomate, (200, 200))
        fm=[]
        betaB=350
        alfaB=-600
        alfaE=-600
        betaE=350
    if pygame.mouse.get_pressed()[0]:
        if rect.collidepoint(pygame.mouse.get_pos()) and ff==0:
            a=-600
            b=-600
            aa=-600
            bb=-600
            aaa=-600
            bbb=-600
            BACKGROUND=pygame.image.load("Fundomusica.jpeg")
            BACKGROUND=pygame.transform.scale(BACKGROUND, (LARGURA, ALTURA))
            vetorrosa_group.update()
            vetorrosa_group.draw(BACKGROUND)
            vetormarinho_group.update()
            vetormarinho_group.draw(BACKGROUND)
            vetorvermelho_group.update()
            vetorvermelho_group.draw(BACKGROUND)
            vetorazul_group.update()
            vetorazul_group.draw(BACKGROUND)
            vetorlaranja_group.update()
            vetorlaranja_group.draw(BACKGROUND)
            vetoramarelo_group.update()
            vetoramarelo_group.draw(BACKGROUND)
            vetorroxo_group.update()
            vetorroxo_group.draw(BACKGROUND)
            vetormarrom_group.update()
            vetormarrom_group.draw(BACKGROUND)
            ff=ff+1
            print("boa")
            jo=0
            na=6
    if event.type==pygame.MOUSEBUTTONDOWN and jo<3:
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        jo=jo+1
        volte=True
        print("aaa")
        print("jo")
    if event.type==pygame.MOUSEBUTTONDOWN and 445<mouse[0]<615 and 62<mouse[1]<225 and ff==0 or lk==10 and event.type==pygame.MOUSEBUTTONDOWN :
        print("deu certo")
        ff=ff+1
        BACKGROUND=pygame.image.load("fundomate.jpg")
        BACKGROUND=pygame.transform.scale(BACKGROUND, (LARGURA, ALTURA))
        a=-600
        b=-600
        aa=-600
        bb=-600
        aaa=-600
        bbb=-600
        lk=10
        tio=90
        tia=250
        alfamate=500
        betamate=250
        ulti=ulti+1
    if ulti==1:
        tim=2
        balãomate=pygame.image.load("matematica2.png")
        balãomate=pygame.transform.scale(balãomate, (200, 200))
    if ulti==2 and tim==2:
        balãomate=pygame.image.load("espaço.png")
        balãomate=pygame.transform.scale(balãomate, (200, 200))
        tim=3
    if event.type==pygame.MOUSEBUTTONDOWN and 69<mouse[0]<240 and 540>mouse[1]>370 and ff==0 or event.type==pygame.MOUSEBUTTONDOWN and epa==True and qek==True:
        BACKGROUND=pygame.image.load("sala de aula.png")
        BACKGROUND=pygame.transform.scale(BACKGROUND, (LARGURA, ALTURA))
        ff=ff=1
        a=-600
        b=-600
        aa=-600
        bb=-600
        aaa=-600 
        bbb=-600
        epa=True
        kal=kal+1
        print("printou")
        alfapor=500
        betapor=250
    if kal==1:
        balãopor=pygame.image.load("portugues2.png")
        balãopor=pygame.transform.scale(balãopor, (200, 200))
    if kal==2:
        balãopor=pygame.image.load("portugues3.png")
        balãopor=pygame.transform.scale(balãopor, (200, 200))
    if kal==3:
        balãopor=pygame.image.load("espaço.png")
        balãopor=pygame.transform.scale(balãopor, (200, 200))


#==========================================================================jogo de portugues==================================================================#
    

    comando=pygame.key.get_pressed()
    if comando[pygame.K_SPACE] and epa==True:
        abrir=0
        cena=abrir
        print(cena)
        guta=0
        alfapor=-600
        betapor=-600
        qek=False
        kal=100
        lk=11
        tim=100
    if abrir==0:        
        aaaa=50
        bbbb=150
        animal=pygame.image.load("galinha.png")
        animal=pygame.transform.scale(animal, (170, 170))
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        alfaB=-600
        alfaE=-600
        alfaA=85
        alfaG=155
        alfaA2=225
        alfaU=295
        alfaH=365
        alfaN=435
        alfaI=500
        alfaL=565
        abrir=11
        letra1="A"
        letra2="G" 
        letra3="A"
        letra4="U"
        letra5="H"
        letra6="N"
        letra7="I"
        letra8="L"
        betaA=350
        betaG=350
        betaA2=350
        betaU=350
        betaH=350
        betaN=350
        betaI=350
        betaL=350     
    if abrir==1:
        aaaa=50
        bbbb=180
        animal=pygame.image.load("porco.png")
        animal=pygame.transform.scale(animal, (180, 120))
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        alfaB=-600
        alfaE=-600        
        alfaP=85
        alfaO=155
        alfaI=225
        alfaL=295
        alfaR=435
        alfaC=365
        alfaN=500
        alfaO2=565
        letra1="P"
        letra2="O" 
        letra3="I"
        letra4="L"
        letra5="C"
        letra6="R"
        letra7="N"
        letra8="O"
        abrir=11
        betaP=350
        betaO=350
        betaI=350
        betaL=350
        betaR=350
        betaC=350
        betaN=350
        betaO2=350
    if abrir==2:
        aaaa=50
        bbbb=150
        animal=pygame.image.load("cachorro.png")
        animal=pygame.transform.scale(animal, (170, 170))
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        alfaB=-600
        alfaE=-600  
        alfaR=85
        alfaH=155
        alfaO2=225
        alfaC=295
        alfaC2=365
        alfaR2=435
        alfaO=500
        alfaA=565
        abrir=11
        letra1="R"
        letra2="H" 
        letra3="O"
        letra4="C"
        letra5="C"
        letra6="R"
        letra7="O"
        letra8="A"
        betaC=350
        betaA=350
        betaC2=350
        betaH=350
        betaO2=350
        betaR=350
        betaR2=350
        betaO=350
    if abrir==3:
        aaaa=50
        bbbb=180
        animal=pygame.image.load("rato.png")
        animal=pygame.transform.scale(animal, (170, 170))
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        alfaB=-600
        alfaE=-600  
        alfaA2=85
        alfaO=155
        alfaA=225
        alfaR=295
        alfaU=365
        alfaG=435
        alfaT=500
        alfaO2=565
        abrir=11
        letra1="A"
        letra2="O" 
        letra3="A"
        letra4="R"
        letra5="U"
        letra6="G"
        letra7="T"
        letra8="O"
        betaA2=350
        betaO=350
        betaA=350
        betaR=350
        betaU=350
        betaG=350
        betaT=350
        betaO2=350
    if abrir==4:
        aaaa=50
        bbbb=150
        animal=pygame.image.load("gato.png")
        animal=pygame.transform.scale(animal, (170, 170))
        alfaB=-600
        alfaE=-600  
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        alfaT=85
        alfaR=155
        alfaR2=225
        alfaU=295
        alfaA=365
        alfaL=435
        alfaO=500
        alfaG=565
        abrir=11
        letra1="T"
        letra2="R" 
        letra3="R"
        letra4="U"
        letra5="A"
        letra6="L"
        letra7="O"
        letra8="G"
        betaT=350
        betaR=350
        betaR2=350
        betaU=350
        betaA=350
        betaL=350
        betaO=350
        betaG=350
    if abrir==5:
        aaaa=50
        bbbb=150
        animal=pygame.image.load("pinguim.png")
        animal=pygame.transform.scale(animal, (170, 170))
        alfaB=-600
        alfaE=-600  
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        alfaU=85
        alfaT=155
        alfaN=225
        alfaP=295
        alfaG=365
        alfaI=435
        alfaI2=500
        alfaM=565
        abrir=11
        letra1="U"
        letra2="T" 
        letra3="N"
        letra4="P"
        letra5="G"
        letra6="I"
        letra7="I"
        letra8="M"
        betaU=350
        betaT=350
        betaN=350
        betaP=350
        betaG=350
        betaI=350
        betaI2=350
        betaM=350
    if abrir==6:
        aaaa=50
        bbbb=150
        animal=pygame.image.load("pato.png")
        animal=pygame.transform.scale(animal, (200, 200))
        alfaB=-600
        alfaE=-600  
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        alfaT=85
        alfaU=155
        alfaA=225
        alfaR=295
        alfaG=365
        alfaI=435
        alfaO=500
        alfaP=565
        abrir=11
        letra1="T"
        letra2="U" 
        letra3="A"
        letra4="R"
        letra5="G"
        letra6="T"
        letra7="O"
        letra8="P"
        betaT=350
        betaU=350
        betaA=350
        betaR=350
        betaG=350
        betaI=350
        betaO=350
        betaP=350
    if abrir==7:
        aaaa=50
        bbbb=150
        animal=pygame.image.load("abelha.png")
        animal=pygame.transform.scale(animal, (200, 200))
        alfaB=-600
        alfaE=-600  
        alfaA=-600
        alfaG=-600
        alfaA2=-600
        alfaU=-600
        alfaH=-600
        alfaN=-600
        alfaI=-600
        alfaI2=-600
        alfaL=-600
        alfaP=-600
        alfaO=-600
        alfaR=-600
        alfaR2=-600
        alfaC=-600
        alfaC2=-600
        alfaO2=-600
        alfaL=-600
        alfaT=-600
        alfaM=-600
        alfaB=-600
        alfaE=-600
        alfaM=85
        alfaA2=155
        alfaA=225
        alfaR=295
        alfaB=365
        alfaL=435
        alfaE=500
        alfaH=565
        abrir=11
        letra1="M"
        letra2="A" 
        letra3="A"
        letra4="R"
        letra5="B"
        letra6="L"
        letra7="E"
        letra8="H"
        betaM=350
        betaA2=350
        betaA=350
        betaR=350
        betaB=350
        betaL=350
        betaE=350
        betaH=350
    if event.type==pygame.MOUSEBUTTONDOWN and 84<mouse[0]<135 and 345<mouse[1]<400 and abrir==11 and guta<9:
        guta=guta+1
        print("gege")
        if guta==1 and cena==0:
            alfaA=230
            betaA=240
            lixta=lixta+letra1
        if guta==2 and cena==0:
            alfaA=285
            betaA=240
            lixta=lixta+letra1  
        if guta==3 and cena==0:
            alfaA=340
            betaA=240
            lixta=lixta+letra1  
        if guta==4 and cena==0:
            alfaA=395
            betaA=240
            lixta=lixta+letra1  
        if guta==5 and cena==0:
            alfaA=450
            betaA=240
            lixta=lixta+letra1  
        if guta==6 and cena==0:
            alfaA=505
            betaA=240
            lixta=lixta+letra1  
        if guta==7 and cena==0:
            alfaA=560
            betaA=240
            lixta=lixta+letra1
        if guta==1 and cena==1:
            alfaP=230
            betaP=240
            lixta=lixta+letra1
        if guta==2 and cena==1:
            alfaP=285
            betaP=240
            lixta=lixta+letra1  
        if guta==3 and cena==1:
            alfaP=340
            betaP=240
            lixta=lixta+letra1  
        if guta==4 and cena==1:
            alfaP=395
            betaP=240
            lixta=lixta+letra1  
        if guta==5 and cena==1:
            alfaP=450
            betaP=240
            lixta=lixta+letra1  
        if guta==6 and cena==1:
            alfaP=505
            betaP=240
            lixta=lixta+letra1  
        if guta==7 and cena==1:
            alfaP=560
            betaP=240
            lixta=lixta+letra1
        if guta==1 and cena==2:
            alfaR=230
            betaR=240
            lixta=lixta+letra1
        if guta==2 and cena==2:
            alfaR=285
            betaR=240
            lixta=lixta+letra1  
        if guta==3 and cena==2:
            alfaR=340
            betaR=240
            lixta=lixta+letra1  
        if guta==4 and cena==2:
            alfaR=395
            betaR=240
            lixta=lixta+letra1  
        if guta==5 and cena==2:
            alfaR=450
            betaR=240
            lixta=lixta+letra1  
        if guta==6 and cena==2:
            alfaR=505
            betaR=240
            lixta=lixta+letra1  
        if guta==7 and cena==2:
            alfaR=560
            betaR=240
            lixta=lixta+letra1
        if guta==8 and cena==2:
            lixta=lixta+letra1
        if guta==1 and cena==3:
            alfaA2=230
            betaA2=240
            lixta=lixta+letra1
        if guta==2 and cena==3:
            alfaA2=285
            betaA2=240
            lixta=lixta+letra1  
        if guta==3 and cena==3:
            alfaA2=340
            betaA2=240
            lixta=lixta+letra1  
        if guta==4 and cena==3:
            alfaA2=395
            betaA2=240
            lixta=lixta+letra1  
        if guta==5 and cena==3:
            alfaA2=450
            betaA2=240
            lixta=lixta+letra1  
        if guta==6 and cena==3:
            alfaA2=505
            betaA2=240
            lixta=lixta+letra1  
        if guta==7 and cena==3:
            alfaA2=560
            betaA2=240
            lixta=lixta+letra1
        if guta==1 and cena==4:
            alfaT=230
            betaT=240
            lixta=lixta+letra1
        if guta==2 and cena==4:
            alfaT=285
            betaT=240
            lixta=lixta+letra1  
        if guta==3 and cena==4:
            alfaT=340
            betaT=240
            lixta=lixta+letra1  
        if guta==4 and cena==4:
            alfaT=395
            betaT=240
            lixta=lixta+letra1  
        if guta==5 and cena==4:
            alfaT=450
            betaT=240
            lixta=lixta+letra1  
        if guta==6 and cena==4:
            alfaT=505
            betaT=240
            lixta=lixta+letra1  
        if guta==7 and cena==4:
            alfaT=560
            betaT=240
            lixta=lixta+letra1
        if guta==1 and cena==5:
            alfaU=230
            betaU=240
            lixta=lixta+letra1
        if guta==2 and cena==5:
            alfaU=285
            betaU=240
            lixta=lixta+letra1  
        if guta==3 and cena==5:
            alfaU=340
            betaU=240
            lixta=lixta+letra1  
        if guta==4 and cena==5:
            alfaU=395
            betaU=240
            lixta=lixta+letra1  
        if guta==5 and cena==5:
            alfaU=450
            betaU=240
            lixta=lixta+letra1  
        if guta==6 and cena==5:
            alfaU=505
            betaU=240
            lixta=lixta+letra1  
        if guta==7 and cena==5:
            alfaU=560
            betaU=240
            lixta=lixta+letra1
        if guta==1 and cena==6:
            alfaT=230
            betaT=240
            lixta=lixta+letra1
        if guta==2 and cena==6:
            alfaT=285
            betaT=240
            lixta=lixta+letra1  
        if guta==3 and cena==6:
            alfaT=340
            betaT=240
            lixta=lixta+letra1  
        if guta==4 and cena==6:
            alfaT=395
            betaT=240
            lixta=lixta+letra1  
        if guta==5 and cena==6:
            alfaT=450
            betaT=240
            lixta=lixta+letra1  
        if guta==6 and cena==6:
            alfaT=505
            betaT=240
            lixta=lixta+letra1  
        if guta==7 and cena==6:
            alfaT=560
            betaT=240
            lixta=lixta+letra1
        if guta==1 and cena==7:
            alfaM=230
            betaM=240
            lixta=lixta+letra1
        if guta==2 and cena==7:
            alfaM=285
            betaM=240
            lixta=lixta+letra1  
        if guta==3 and cena==7:
            alfaM=340
            betaM=240
            lixta=lixta+letra1  
        if guta==4 and cena==7:
            alfaM=395
            betaM=240
            lixta=lixta+letra1  
        if guta==5 and cena==7:
            alfaM=450
            betaM=240
            lixta=lixta+letra1  
        if guta==6 and cena==7:
            alfaM=505
            betaM=240
            lixta=lixta+letra1  
        if guta==7 and cena==7:
            alfaM=560
            betaM=240
            lixta=lixta+letra1                   
    if event.type==pygame.MOUSEBUTTONDOWN and 153<mouse[0]<205 and 345<mouse[1]<400 and abrir==11 and guta<9:
        print("ge")
        guta=guta+1
        if guta==1 and cena==0:
            alfaG=230
            betaG=240
            lixta=lixta+letra2
        if guta==2 and cena==0:
            alfaG=285
            betaG=240
            lixta=lixta+letra2
        if guta==3 and cena==0:
            alfaG=340
            betaG=240
            lixta=lixta+letra2
        if guta==4 and cena==0:
            alfaG=395
            betaG=240
            lixta=lixta+letra2
        if guta==5 and cena==0:
            alfaG=450
            betaG=240
            lixta=lixta+letra2
        if guta==6 and cena==0:
            alfaG=505
            betaG=240
            lixta=lixta+letra2
        if guta==7 and cena==0:
            alfaG=560
            betaG=240
            lixta=lixta+letra2
        if guta==1 and cena==1:
            alfaO=230
            betaO=240
            lixta=lixta+letra2
        if guta==2 and cena==1:
            alfaO=285
            betaO=240
            lixta=lixta+letra2
        if guta==3 and cena==1:
            alfaO=340
            betaO=240
            lixta=lixta+letra2
        if guta==4 and cena==1:
            alfaO=395
            betaO=240
            lixta=lixta+letra2
        if guta==5 and cena==1:
            alfaO=450
            betaO=240
            lixta=lixta+letra2
        if guta==6 and cena==1:
            alfaO=505
            betaO=240
            lixta=lixta+letra2
        if guta==7 and cena==1:
            alfaO=560
            betaO=240
            lixta=lixta+letra2
        if guta==1 and cena==2:
            alfaH=230
            betaH=240
            lixta=lixta+letra2
        if guta==2 and cena==2:
            alfaH=285
            betaH=240
            lixta=lixta+letra2
        if guta==3 and cena==2:
            alfaH=340
            betaH=240
            lixta=lixta+letra2
        if guta==4 and cena==2:
            alfaH=395
            betaH=240
            lixta=lixta+letra2
        if guta==5 and cena==2:
            alfaH=450
            betaH=240
            lixta=lixta+letra2
        if guta==6 and cena==2:
            alfaH=505
            betaH=240
            lixta=lixta+letra2
        if guta==7 and cena==2:
            alfaH=560
            betaH=240
            lixta=lixta+letra2
        if guta==8 and cena==2:
            lixta=lixta+letra2
        if guta==1 and cena==3:
            alfaO=230
            betaO=240
            lixta=lixta+letra2
        if guta==2 and cena==3:
            alfaO=285
            betaO=240
            lixta=lixta+letra2
        if guta==3 and cena==3:
            alfaO=340
            betaO=240
            lixta=lixta+letra2
        if guta==4 and cena==3:
            alfaO=395
            betaO=240
            lixta=lixta+letra2
        if guta==5 and cena==3:
            alfaO=450
            betaO=240
            lixta=lixta+letra2
        if guta==6 and cena==3:
            alfaO=505
            betaO=240
            lixta=lixta+letra2
        if guta==7 and cena==3:
            alfaO=560
            betaO=240
            lixta=lixta+letra2
        if guta==1 and cena==4:
            alfaR=230
            betaR=240
            lixta=lixta+letra2
        if guta==2 and cena==4:
            alfaR=285
            betaR=240
            lixta=lixta+letra2
        if guta==3 and cena==4:
            alfaR=340
            betaR=240
            lixta=lixta+letra2
        if guta==4 and cena==4:
            alfaR=395
            betaR=240
            lixta=lixta+letra2
        if guta==5 and cena==4:
            alfaR=450
            betaR=240
            lixta=lixta+letra2
        if guta==6 and cena==4:
            alfaR=505
            betaR=240
            lixta=lixta+letra2
        if guta==7 and cena==4:
            alfaR=560
            betaR=240
            lixta=lixta+letra2
        if guta==1 and cena==5:
            alfaT=230
            betaT=240
            lixta=lixta+letra2
        if guta==2 and cena==5:
            alfaT=285
            betaT=240
            lixta=lixta+letra2
        if guta==3 and cena==5:
            alfaT=340
            betaT=240
            lixta=lixta+letra2
        if guta==4 and cena==5:
            alfaT=395
            betaT=240
            lixta=lixta+letra2
        if guta==5 and cena==5:
            alfaT=450
            betaT=240
            lixta=lixta+letra2
        if guta==6 and cena==5:
            alfaT=505
            betaT=240
            lixta=lixta+letra2
        if guta==7 and cena==5:
            alfaT=560
            betaT=240
            lixta=lixta+letra2
        if guta==1 and cena==6:
            alfaU=230
            betaU=240
            lixta=lixta+letra2
        if guta==2 and cena==6:
            alfaU=285
            betaU=240
            lixta=lixta+letra2
        if guta==3 and cena==6:
            alfaU=340
            betaU=240
            lixta=lixta+letra2
        if guta==4 and cena==6:
            alfaU=395
            betaU=240
            lixta=lixta+letra2
        if guta==5 and cena==6:
            alfaU=450
            betaU=240
            lixta=lixta+letra2
        if guta==6 and cena==6:
            alfaU=505
            betaU=240
            lixta=lixta+letra2
        if guta==7 and cena==6:
            alfaU=560
            betaU=240
            lixta=lixta+letra2
        if guta==1 and cena==7:
            alfaA2=230
            betaA2=240
            lixta=lixta+letra2
        if guta==2 and cena==7:
            alfaA2=285
            betaA2=240
            lixta=lixta+letra2
        if guta==3 and cena==7:
            alfaA2=340
            betaA2=240
            lixta=lixta+letra2
        if guta==4 and cena==7:
            alfaA2=395
            betaA2=240
            lixta=lixta+letra2
        if guta==5 and cena==7:
            alfaA2=450
            betaA2=240
            lixta=lixta+letra2
        if guta==6 and cena==7:
            alfaA2=505
            betaA2=240
            lixta=lixta+letra2
        if guta==7 and cena==7:
            alfaA2=560
            betaA2=240
            lixta=lixta+letra2            
    if event.type==pygame.MOUSEBUTTONDOWN and 223<mouse[0]<275 and 345<mouse[1]<400 and abrir==11 and guta<9:
        guta=guta+1
        print("ge")
        if guta==1 and cena==0:
            alfaA2=230
            betaA2=240
            lixta=lixta+letra3
        if guta==2 and cena==0:
            alfaA2=285
            betaA2=240
            lixta=lixta+letra3
        if guta==3 and cena==0:
            alfaA2=340
            betaA2=240
            lixta=lixta+letra3
        if guta==4 and cena==0:
            alfaA2=395
            betaA2=240
            lixta=lixta+letra3
        if guta==5 and cena==0:
            alfaA2=450
            betaA2=240
            lixta=lixta+letra3
        if guta==6 and cena==0:
            alfaA2=505
            betaA2=240
            lixta=lixta+letra3
        if guta==7 and cena==0:
            alfaA2=560
            betaA2=240
            lixta=lixta+letra3
        if guta==1 and cena==1:
            alfaI=230
            betaI=240
            lixta=lixta+letra3
        if guta==2 and cena==1:
            alfaI=285
            betaI=240
            lixta=lixta+letra3
        if guta==3 and cena==1:
            alfaI=340
            betaI=240
            lixta=lixta+letra3
        if guta==4 and cena==1:
            alfaI=395
            betaI=240
            lixta=lixta+letra3
        if guta==5 and cena==1:
            alfaI=450
            betaI=240
            lixta=lixta+letra3
        if guta==6 and cena==1:
            alfaI=505
            betaI=240
            lixta=lixta+letra3
        if guta==7 and cena==1:
            alfaI=560
            betaI=240
            lixta=lixta+letra3
            print(lixta)
        if guta==1 and cena==2:
            alfaO2=230
            betaO2=240
            lixta=lixta+letra3
        if guta==2 and cena==2:
            alfaO2=285
            betaO2=240
            lixta=lixta+letra3
        if guta==3 and cena==2:
            alfaO2=340
            betaO2=240
            lixta=lixta+letra3
        if guta==4 and cena==2:
            alfaO2=395
            betaO2=240
            lixta=lixta+letra3
        if guta==5 and cena==2:
            alfaO2=450
            betaO2=240
            lixta=lixta+letra3
        if guta==6 and cena==2:
            alfaO2=505
            betaO2=240
            lixta=lixta+letra3
        if guta==7 and cena==2:
            alfaO2=560
            betaO2=240
            lixta=lixta+letra3
        if guta==8 and cena==2:
            lixta=lixta+letra3
        if guta==1 and cena==3:
            alfaA=230
            betaA=240
            lixta=lixta+letra3
        if guta==2 and cena==3:
            alfaA=285
            betaA=240
            lixta=lixta+letra3
        if guta==3 and cena==3:
            alfaA=340
            betaA=240
            lixta=lixta+letra3
        if guta==4 and cena==3:
            alfaA=395
            betaA=240
            lixta=lixta+letra3
        if guta==5 and cena==3:
            alfaA=450
            betaA=240
            lixta=lixta+letra3
        if guta==6 and cena==3:
            alfaA=505
            betaA=240
            lixta=lixta+letra3
        if guta==7 and cena==3:
            alfaA=560
            betaA=240
            lixta=lixta+letra3
        if guta==1 and cena==4:
            alfaR2=230
            betaR2=240
            lixta=lixta+letra3
        if guta==2 and cena==4:
            alfaR2=285
            betaR2=240
            lixta=lixta+letra3
        if guta==3 and cena==4:
            alfaR2=340
            betaR2=240
            lixta=lixta+letra3
        if guta==4 and cena==4:
            alfaR2=395
            betaR2=240
            lixta=lixta+letra3
        if guta==5 and cena==4:
            alfaR2=450
            betaR2=240
            lixta=lixta+letra3
        if guta==6 and cena==4:
            alfaR2=505
            betaR2=240
            lixta=lixta+letra3
        if guta==7 and cena==4:
            alfaR2=560
            betaR2=240
            lixta=lixta+letra3
        if guta==1 and cena==5:
            alfaN=230
            betaN=240
            lixta=lixta+letra3
        if guta==2 and cena==5:
            alfaN=285
            betaN=240
            lixta=lixta+letra3
        if guta==3 and cena==5:
            alfaN=340
            betaN=240
            lixta=lixta+letra3
        if guta==4 and cena==5:
            alfaN=395
            betaN=240
            lixta=lixta+letra3
        if guta==5 and cena==5:
            alfaN=450
            betaN=240
            lixta=lixta+letra3
        if guta==6 and cena==5:
            alfaN=505
            betaN=240
            lixta=lixta+letra3
        if guta==7 and cena==5:
            alfaN=560
            betaN=240
            lixta=lixta+letra3
        if guta==1 and cena==6:
            alfaA=230
            betaA=240
            lixta=lixta+letra3
        if guta==2 and cena==6:
            alfaA=285
            betaA=240
            lixta=lixta+letra3
        if guta==3 and cena==6:
            alfaA=340
            betaA=240
            lixta=lixta+letra3
        if guta==4 and cena==6:
            alfaA=395
            betaA=240
            lixta=lixta+letra3
        if guta==5 and cena==6:
            alfaA=450
            betaA=240
            lixta=lixta+letra3
        if guta==6 and cena==6:
            alfaA=505
            betaA=240
            lixta=lixta+letra3
        if guta==7 and cena==6:
            alfaA=560
            betaA=240
            lixta=lixta+letra3
        if guta==1 and cena==7:
            alfaA=230
            betaA=240
            lixta=lixta+letra3
        if guta==2 and cena==7:
            alfaA=285
            betaA=240
            lixta=lixta+letra3
        if guta==3 and cena==7:
            alfaA=340
            betaA=240
            lixta=lixta+letra3
        if guta==4 and cena==7:
            alfaA=395
            betaA=240
            lixta=lixta+letra3
        if guta==5 and cena==7:
            alfaA=450
            betaA=240
            lixta=lixta+letra3
        if guta==6 and cena==7:
            alfaA=505
            betaA=240
            lixta=lixta+letra3
        if guta==7 and cena==7:
            alfaA=560
            betaA=240
            lixta=lixta+letra3          
    if event.type==pygame.MOUSEBUTTONDOWN and 293<mouse[0]<345 and 345<mouse[1]<400 and abrir==11 and guta<9:
        guta=guta+1
        print("ge")
        if guta==1 and cena==0:
            alfaU=230
            betaU=240
            lixta=lixta+letra4
        if guta==2 and cena==0:
            alfaU=285
            betaU=240
            lixta=lixta+letra4
        if guta==3 and cena==0:
            alfaU=340
            betaU=240
            lixta=lixta+letra4
        if guta==4 and cena==0:
            alfaU=395
            betaU=240
            lixta=lixta+letra4
        if guta==5 and cena==0:
            alfaU=450
            betaU=240
            lixta=lixta+letra4
        if guta==6 and cena==0:
            alfaU=505
            betaU=240
            lixta=lixta+letra4
        if guta==7 and cena==0:
            alfaU=560
            betaU=240
            lixta=lixta+letra4
        if guta==1 and cena==1:
            alfaL=230
            betaL=240
            lixta=lixta+letra4
        if guta==2 and cena==1:
            alfaL=285
            betaL=240
            lixta=lixta+letra4
        if guta==3 and cena==1:
            alfaL=340
            betaL=240
            lixta=lixta+letra4
        if guta==4 and cena==1:
            alfaL=395
            betaL=240
            lixta=lixta+letra4
        if guta==5 and cena==1:
            alfaL=450
            betaL=240
            lixta=lixta+letra4
        if guta==6 and cena==1:
            alfaL=505
            betaL=240
            lixta=lixta+letra4
        if guta==7 and cena==1:
            alfaL=560
            betaL=240
            lixta=lixta+letra4
        if guta==1 and cena==2:
            alfaC=230
            betaC=240
            lixta=lixta+letra4
        if guta==2 and cena==2:
            alfaC=285
            betaC=240
            lixta=lixta+letra4
        if guta==3 and cena==2:
            alfaC=340
            betaC=240
            lixta=lixta+letra4
        if guta==4 and cena==2:
            alfaC=395
            betaC=240
            lixta=lixta+letra4
        if guta==5 and cena==2:
            alfaC=450
            betaC=240
            lixta=lixta+letra4
        if guta==6 and cena==2:
            alfaC=505
            betaC=240
            lixta=lixta+letra4
        if guta==7 and cena==2:
            alfaC=560
            betaC=240
            lixta=lixta+letra4
        if guta==8 and cena==2:
            lixta=lixta+letra4
        if guta==1 and cena==3:
            alfaR=230
            betaR=240
            lixta=lixta+letra4
        if guta==2 and cena==3:
            alfaR=285
            betaR=240
            lixta=lixta+letra4
        if guta==3 and cena==3:
            alfaR=340
            betaR=240
            lixta=lixta+letra4
        if guta==4 and cena==3:
            alfaR=395
            betaR=240
            lixta=lixta+letra4
        if guta==5 and cena==3:
            alfaR=450
            betaR=240
            lixta=lixta+letra4
        if guta==6 and cena==3:
            alfaR=505
            betaR=240
            lixta=lixta+letra4
        if guta==7 and cena==3:
            alfaR=560
            betaR=240
            lixta=lixta+letra4
        if guta==1 and cena==4:
            alfaU=230
            betaU=240
            lixta=lixta+letra4
        if guta==2 and cena==4:
            alfaU=285
            betaU=240
            lixta=lixta+letra4
        if guta==3 and cena==4:
            alfaU=340
            betaU=240
            lixta=lixta+letra4
        if guta==4 and cena==4:
            alfaU=395
            betaU=240
            lixta=lixta+letra4
        if guta==5 and cena==4:
            alfaU=450
            betaU=240
            lixta=lixta+letra4
        if guta==6 and cena==4:
            alfaU=505
            betaU=240
            lixta=lixta+letra4
        if guta==7 and cena==4:
            alfaU=560
            betaU=240
            lixta=lixta+letra4
        if guta==1 and cena==5:
            alfaP=230
            betaP=240
            lixta=lixta+letra4
        if guta==2 and cena==5:
            alfaP=285
            betaP=240
            lixta=lixta+letra4
        if guta==3 and cena==5:
            alfaP=340
            betaP=240
            lixta=lixta+letra4
        if guta==4 and cena==5:
            alfaP=395
            betaP=240
            lixta=lixta+letra4
        if guta==5 and cena==5:
            alfaP=450
            betaP=240
            lixta=lixta+letra4
        if guta==6 and cena==5:
            alfaP=505
            betaP=240
            lixta=lixta+letra4
        if guta==7 and cena==5:
            alfaP=560
            betaP=240
            lixta=lixta+letra4
        if guta==1 and cena==6:
            alfaR=230
            betaR=240
            lixta=lixta+letra4
        if guta==2 and cena==6:
            alfaR=285
            betaR=240
            lixta=lixta+letra4
        if guta==3 and cena==6:
            alfaR=340
            betaR=240
            lixta=lixta+letra4
        if guta==4 and cena==6:
            alfaR=395
            betaR=240
            lixta=lixta+letra4
        if guta==5 and cena==6:
            alfaR=450
            betaR=240
            lixta=lixta+letra4
        if guta==6 and cena==6:
            alfaR=505
            betaR=240
            lixta=lixta+letra4
        if guta==7 and cena==6:
            alfaR=560
            betaR=240
            lixta=lixta+letra4
        if guta==1 and cena==7:
            alfaR=230
            betaR=240
            lixta=lixta+letra4
        if guta==2 and cena==7:
            alfaR=285
            betaR=240
            lixta=lixta+letra4
        if guta==3 and cena==7:
            alfaR=340
            betaR=240
            lixta=lixta+letra4
        if guta==4 and cena==7:
            alfaR=395
            betaR=240
            lixta=lixta+letra4
        if guta==5 and cena==7:
            alfaR=450
            betaR=240
            lixta=lixta+letra4
        if guta==6 and cena==7:
            alfaR=505
            betaR=240
            lixta=lixta+letra4
        if guta==7 and cena==7:
            alfaR=560
            betaR=240
            lixta=lixta+letra4    
    if event.type==pygame.MOUSEBUTTONDOWN and 363<mouse[0]<415 and 345<mouse[1]<400 and abrir==11 and guta<9:
        guta=guta+1
        print("ge")
        if guta==1 and cena==0:
            alfaH=230
            betaH=240
            lixta=lixta+letra5
        if guta==2 and cena==0:
            alfaH=285
            betaH=240
            lixta=lixta+letra5
        if guta==3 and cena==0:
            alfaH=340
            betaH=240
            lixta=lixta+letra5
        if guta==4 and cena==0:
            alfaH=395
            betaH=240
            lixta=lixta+letra5
        if guta==5 and cena==0:
            alfaH=450
            betaH=240
            lixta=lixta+letra5
        if guta==6 and cena==0:
            alfaH=505
            betaH=240
            lixta=lixta+letra5
        if guta==7 and cena==0:
            alfaH=560
            betaH=240
            lixta=lixta+letra5
        if guta==1 and cena==1:
            alfaC=230
            betaC=240
            lixta=lixta+letra5
        if guta==2 and cena==1:
            alfaC=285
            betaC=240
            lixta=lixta+letra5
        if guta==3 and cena==1:
            alfaC=340
            betaC=240
            lixta=lixta+letra5
        if guta==4 and cena==1:
            alfaC=395
            betaC=240
            lixta=lixta+letra5
        if guta==5 and cena==1:
            alfaC=450
            betaC=240
            lixta=lixta+letra5
        if guta==6 and cena==1:
            alfaC=505
            betaC=240
            lixta=lixta+letra5
        if guta==7 and cena==1:
            alfaC=560
            betaC=240
            lixta=lixta+letra5
        if guta==1 and cena==2:
            alfaC2=230
            betaC2=240
            lixta=lixta+letra5
        if guta==2 and cena==2:
            alfaC2=285
            betaC2=240
            lixta=lixta+letra5
        if guta==3 and cena==2:
            alfaC2=340
            betaC2=240
            lixta=lixta+letra5
        if guta==4 and cena==2:
            alfaC2=395
            betaC2=240
            lixta=lixta+letra5
        if guta==5 and cena==2:
            alfaC2=450
            betaC2=240
            lixta=lixta+letra5
        if guta==6 and cena==2:
            alfaC2=505
            betaC2=240
            lixta=lixta+letra5
        if guta==7 and cena==2:
            alfaC2=560
            betaC2=240
            lixta=lixta+letra5
        if guta==8 and cena==2:
            lixta=lixta+letra5
        if guta==1 and cena==3:
            alfaU=230
            betaU=240
            lixta=lixta+letra5
        if guta==2 and cena==3:
            alfaU=285
            betaU=240
            lixta=lixta+letra5
        if guta==3 and cena==3:
            alfaU=340
            betaU=240
            lixta=lixta+letra5
        if guta==4 and cena==3:
            alfaU=395
            betaU=240
            lixta=lixta+letra5
        if guta==5 and cena==3:
            alfaU=450
            betaU=240
            lixta=lixta+letra5
        if guta==6 and cena==3:
            alfaU=505
            betaU=240
            lixta=lixta+letra5
        if guta==7 and cena==3:
            alfaU=560
            betaU=240
            lixta=lixta+letra5
        if guta==1 and cena==4:
            alfaA=230
            betaA=240
            lixta=lixta+letra5
        if guta==2 and cena==4:
            alfaA=285
            betaA=240
            lixta=lixta+letra5
        if guta==3 and cena==4:
            alfaA=340
            betaA=240
            lixta=lixta+letra5
        if guta==4 and cena==4:
            alfaA=395
            betaA=240
            lixta=lixta+letra5
        if guta==5 and cena==4:
            alfaA=450
            betaA=240
            lixta=lixta+letra5
        if guta==6 and cena==4:
            alfaA=505
            betaA=240
            lixta=lixta+letra5
        if guta==7 and cena==4:
            alfaA=560
            betaA=240
            lixta=lixta+letra5
        if guta==1 and cena==5:
            alfaG=230
            betaG=240
            lixta=lixta+letra5
        if guta==2 and cena==5:
            alfaG=285
            betaG=240
            lixta=lixta+letra5
        if guta==3 and cena==5:
            alfaG=340
            betaG=240
            lixta=lixta+letra5
        if guta==4 and cena==5:
            alfaG=395
            betaG=240
            lixta=lixta+letra5
        if guta==5 and cena==5:
            alfaG=450
            betaG=240
            lixta=lixta+letra5
        if guta==6 and cena==5:
            alfaG=505
            betaG=240
            lixta=lixta+letra5
        if guta==7 and cena==5:
            alfaG=560
            betaG=240
            lixta=lixta+letra5
        if guta==1 and cena==6:
            alfaG=230
            betaG=240
            lixta=lixta+letra5
        if guta==2 and cena==6:
            alfaG=285
            betaG=240
            lixta=lixta+letra5
        if guta==3 and cena==6:
            alfaG=340
            betaG=240
            lixta=lixta+letra5
        if guta==4 and cena==6:
            alfaG=395
            betaG=240
            lixta=lixta+letra5
        if guta==5 and cena==6:
            alfaG=450
            betaG=240
            lixta=lixta+letra5
        if guta==6 and cena==6:
            alfaG=505
            betaG=240
            lixta=lixta+letra5
        if guta==7 and cena==6:
            alfaG=560
            betaG=240
            lixta=lixta+letra5 
        if guta==1 and cena==7:
            alfaB=230
            betaB=240
            lixta=lixta+letra5
        if guta==2 and cena==7:
            alfaB=285
            betaB=240
            lixta=lixta+letra5
        if guta==3 and cena==7:
            alfaB=340
            betaB=240
            lixta=lixta+letra5
        if guta==4 and cena==7:
            alfaB=395
            betaB=240
            lixta=lixta+letra5
        if guta==5 and cena==7:
            alfaB=450
            betaB=240
            lixta=lixta+letra5
        if guta==6 and cena==7:
            alfaB=505
            betaB=240
            lixta=lixta+letra5
        if guta==7 and cena==7:
            alfaB=560
            betaB=240
            lixta=lixta+letra5                     
    if event.type==pygame.MOUSEBUTTONDOWN and 433<mouse[0]<485 and 345<mouse[1]<400 and abrir==11 and guta<9:
        guta=guta+1
        print("ge")
        if guta==1 and cena==0:
            alfaN=230
            betaN=240
            lixta=lixta+letra6
        if guta==2 and cena==0:
            alfaN=285
            betaN=240
            lixta=lixta+letra6
        if guta==3 and cena==0:
            alfaN=340
            betaN=240
            lixta=lixta+letra6
        if guta==4 and cena==0:
            alfaN=395
            betaN=240
            lixta=lixta+letra6
        if guta==5 and cena==0:
            alfaN=450
            betaN=240
            lixta=lixta+letra6
        if guta==6 and cena==0:
            alfaN=505
            betaN=240
            lixta=lixta+letra6
        if guta==7 and cena==0:
            alfaN=560
            betaN=240
            lixta=lixta+letra6
        if guta==1 and cena==1:
            alfaR=230
            betaR=240
            lixta=lixta+letra6
        if guta==2 and cena==1:
            alfaR=285
            betaR=240
            lixta=lixta+letra6
        if guta==3 and cena==1:
            alfaR=340
            betaR=240
            lixta=lixta+letra6
        if guta==4 and cena==1:
            alfaR=395
            betaR=240
            lixta=lixta+letra6
        if guta==5 and cena==1:
            alfaR=450
            betaR=240
            lixta=lixta+letra6
        if guta==6 and cena==1:
            alfaR=505
            betaR=240
            lixta=lixta+letra6
        if guta==7 and cena==1:
            alfaR=560
            betaR=240
            lixta=lixta+letra6
        if guta==1 and cena==2:
            alfaR2=230
            betaR2=240
            lixta=lixta+letra6
        if guta==2 and cena==2:
            alfaR2=285
            betaR2=240
            lixta=lixta+letra6
        if guta==3 and cena==2:
            alfaR2=340
            betaR2=240
            lixta=lixta+letra6
        if guta==4 and cena==2:
            alfaR2=395
            betaR2=240
            lixta=lixta+letra6
        if guta==5 and cena==2:
            alfaR2=450
            betaR2=240
            lixta=lixta+letra6
        if guta==6 and cena==2:
            alfaR2=505
            betaR2=240
            lixta=lixta+letra6
        if guta==7 and cena==2:
            alfaR2=560
            betaR2=240
            lixta=lixta+letra6
        if guta==8 and cena==2:
            lixta=lixta+letra6
        if guta==1 and cena==3:
            alfaG=230
            betaG=240
            lixta=lixta+letra6
        if guta==2 and cena==3:
            alfaG=285
            betaG=240
            lixta=lixta+letra6
        if guta==3 and cena==3:
            alfaG=340
            betaG=240
            lixta=lixta+letra6
        if guta==4 and cena==3:
            alfaG=395
            betaG=240
            lixta=lixta+letra6
        if guta==5 and cena==3:
            alfaG=450
            betaG=240
            lixta=lixta+letra6
        if guta==6 and cena==3:
            alfaG=505
            betaG=240
            lixta=lixta+letra6
        if guta==7 and cena==3:
            alfaG=560
            betaG=240
            lixta=lixta+letra6
        if guta==1 and cena==4:
            alfaL=230
            betaL=240
            lixta=lixta+letra6
        if guta==2 and cena==4:
            alfaL=285
            betaL=240
            lixta=lixta+letra6
        if guta==3 and cena==4:
            alfaL=340
            betaL=240
            lixta=lixta+letra6
        if guta==4 and cena==4:
            alfaL=395
            betaL=240
            lixta=lixta+letra6
        if guta==5 and cena==4:
            alfaL=450
            betaL=240
            lixta=lixta+letra6
        if guta==6 and cena==4:
            alfaL=505
            betaL=240
            lixta=lixta+letra6
        if guta==7 and cena==4:
            alfaL=560
            betaL=240
            lixta=lixta+letra6
        if guta==1 and cena==5:
            alfaI=230
            betaI=240
            lixta=lixta+letra6
        if guta==2 and cena==5:
            alfaI=285
            betaI=240
            lixta=lixta+letra6
        if guta==3 and cena==5:
            alfaI=340
            betaI=240
            lixta=lixta+letra6
        if guta==4 and cena==5:
            alfaI=395
            betaI=240
            lixta=lixta+letra6
        if guta==5 and cena==5:
            alfaI=450
            betaI=240
            lixta=lixta+letra6
        if guta==6 and cena==5:
            alfaI=505
            betaI=240
            lixta=lixta+letra6
        if guta==7 and cena==5:
            alfaI=560
            betaI=240
            lixta=lixta+letra6
        if guta==1 and cena==6:
            alfaI=230
            betaI=240
            lixta=lixta+letra6
        if guta==2 and cena==6:
            alfaI=285
            betaI=240
            lixta=lixta+letra6
        if guta==3 and cena==6:
            alfaI=340
            betaI=240
            lixta=lixta+letra6
        if guta==4 and cena==6:
            alfaI=395
            betaI=240
            lixta=lixta+letra6
        if guta==5 and cena==6:
            alfaI=450
            betaI=240
            lixta=lixta+letra6
        if guta==6 and cena==6:
            alfaI=505
            betaI=240
            lixta=lixta+letra6
        if guta==7 and cena==6:
            alfaI=560
            betaI=240
            lixta=lixta+letra6
        if guta==1 and cena==7:
            alfaL=230
            betaL=240
            lixta=lixta+letra6
        if guta==2 and cena==7:
            alfaL=285
            betaL=240
            lixta=lixta+letra6
        if guta==3 and cena==7:
            alfaL=340
            betaL=240
            lixta=lixta+letra6
        if guta==4 and cena==7:
            alfaL=395
            betaL=240
            lixta=lixta+letra6
        if guta==5 and cena==7:
            alfaL=450
            betaL=240
            lixta=lixta+letra6
        if guta==6 and cena==7:
            alfaL=505
            betaL=240
            lixta=lixta+letra6
        if guta==7 and cena==7:
            alfaL=560
            betaL=240
            lixta=lixta+letra6    
    if event.type==pygame.MOUSEBUTTONDOWN and 503<mouse[0]<545 and 345<mouse[1]<400 and abrir==11 and guta<9:
        guta=guta+1
        print("ge")
        if guta==1 and cena==0:
            alfaI=230
            betaI=240
            lixta=lixta+letra7
        if guta==2 and cena==0:
            alfaI=285
            betaI=240
            lixta=lixta+letra7
        if guta==3 and cena==0:
            alfaI=340
            betaI=240
            lixta=lixta+letra7
        if guta==4 and cena==0:
            alfaI=395
            betaI=240
            lixta=lixta+letra7
        if guta==5 and cena==0:
            alfaI=450
            betaI=240
            lixta=lixta+letra7
        if guta==6 and cena==0:
            alfaI=505
            betaI=240
            lixta=lixta+letra7
        if guta==7 and cena==0:
            alfaI=560
            betaI=240
            lixta=lixta+letra7
        if guta==1 and cena==1:
            alfaN=230
            betaN=240
            lixta=lixta+letra7
        if guta==2 and cena==1:
            alfaN=285
            betaN=240
            lixta=lixta+letra7
        if guta==3 and cena==1:
            alfaN=340
            betaN=240
            lixta=lixta+letra7
        if guta==4 and cena==1:
            alfaN=395
            betaN=240
            lixta=lixta+letra7
        if guta==5 and cena==1:
            alfaN=450
            betaN=240
            lixta=lixta+letra7
        if guta==6 and cena==1:
            alfaN=505
            betaN=240
            lixta=lixta+letra7
        if guta==7 and cena==1:
            alfaN=560
            betaN=240
            lixta=lixta+letra7
        if guta==1 and cena==2:
            alfaO=230
            betaO=240
            lixta=lixta+letra7
        if guta==2 and cena==2:
            alfaO=285
            betaO=240
            lixta=lixta+letra7
        if guta==3 and cena==2:
            alfaO=340
            betaO=240
            lixta=lixta+letra7
        if guta==4 and cena==2:
            alfaO=395
            betaO=240
            lixta=lixta+letra7
        if guta==5 and cena==2:
            alfaO=450
            betaO=240
            lixta=lixta+letra7
        if guta==6 and cena==2:
            alfaO=505
            betaO=240
            lixta=lixta+letra7
        if guta==7 and cena==2:
            alfaO=560
            betaO=240
            lixta=lixta+letra7
        if guta==8 and cena==2:
            lixta=lixta+letra7
        if guta==7 and cena==1:
            alfaN=560
            betaN=240
            lixta=lixta+letra7
        if guta==1 and cena==3:
            alfaT=230
            betaT=240
            lixta=lixta+letra7
        if guta==2 and cena==3:
            alfaT=285
            betaT=240
            lixta=lixta+letra7
        if guta==3 and cena==3:
            alfaT=340
            betaT=240
            lixta=lixta+letra7
        if guta==4 and cena==3:
            alfaT=395
            betaT=240
            lixta=lixta+letra7
        if guta==5 and cena==3:
            alfaT=450
            betaT=240
            lixta=lixta+letra7
        if guta==6 and cena==3:
            alfaT=505
            betaT=240
            lixta=lixta+letra7
        if guta==7 and cena==3:
            alfaT=560
            betaT=240
            lixta=lixta+letra7
        if guta==7 and cena==1:
            alfaN=560
            betaN=240
            lixta=lixta+letra7
        if guta==1 and cena==4:
            alfaO=230
            betaO=240
            lixta=lixta+letra7
        if guta==2 and cena==4:
            alfaO=285
            betaO=240
            lixta=lixta+letra7
        if guta==3 and cena==4:
            alfaO=340
            betaO=240
            lixta=lixta+letra7
        if guta==4 and cena==4:
            alfaO=395
            betaO=240
            lixta=lixta+letra7
        if guta==5 and cena==4:
            alfaO=450
            betaO=240
            lixta=lixta+letra7
        if guta==6 and cena==4:
            alfaO=505
            betaO=240
            lixta=lixta+letra7
        if guta==7 and cena==4:
            alfaO=560
            betaO=240
            lixta=lixta+letra7
        if guta==1 and cena==5:
            alfaI2=230
            betaI2=240
            lixta=lixta+letra7
        if guta==2 and cena==5:
            alfaI2=285
            betaI2=240
            lixta=lixta+letra7
        if guta==3 and cena==5:
            alfaI2=340
            betaI2=240
            lixta=lixta+letra7
        if guta==4 and cena==5:
            alfaI2=395
            betaI2=240
            lixta=lixta+letra7
        if guta==5 and cena==5:
            alfaI2=450
            betaI2=240
            lixta=lixta+letra7
        if guta==6 and cena==5:
            alfaI2=505
            betaI2=240
            lixta=lixta+letra7
        if guta==7 and cena==5:
            alfaI2=560
            betaI2=240
            lixta=lixta+letra7
        if guta==1 and cena==6:
            alfaO=230
            betaO=240
            lixta=lixta+letra7
        if guta==2 and cena==6:
            alfaO=285
            betaO=240
            lixta=lixta+letra7
        if guta==3 and cena==6:
            alfaO=340
            betaO=240
            lixta=lixta+letra7
        if guta==4 and cena==6:
            alfaO=395
            betaO=240
            lixta=lixta+letra7
        if guta==5 and cena==6:
            alfaO=450
            betaO=240
            lixta=lixta+letra7
        if guta==6 and cena==6:
            alfaO=505
            betaO=240
            lixta=lixta+letra7
        if guta==7 and cena==6:
            alfaO=560
            betaO=240
            lixta=lixta+letra7
        if guta==1 and cena==7:
            alfaE=230
            betaE=240
            lixta=lixta+letra7
        if guta==2 and cena==7:
            alfaE=285
            betaE=240
            lixta=lixta+letra7
        if guta==3 and cena==7:
            alfaE=340
            betaE=240
            lixta=lixta+letra7
        if guta==4 and cena==7:
            alfaE=395
            betaE=240
            lixta=lixta+letra7
        if guta==5 and cena==7:
            alfaE=450
            betaE=240
            lixta=lixta+letra7
        if guta==6 and cena==7:
            alfaE=505
            betaE=240
            lixta=lixta+letra7
        if guta==7 and cena==7:
            alfaE=560
            betaE=240
            lixta=lixta+letra7
    if event.type==pygame.MOUSEBUTTONDOWN and 565<mouse[0]<615 and 345<mouse[1]<400 and abrir==11 and guta<9:
        guta=guta+1
        print("ge")
        if guta==1 and cena==0:
            alfaL=230
            betaL=240
            lixta=lixta+letra8
        if guta==2 and cena==0:
            alfaL=285
            betaL=240
            lixta=lixta+letra8
        if guta==3 and cena==0:
            alfaL=340
            betaL=240
            lixta=lixta+letra8
        if guta==4 and cena==0:
            alfaL=395
            betaL=240
            lixta=lixta+letra8
        if guta==5 and cena==0:
            alfaL=450
            betaL=240
            lixta=lixta+letra8
        if guta==6 and cena==0:
            alfaL=505
            betaL=240
            lixta=lixta+letra8
        if guta==7 and cena==0:
            alfaL=560
            betaL=240
            lixta=lixta+letra8
        if guta==1 and cena==1:
            alfaO2=230
            betaO2=240
            lixta=lixta+letra8
        if guta==2 and cena==1:
            alfaO2=285
            betaO2=240
            lixta=lixta+letra8
        if guta==3 and cena==1:
            alfaO2=340
            betaO2=240
            lixta=lixta+letra8
        if guta==4 and cena==1:
            alfaO2=395
            betaO2=240
            lixta=lixta+letra8
        if guta==5 and cena==1:
            alfaO2=450
            betaO2=240
            lixta=lixta+letra8
        if guta==6 and cena==1:
            alfaO2=505
            betaO2=240
            lixta=lixta+letra8
        if guta==7 and cena==1:
            alfaO2=560
            betaO2=240
            lixta=lixta+letra8
        if guta==1 and cena==2:
            alfaA=230
            betaA=240
            lixta=lixta+letra8
        if guta==2 and cena==2:
            alfaA=285
            betaA=240
            lixta=lixta+letra8
        if guta==3 and cena==2:
            alfaA=340
            betaA=240
            lixta=lixta+letra8
        if guta==4 and cena==2:
            alfaA=395
            betaA=240
            lixta=lixta+letra8
        if guta==5 and cena==2:
            alfaA=450
            betaA=240
            lixta=lixta+letra8
        if guta==6 and cena==2:
            alfaA=505
            betaA=240
            lixta=lixta+letra8
        if guta==7 and cena==2:
            alfaA=560
            betaA=240
            lixta=lixta+letra8
        if guta==8 and cena==2:
            lixta=lixta+letra8
        if guta==1 and cena==3:
            alfaO2=230
            betaO2=240
            lixta=lixta+letra8
        if guta==2 and cena==3:
            alfaO2=285
            betaO2=240
            lixta=lixta+letra8
        if guta==3 and cena==3:
            alfaO2=340
            betaO2=240
            lixta=lixta+letra8
        if guta==4 and cena==3:
            alfaO2=395
            betaO2=240
            lixta=lixta+letra8
        if guta==5 and cena==3:
            alfaO2=450
            betaO2=240
            lixta=lixta+letra8
        if guta==6 and cena==3:
            alfaO2=505
            betaO2=240
            lixta=lixta+letra8
        if guta==7 and cena==3:
            alfaO2=560
            betaO2=240
            lixta=lixta+letra8
        if guta==1 and cena==4:
            alfaG=230
            betaG=240
            lixta=lixta+letra8
        if guta==2 and cena==4:
            alfaG=285
            betaG=240
            lixta=lixta+letra8
        if guta==3 and cena==4:
            alfaG=340
            betaG=240
            lixta=lixta+letra8
        if guta==4 and cena==4:
            alfaG=395
            betaG=240
            lixta=lixta+letra8
        if guta==5 and cena==4:
            alfaG=450
            betaG=240
            lixta=lixta+letra8
        if guta==6 and cena==4:
            alfaG=505
            betaG=240
            lixta=lixta+letra8
        if guta==7 and cena==4:
            alfaG=560
            betaG=240
            lixta=lixta+letra8
        if guta==1 and cena==5:
            alfaM=230
            betaM=240
            lixta=lixta+letra8
        if guta==2 and cena==5:
            alfaM=285
            betaM=240
            lixta=lixta+letra8
        if guta==3 and cena==5:
            alfaM=340
            betaM=240
            lixta=lixta+letra8
        if guta==4 and cena==5:
            alfaM=395
            betaM=240
            lixta=lixta+letra8
        if guta==5 and cena==5:
            alfaM=450
            betaM=240
            lixta=lixta+letra8
        if guta==6 and cena==5:
            alfaM=505
            betaM=240
            lixta=lixta+letra8
        if guta==7 and cena==5:
            alfaM=560
            betaM=240
            lixta=lixta+letra8
        if guta==1 and cena==6:
            alfaP=230
            betaP=240
            lixta=lixta+letra8
        if guta==2 and cena==6:
            alfaP=285
            betaP=240
            lixta=lixta+letra8
        if guta==3 and cena==6:
            alfaP=340
            betaP=240
            lixta=lixta+letra8
        if guta==4 and cena==6:
            alfaP=395
            betaP=240
            lixta=lixta+letra8
        if guta==5 and cena==6:
            alfaP=450
            betaP=240
            lixta=lixta+letra8
        if guta==6 and cena==6:
            alfaP=505
            betaP=240
            lixta=lixta+letra8
        if guta==7 and cena==6:
            alfaP=560
            betaP=240
            lixta=lixta+letra8
        if guta==1 and cena==7:
            alfaH=230
            betaH=240
            lixta=lixta+letra8
        if guta==2 and cena==7:
            alfaH=285
            betaH=240
            lixta=lixta+letra8
        if guta==3 and cena==7:
            alfaH=340
            betaH=240
            lixta=lixta+letra8
        if guta==4 and cena==7:
            alfaH=395
            betaH=240
            lixta=lixta+letra8
        if guta==5 and cena==7:
            alfaH=450
            betaH=240
            lixta=lixta+letra8
        if guta==6 and cena==7:
            alfaH=505
            betaH=240
            lixta=lixta+letra8
        if guta==7 and cena==7:
            alfaH=560
            betaH=240
            lixta=lixta+letra8
    if cena==0 and guta==7:
        if lixta=="GALINHA":
            print("acertou")
            epa=True
            guta=0
            lixta=""
            abrir=1
            cena=abrir
        else:
            alfaA=85
            alfaG=155
            alfaA2=225
            alfaU=295
            alfaH=365
            alfaN=435
            alfaI=500
            alfaL=565
            lixta=""
            guta=0
            betaA=350
            betaG=350
            betaA2=350
            betaU=350
            betaH=350
            betaN=350
            betaI=350
            betaL=350
    if cena==1 and guta==5:
        if lixta=="PORCO":
            print("acertou")
            epa=True
            guta=0
            lixta=""
            abrir=2
            cena=abrir
        else:
            alfaP=85
            alfaO=155
            alfaI=225
            alfaL=295
            alfaR=435
            alfaC=365
            alfaN=500
            alfaO2=565
            lixta=""
            guta=0
            betaP=350
            betaO=350
            betaI=350
            betaL=350
            betaR=350
            betaC=350
            betaN=350
            betaO2=350
    if cena==2 and guta==8:
        if lixta=="CACHORRO":
            print("acertou")
            epa=True
            guta=0
            lixta=""
            abrir=3
            cena=abrir
        else:
            alfaR=85
            alfaH=155
            alfaO2=225
            alfaC=295
            alfaC2=365
            alfaR2=435
            alfaO=500
            alfaA=565
            lixta=""
            guta=0
            betaC=350
            betaA=350
            betaC2=350
            betaH=350
            betaO2=350
            betaR=350
            betaR2=350
            betaO=350
    if cena==3 and guta==4:    
        if lixta=="RATO":
            print("acertou")
            epa=True
            guta=0
            lixta=""
            abrir=4
            cena=abrir
        else:
            alfaA2=85
            alfaO=155
            alfaA=225
            alfaR=295
            alfaU=365
            alfaG=435
            alfaT=500
            alfaO2=565
            betaA2=350
            betaO=350
            betaA=350
            betaR=350
            betaU=350
            betaG=350
            betaT=350
            betaO2=350
            lixta=""
            guta=0
    if cena==4 and guta==4:    
        if lixta=="GATO":
            print("acertou")
            epa=True
            guta=0
            lixta=""
            abrir=5
            cena=abrir
        else:
            alfaT=85
            alfaR=155
            alfaR2=225
            alfaU=295
            alfaA=365
            alfaL=435
            alfaO=500
            alfaG=565
            betaT=350
            betaR=350
            betaR2=350
            betaU=350
            betaA=350
            betaL=350
            betaO=350
            betaG=350
            lixta=""
            guta=0            
    if cena==5 and guta==7:    
        if lixta=="PINGUIM":
            print("acertou")
            epa=True
            guta=0
            lixta=""
            abrir=6
            cena=abrir
        else:
            alfaU=85
            alfaT=155
            alfaN=225
            alfaP=295
            alfaG=365
            alfaI=435
            alfaI2=500
            alfaM=565
            betaU=350
            betaT=350
            betaN=350
            betaP=350
            betaG=350
            betaI=350
            betaI2=350
            betaM=350
            lixta=""
            guta=0   
    if cena==6 and guta==4:    
        if lixta=="PATO":
            print("acertou")
            epa=True
            guta=0
            lixta=""
            abrir=7
            cena=abrir
        else:
            alfaT=85
            alfaU=155
            alfaA=225
            alfaR=295
            alfaG=365
            alfaI=435
            alfaO=500
            alfaP=565
            betaT=350
            betaU=350
            betaA=350
            betaR=350
            betaG=350
            betaI=350
            betaO=350
            betaP=350
            lixta=""
            guta=0
    if cena==7 and guta==6:    
        if lixta=="ABELHA":
            print("acertou")
            epa=True
            guta=0
            lixta=""
            abrir=0
            cena=abrir
        else:
            alfaM=85
            alfaA2=155
            alfaA=225
            alfaR=295
            alfaB=365
            alfaL=435
            alfaE=500
            alfaH=565
            betaM=350
            betaA2=350
            betaA=350
            betaR=350
            betaB=350
            betaL=350
            betaE=350
            betaH=350
            lixta=""
            guta=0                              
#=========================================================================jogo da matematica=====================================================================#
    comando=pygame.key.get_pressed()
    if comando[pygame.K_SPACE] and lk==10:
        confere1=-600
        confere2=-600
        alfamate=-600
        betamate=-600
        if ok==True:
            numeros.tirar()
            ok=False
        nt1=random.randint(0,9)
        nt2=random.randint(0,9)
        nt3=random.randint(0,2)
        numeros.adicionar()
        numeros1.adicionar(trocs1,trocs2)
        sinal.adicionar()
        print(nt3)
        print(nt1,"esse")
        if nt3==0:
            resultado=nt1+nt2
        if nt3==1:
            resultado=nt1-nt2
        if nt3==2:
            resultado=nt1*nt2
        print (resultado)            
        print("leite")
        resultado1=str(resultado)
        if len(resultado1)==2:
            gaga=0
            lk=11
        else:
            lk=11
            gaga=1

    #print("g",pygame.mouse.get_pos())            
    if event.type==pygame.MOUSEBUTTONDOWN and 160<mouse[0]<205 and 425<mouse[1]<485 and gaga<2:
        errado1=-600
        errado2=-600
        
        resposta=resposta + "1"
        gaga=gaga+1
        print("1")
    if event.type==pygame.MOUSEBUTTONDOWN and 225<mouse[0]<276 and 425<mouse[1]<485 and gaga<2:
        errado1=-600
        errado2=-600
        
        resposta=resposta + "2"
        gaga=gaga+1
        print("2")
    if event.type==pygame.MOUSEBUTTONDOWN and 295<mouse[0]<340 and 425<mouse[1]<485 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "3"
        gaga=gaga+1
        print("3")
    if event.type==pygame.MOUSEBUTTONDOWN and 160<mouse[0]<205 and 407>mouse[1]>345 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "4"
        gaga=gaga+1
        print("4")
    if event.type==pygame.MOUSEBUTTONDOWN and 225<mouse[0]<278 and 407>mouse[1]>345 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "5"
        gaga=gaga+1
        print("5")
    if event.type==pygame.MOUSEBUTTONDOWN and 295<mouse[0]<340 and 407>mouse[1]>345 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "6"
        gaga=gaga+1
        print("6")
    if event.type==pygame.MOUSEBUTTONDOWN and 160<mouse[0]<205 and 325>mouse[1]>265 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "7"
        gaga=gaga+1
        print("7")
    if event.type==pygame.MOUSEBUTTONDOWN and 225<mouse[0]<276 and 325>mouse[1]>265 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "8"
        gaga=gaga+1
        print("8")
    if event.type==pygame.MOUSEBUTTONDOWN and 295<mouse[0]<340 and 325>mouse[1]>265 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "9"
        gaga=gaga+1
        print("9")
    if event.type==pygame.MOUSEBUTTONDOWN and 160<mouse[0]<205 and 570>mouse[1]>505 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "-"
        gaga=gaga+1
        print("-")
    if event.type==pygame.MOUSEBUTTONDOWN and 225<mouse[0]<276 and 570>mouse[1]>505 and gaga<2:
        
        errado1=-600
        errado2=-600
        resposta=resposta + "0"
        gaga=gaga+1
        print("0")                
    if resposta==resultado1:
        print("acertou")
        resposta=""
        ok=True
        nt1=10
        numeros.adicionar()
        nt3=3
        sinal.adicionar()
        nt2=10
        numeros1.adicionar(trocs1, trocs2)
        confere1=500
        confere2=250
        alfamate=-600
        betamate=-600
        ulti=1000
        lk=10
    if resposta!=resultado1 and resposta!="" and gaga==2:
        print("errou")
        resposta=""
        errado1=500
        errado2=250
        ulti=1000
        tim=3
        lk=11
        if len(resultado1)==2:
            print(lk)
            lk=11
            gaga=0
        else:
            lk=11
            gaga=1


        
        


    #print("g",pygame.mouse.get_pos())
#============================================================================jogo da musica=============================================#
    comando=pygame.key.get_pressed()
    if comando[pygame.K_SPACE] and volte==True and jo==3:
            jj=1
            deu=0
            j=0  
            volte=False
            ll=random.randint(1,8)
            pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
            print(ll)


    if ll==1 and event.type == pygame.USEREVENT+jj and deu<5:
        vetorrosa.diminuir()
        vetorrosa_group.update()
        vetorrosa_group.draw(BACKGROUND)
        fm.append(ll)
        cm=ll
        print(ll,"rosa")
        print(fm)
        jj=jj+1
        pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
        deu=deu+1
        tomada=True
        audio1.play()
    elif cm==1 and tomada==True:
        vetorrosa.aumentar()
        vetorrosa_group.update()
        vetorrosa_group.draw(BACKGROUND)
        print("leite com cafe")
        tomada=False
        jj1=jj1+1
        ll=random.randint(1,8)
    if ll==2 and event.type == pygame.USEREVENT+jj and deu<5:
        vetorazul.diminuir()
        vetorazul_group.update()
        vetorazul_group.draw(BACKGROUND)
        fm.append(ll)
        cm=ll
        print(ll,'azul')
        print(fm)
        jj=jj+1
        pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
        deu=deu+1
        tomada=True
        audio2.play()
    elif cm==2 and tomada==True:
        vetorazul.aumentar()
        vetorazul_group.update()
        vetorazul_group.draw(BACKGROUND)
        print("leite com cafe")
        tomada=False
        jj1=jj1+1
        ll=random.randint(1,8)
    if ll==3 and event.type == pygame.USEREVENT+jj and deu<5:
        vetormarinho.diminuir()
        vetormarinho_group.update()
        vetormarinho_group.draw(BACKGROUND)
        fm.append(ll)
        cm=ll
        print(ll,'marinho')
        print(fm)
        jj=jj+1
        pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
        deu=deu+1
        tomada=True
        audio3.play()
    elif cm==3 and tomada==True:
        vetormarinho.aumentar()
        vetormarinho_group.update()
        vetormarinho_group.draw(BACKGROUND)
        print("leite com cafe")
        tomada=False
        jj1=jj1+1
        ll=random.randint(1,8)
    if ll==4 and event.type == pygame.USEREVENT+jj and deu<5:
        vetorvermelho.diminuir()
        vetorvermelho_group.update()
        vetorvermelho_group.draw(BACKGROUND)
        fm.append(ll)
        cm=ll
        print(ll,'vermelho')
        print(fm)
        jj=jj+1
        pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
        deu=deu+1
        tomada=True
        audio4.play()
    elif cm==4 and tomada==True:
        vetorvermelho.aumentar()
        vetorvermelho_group.update()
        vetorvermelho_group.draw(BACKGROUND)
        print("leite com cafe")
        tomada=False
        jj1=jj1+1
        ll=random.randint(1,8)
    if ll==5 and event.type == pygame.USEREVENT+jj and deu<5:
        vetorlaranja.diminuir()
        vetorlaranja_group.update()
        vetorlaranja_group.draw(BACKGROUND)
        fm.append(ll)
        cm=ll
        print(ll,'vermelho')
        print(fm)
        jj=jj+1
        pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
        deu=deu+1
        tomada=True
        audio5.play()
    elif cm==5 and tomada==True:
        vetorlaranja.aumentar()
        vetorlaranja_group.update()
        vetorlaranja_group.draw(BACKGROUND)
        print("leite com cafe")
        tomada=False
        jj1=jj1+1
        ll=random.randint(1,8)
    if ll==6 and event.type == pygame.USEREVENT+jj and deu<5:
        vetoramarelo.diminuir()
        vetoramarelo_group.update()
        vetoramarelo_group.draw(BACKGROUND)
        fm.append(ll)
        cm=ll
        print(ll,'vermelho')
        print(fm)
        jj=jj+1
        pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
        deu=deu+1
        tomada=True
        audio6.play()
    elif cm==6 and tomada==True:
        vetoramarelo.aumentar()
        vetoramarelo_group.update()
        vetoramarelo_group.draw(BACKGROUND)
        print("leite com cafe")
        tomada=False
        jj1=jj1+1
        ll=random.randint(1,8)
    if ll==7 and event.type == pygame.USEREVENT+jj and deu<5:
        vetorroxo.diminuir()
        vetorroxo_group.update()
        vetorroxo_group.draw(BACKGROUND)
        fm.append(ll)
        cm=ll
        print(ll,'vermelho')
        print(fm)
        jj=jj+1
        pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
        deu=deu+1
        tomada=True
        audio7.play()
    elif cm==7 and tomada==True:
        vetorroxo.aumentar()
        vetorroxo_group.update()
        vetorroxo_group.draw(BACKGROUND)
        print("leite com cafe")
        tomada=False
        jj1=jj1+1
        ll=random.randint(1,8)
    if ll==8 and event.type == pygame.USEREVENT+jj and deu<5:
        vetormarrom.diminuir()
        vetormarrom_group.update()
        vetormarrom_group.draw(BACKGROUND)
        fm.append(ll)
        cm=ll
        print(ll,'vermelho')
        print(fm)
        jj=jj+1
        pygame.time.set_timer(pygame.USEREVENT+jj, 2000)
        deu=deu+1
        tomada=True
        audio8.play()
    elif cm==8 and tomada==True:
        vetormarrom.aumentar()
        vetormarrom_group.update()
        vetormarrom_group.draw(BACKGROUND)
        print("leite com cafe")
        tomada=False
        jj1=jj1+1
        ll=random.randint(1,8)
    ###############################################################################################                            
    
    if deu==5:
        na=1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        deu=6
        lm=0

    ########################################################################################################
    if event.type==pygame.MOUSEBUTTONDOWN and 50<mouse[0]<230 and 30<mouse[1]<90 and lm==0 and j<5: 
        f1.append(1)
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        j=j+1
        print(f1)
        audio1.play()
    if event.type==pygame.MOUSEBUTTONDOWN and 317<mouse[0]<500 and 30<mouse[1]<90 and lm==0 and j<5: 
        f1.append(3)
        j=j+1
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print(f1)
        audio3.play()
    if event.type==pygame.MOUSEBUTTONDOWN and 50<mouse[0]<230 and 148<mouse[1]<205 and lm==0 and j<5: 
        f1.append(4)
        j=j+1
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print(f1)
        audio4.play()
    if event.type==pygame.MOUSEBUTTONDOWN and 317<mouse[0]<500 and 148<mouse[1]<205 and lm==0 and j<5: 
        f1.append(2)
        j=j+1
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print(f1)
        audio2.play()
    if event.type==pygame.MOUSEBUTTONDOWN and 50<mouse[0]<230 and 265<mouse[1]<322 and lm==0 and j<5: 
        f1.append(5)
        j=j+1
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print(f1)
        audio5.play()
    if event.type==pygame.MOUSEBUTTONDOWN and 50<mouse[0]<230 and 385<mouse[1]<445 and lm==0 and j<5: 
        f1.append(6)
        j=j+1
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print(f1)
        audio6.play()
    if event.type==pygame.MOUSEBUTTONDOWN and 317<mouse[0]<500 and 265<mouse[1]<322 and lm==0 and j<5: 
        f1.append(7)
        j=j+1
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print(f1)
        audio7.play()
    if event.type==pygame.MOUSEBUTTONDOWN and 317<mouse[0]<500 and 385<mouse[1]<445 and lm==0 and j<5: 
        f1.append(8)
        j=j+1
        na=na+1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print(f1)
        audio8.play()
    ########################################################################################################                    
    
    if f1==fm and j==5:
        print("acertoumizeravi")
        na=-1
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        j=7
        volte=True
        fm=[]
        f1=[]
        lm=1
        pygame.time.set_timer(pygame.USEREVENT+1, 2000)
    elif j==7 and event.type == pygame.USEREVENT+1:
        na=9
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print("legal")
        deu=0
        ll=9
        j=500
    if f1!=fm and j==5:
        print("erroumizeravi")
        na=0
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        fm=[]
        f1=[]
        j=6
        lm=1
        volte=True
        pygame.time.set_timer(pygame.USEREVENT+1, 2000)
    elif j==6 and event.type == pygame.USEREVENT+1:
        na=9
        acertou.adicionar()
        acertou_group.update()
        acertou_group.draw(BACKGROUND)
        print("legal1")
        deu=0
        ll=9
        j=500
    #####################################################################################    
    dançando_group.update()
    dançando_group.draw(BACKGROUND)               
    balão_group.update()
    balão_group.draw(BACKGROUND)
    numeros1_group.update()
    numeros1_group.draw(BACKGROUND)
    sinal_group.update()
    sinal_group.draw(BACKGROUND)
    numeros_group.update()
    numeros_group.draw(BACKGROUND)
    screen.blit(BACKGROUND,(0,0))
    screen.blit(letraP,(alfaP,betaP))
    screen.blit(letraT,(alfaT,betaT))
    screen.blit(letraO,(alfaO,betaO))
    screen.blit(letraC,(alfaC,betaC))
    screen.blit(letraC,(alfaC2,betaC2))
    screen.blit(letraO2,(alfaO2,betaO2))
    screen.blit(letraR,(alfaR,betaR))
    screen.blit(letraR,(alfaR2,betaR2))
    screen.blit(letraA,(alfaA,betaA))
    screen.blit(letraG,(alfaG,betaG))
    screen.blit(letraA2,(alfaA2,betaA2))
    screen.blit(letraU,(alfaU,betaU))
    screen.blit(letraH,(alfaH,betaH))
    screen.blit(letraN,(alfaN,betaN))
    screen.blit(letraM,(alfaM,betaM))
    screen.blit(letraI,(alfaI,betaI))
    screen.blit(letraI2,(alfaI2,betaI2))
    screen.blit(letraL,(alfaL,betaL))
    screen.blit(letraB,(alfaB,betaB))
    screen.blit(letraE,(alfaE,betaE))
    screen.blit(iconemusica,(a,b))
    screen.blit(animal,(aaaa,bbbb))
    screen.blit(iconepor,(aaa,bbb))
    screen.blit(iconematematica,(aa,bb))
    screen.blit(OZZY,(X,Y))
    screen.blit(calculadora,(tio,tia))
    screen.blit(confere,(confere1,confere2))
    screen.blit(errado,(errado1,errado2))
    screen.blit(balãopor,(alfapor,betapor))
    screen.blit(balãomate,(alfamate,betamate))
    pygame.display.update()


