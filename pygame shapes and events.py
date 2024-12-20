import pygame 
pygame.init()
playing = True
screen = pygame.display.set_mode((800,800))
class Circle():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.s = screen
    def display(self):
        pygame.draw.circle(self.s,"blue",(self.x,self.y), self.r,1)
    def grow(self):
        self.r += 10
        pygame.draw.circle(self.s,"blue",(self.x,self.y),self.r,20)
ball1 = Circle(100,100,100)
ball = Circle(100,100,100)        
while playing == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if(event.type == pygame.MOUSEMOTION):
            x,y = pygame.mouse.get_pos()

            new_Circle = Circle(x,y,100) 
            new_Circle.display()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball1.grow()
            pygame.display.update()
    ball.display()
    
    pygame.display.update()