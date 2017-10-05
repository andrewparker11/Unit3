#Andrew Parker
#10/5/17
#dotsDemo.py - Making some dots

from ggame import * 

red = Color(0xFF0000,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)


blackOutline = LineStyle(1,black) #pixels, color
redRectangle = RectangleAsset(60,10,blackOutline,red) #width, height, outline, fill
blackRectangle = RectangleAsset(60,10,blackOutline,black)
yellowRectangle = RectangleAsset(60,10,blackOutline,yellow)
dot = CircleAsset(20,LineStyle(1,red),red)

for j in range(10):
    for i in range(20):
        Sprite(redRectangle,(20 + 50*i, 20+50*j))
        Sprite(yellowRectangle,(20 + 50*i, 20+50*j))
        Sprite(blackRectangle,(20 + 50*i, 20+50*j)) 

App().run()


#Sprite(dot,(20 + 50*i,20 + 50*j))



