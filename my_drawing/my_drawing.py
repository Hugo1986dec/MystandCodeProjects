"""
File: my_drawing.py
Name:劉映麟
----------------------
TODO:
"""

from campy.graphics.gobjects import GLabel
from campy.graphics.gobjects import GOval, GRect, GLine, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=1000, height=1000, title='Super Mario')
    background = GRect(1200, 1200, x=0, y=0)
    window.add(background)
    background.filled = True
    background.fill_color = "darkblue"
    hat = GRect(150, 50, x=350, y=200)
    window.add(hat)
    hat.filled = True
    hat.fill_color = "red"
    hat1 = GRect(325, 50, x=300, y=250)
    window.add(hat1)
    hat1.filled = True
    hat1.fill_color = "red"
    # 消除紅色長方形間的黑線
    line = GLine(350, 250, 500, 250)
    window.add(line)
    line.color = "red"
    face = GRect(325, 250, x=300, y=300)
    window.add(face)
    face.filled = True
    face.fill_color = "orange"
    # 臉部輪廓
    space1 = GRect(90, 50, x=535, y=300)
    window.add(space1)
    face.filled = True
    space1.fill_color = "darkblue"
    # 消除底色線
    line2 = GLine(625, 300, 625, 350)
    window.add(line2)
    line2.color = "darkblue"
    #   鼻子
    nose = GRect(50, 50, x=625, y=400)
    window.add(nose)
    nose.filled = True
    nose.fill_color = "orange"
    #   消除鼻子底色線
    line3 = GLine(625, 400, 625, 450)
    window.add(line3)
    line3.color = "orange"
    # 鬍子1
    beard1 = GRect(175, 50, x=450, y=450)
    window.add(beard1)
    beard1.filled = True
    beard1.fill_color = "saddlebrown"
    # 鬍子2
    beard2 = GRect(35, 50, x=500, y=400)
    window.add(beard2)
    beard2.filled = True
    beard2.fill_color = "saddlebrown"
    # 消除鬍子底色線
    line4 = GLine(500, 450, 535, 450)
    window.add(line4)
    line4.color = "saddlebrown"
    # 眼睛
    eye = GRect(50, 100, x=450, y=300)
    window.add(eye)
    eye.filled = True
    eye.fill_color = "saddlebrown"
    #   頭髮1
    hair1 = GRect(75, 50, x=300, y=300)
    window.add(hair1)
    hair1.filled = True
    hair1.fill_color = "saddlebrown"
    #   頭髮2
    hair2 = GRect(25, 100, x=325, y=350)
    window.add(hair2)
    hair2.filled = True
    hair2.fill_color = "saddlebrown"
    #   頭髮3
    hair3 = GRect(25, 25, x=350, y=425)
    window.add(hair3)
    hair3.filled = True
    hair3.fill_color = "saddlebrown"
    #   頭髮4
    hair4 = GRect(50, 140, x=250, y=350)
    window.add(hair4)
    hair4.filled = True
    hair4.fill_color = "saddlebrown"
    #   頭髮5
    hair5 = GRect(25, 40, x=300, y=450)
    window.add(hair5)
    hair5.filled = True
    hair5.fill_color = "saddlebrown"
    # 消除頭髮1底色線
    line5 = GLine(325, 350, 375, 350)
    window.add(line5)
    line5.color = "saddlebrown"
    # 消除頭髮2底色線
    line6 = GLine(350, 425, 350, 450)
    window.add(line6)
    line6.color = "saddlebrown"
    # 消除頭髮4底色線
    line7 = GLine(300, 450, 300, 490)
    window.add(line7)
    line7.color = "saddlebrown"
    # 脖子
    neck = GRect(25, 60, x=300, y=490)
    window.add(neck)
    neck.filled = True
    neck.fill_color = "darkblue"
    # 消除脖子底色線1
    line8 = GLine(300, 490, 300, 550)
    window.add(line8)
    line8.color = "darkblue"
    # 消除脖子底色線2
    line9 = GLine(300, 550, 325, 550)
    window.add(line9)
    line9.color = "darkblue"
    # 嘴巴
    mouth = GRect(45, 60, x=580, y=490)
    window.add(mouth)
    mouth.filled = True
    mouth.fill_color = "darkblue"
    # 消除嘴巴底色線1
    line10 = GLine(580, 550, 625, 550)
    window.add(line10)
    line10.color = "darkblue"
    # 消除底色線2
    line11 = GLine(625, 490, 625, 550)
    window.add(line11)
    line11.color = "darkblue"
    # 身體
    body = GRect(480, 300, x=200, y=550)
    window.add(body)
    body.filled = True
    body.fill_color = "saddlebrown"
    # 背景2
    background1 = GRect(75, 50, x=200, y=550)
    window.add(background1)
    background1.filled = True
    background1.fill_color = "darkblue"
    # 背景3
    background2 = GRect(37.5, 100, x=200, y=550)
    window.add(background2)
    background2.filled = True
    background2.fill_color = "darkblue"
    # 消除身體底色線1
    line11 = GLine(200, 550, 275, 550)
    window.add(line11)
    line11.color = "darkblue"
    # 消除身體底色線2
    line12 = GLine(200, 550, 200, 650)
    window.add(line12)
    line12.color = "darkblue"
    # 消除身體底色線3
    line13 = GLine(237.5, 550, 237.5, 600)
    window.add(line13)
    line13.color = "darkblue"
    # 右手
    right_arm = GRect(75, 150, x=200, y=700)
    window.add(right_arm)
    right_arm.filled = True
    right_arm.fill_color = "orange"
    # 右手
    right_hand = GRect(37.5, 50, x=275, y=750)
    window.add(right_hand)
    right_hand.filled = True
    right_hand.fill_color = "orange"
    # 左手
    left_arm = GRect(80, 150, x=600, y=700)
    window.add(left_arm)
    left_arm.filled = True
    left_arm.fill_color = "orange"
    # 左手
    left_hand = GRect(37.5, 50, x=562.5, y=750)
    window.add(left_hand)
    left_hand.filled = True
    left_hand.fill_color = "orange"

    # 消除手臂線
    line14 = GLine(275, 750, 275, 800)
    window.add(line14)
    line14.color = "orange"
    # 消除手臂線
    line15 = GLine(600, 750, 600, 800)
    window.add(line15)
    line15.color = "orange"
    # 褲子
    pants1 = GRect(325, 100, x=275, y=800)
    window.add(pants1)
    pants1.filled = True
    pants1.fill_color = "red"
    # 褲子2
    pants2 = GRect(250, 50, x=312.5, y=750)
    window.add(pants2)
    pants2.filled = True
    pants2.fill_color = "red"
    # 褲子3
    pants3 = GRect(250, 50, x=312.5, y=700)
    window.add(pants3)
    pants3.filled = True
    pants3.fill_color = "red"
    # 消除褲子線1
    line17 = GLine(312.5, 800, 562.5, 800)
    window.add(line17)
    line17.color = "red"
    # 消除褲子線2
    line18 = GLine(312.5, 750, 562.5, 750)
    window.add(line18)
    line18.color = "red"
    #   鈕扣1
    button1 = GRect(50, 50, x=362.5, y=700)
    window.add(button1)
    button1.filled = True
    button1.fill_color = "orange"
    #   鈕扣2
    button2 = GRect(50, 50, x=462.5, y=700)
    window.add(button2)
    button2.filled = True
    button2.fill_color = "orange"
    #   吊帶1
    suspenders1 = GRect(50, 150, x=362.5, y=550)
    window.add(suspenders1)
    suspenders1.filled = True
    suspenders1.fill_color = "red"
    #   吊帶2
    suspenders2 = GRect(50, 100, x=462.5, y=600)
    window.add(suspenders2)
    suspenders2.filled = True
    suspenders2.fill_color = "red"
    # 消除吊帶線
    line19 = GLine(312.5, 700, 562.5, 700)
    window.add(line19)
    line19.color = "red"
    # 胯下
    crotch = GRect(125, 50, x=375, y=850)
    window.add(crotch)
    crotch.filled = True
    crotch.fill_color = "darkblue"
    # 消除胯下線
    line16 = GLine(375, 900, 500, 900)
    window.add(line16)
    line16.color = "darkblue"
    # 肩膀1
    shoulder1 = GRect(167.5, 50, x=512.5, y=550)
    window.add(shoulder1)
    shoulder1.filled = True
    shoulder1.fill_color = "darkblue"
    # 肩膀2
    shoulder2 = GRect(50, 50, x=630, y=600)
    window.add(shoulder2)
    shoulder2.filled = True
    shoulder2.fill_color = "darkblue"
    # 消除肩膀線1
    line20 = GLine(580, 550, 680, 550)
    window.add(line20)
    line20.color = "darkblue"
    # 消除肩膀線2
    line21 = GLine(630, 600, 680, 600)
    window.add(line21)
    line21.color = "darkblue"
    # 消除肩膀線3
    line22 = GLine(680, 500, 680, 900)
    window.add(line22)
    line22.color = "darkblue"
    # 鞋子1
    shoes1 = GRect(150, 80, x=200, y=900)
    window.add(shoes1)
    shoes1.filled = True
    shoes1.fill_color = "saddlebrown"
    # 鞋子2
    shoes2 = GRect(150, 80, x=530, y=900)
    window.add(shoes2)
    shoes2.filled = True
    shoes2.fill_color = "saddlebrown"
    # 鞋頭1
    shoes_head1 = GRect(37.5, 40, x=200, y=900)
    window.add(shoes_head1)
    shoes_head1.filled = True
    shoes_head1.fill_color = "darkblue"
    # 鞋頭2
    shoes_head2 = GRect(37.5, 40, x=642.5, y=900)
    window.add(shoes_head2)
    shoes_head2.filled = True
    shoes_head2.fill_color = "darkblue"
    # 消除鞋頭線1
    line23 = GLine(200, 900, 237.5, 900)
    window.add(line23)
    line23.color = "darkblue"
    # 消除鞋頭線2
    line24 = GLine(200, 900, 200, 940)
    window.add(line24)
    line24.color = "darkblue"
    # 消除鞋頭線3
    line25 = GLine(642.5, 900, 680, 900)
    window.add(line25)
    line25.color = "darkblue"
    # 消除鞋頭線1
    line26 = GLine(680, 900, 680, 940)
    window.add(line26)
    line26.color = "darkblue"

    label1 = GLabel("M", x=730, y=110)
    label1.font = "Times-80-italic"
    label1.color = "green"
    window.add(label1)
    label2 = GLabel("a", x=810, y=110)
    label2.font = "Times-80-italic"
    label2.color = "blue"
    window.add(label2)
    label3 = GLabel("r", x=860, y=110)
    label3.font = "Times-80-italic"
    label3.color = "yellow"
    window.add(label3)
    label4 = GLabel("i", x=900, y=110)
    label4.font = "Times-80-italic"
    label4.color = "red"
    window.add(label4)
    label5 = GLabel("o", x=930, y=110)
    label5.font = "Times-80-italic"
    label5.color = "green"
    window.add(label5)

if __name__ == '__main__':
    main()
