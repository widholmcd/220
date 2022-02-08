"""
Name: Calvin Widholm
lab4.py

Problem: Making a greeting card and making it look nice

Certification of Authenticity:
I certify that this assignment is entirely my own work.- Calvin Widholm- I certify
"""
import time
from graphics import Circle, Polygon, Rectangle, Text, GraphWin, Point, Line



def greeting_card():

   heart = Polygon(Point(90.0, 379.0), Point(97.0, 337.0), Point(120.0, 309.0), Point(148.0, 272.0),
                   Point(171.0, 243.0), Point(194.0, 215.0), Point(248.0, 232.0), Point(282.0, 267.0),
                   Point(306.0, 309.0), Point(336.0, 275.0), Point(370.0, 221.0), Point(419.0, 189.0),
                   Point(456.0, 215.0), Point(480.0, 261.0), Point(492.0, 301.0), Point(500.0, 351.0),
                   Point(474.0, 401.0), Point(436.0, 451.0), Point(395.0, 488.0), Point(352.0, 530.0),
                   Point(314.0, 569.0), Point(297.0, 552.0), Point(270.0, 534.0), Point(237.0, 511.0),
                   Point(209.0, 487.0), Point(175.0, 450.0), Point(150.0, 425.0), Point(125.0, 400.0),
                   Point(100.0, 385.0), Point(90.0, 382.0))
   win = GraphWin("Greeting Card", 700, 700)
   heart.setFill("red")
   heart.draw(win)

   point_a = Point(100, 50)
   point_b = Point(600, 50)
   banner_line_a = Line((Point(0, 0)), point_a)
   banner_line_b = Line((Point(700, 0)), point_b)
   banner_line_a.draw(win)
   banner_line_b.draw(win)
   banner = Rectangle(Point(100, 100), point_b)
   banner.draw(win)



   greeting_text = Text(Point(350, 75), "Happy Valentines Day!!!")
   greeting_text.draw(win)

   mini_heart_a = Polygon(Point(480.0, 74.0), Point(483.0, 69.0), Point(487.0, 65.0), Point(493.0, 66.0),
                          Point(499.0, 72.0), Point(504.0, 67.0), Point(507.0, 64.0), Point(512.0, 69.0),
                          Point(515.0, 78.0), Point(511.0, 84.0), Point(502.0, 88.0), Point(491.0, 84.0),
                          Point(484.0, 79.0))
   mini_heart_a.setFill("red")
   mini_heart_a.draw(win)

   mini_heart_b = Polygon(Point(525, 74.0), Point(528, 69.0), Point(532.0, 65.0), Point(538, 66.0),
                          Point(544.0, 72.0), Point(549.0, 67.0), Point(552.0, 64.0), Point(557.0, 69.0),
                          Point(560.0, 78.0), Point(556.0, 84.0), Point(547.0, 88.0), Point(536.0, 84.0),
                          Point(529.0, 79.0))
   mini_heart_b.setFill("red")
   mini_heart_b.draw(win)

   mini_heart_c = Polygon(Point(200.0, 71.0), Point(205.0, 67.0), Point(211.0, 64.0), Point(220.0, 70.0),
                          Point(227.0, 63.0), Point(234.0, 65.0), Point(241.0, 72.0), Point(241.0, 80.0),
                          Point(236.0, 88.0), Point(227.0, 90.0), Point(219.0, 85.0), Point(212.0, 81.0),
                          Point(206.0, 77.0))
   mini_heart_c.setFill("red")
   mini_heart_c.draw(win)

   mini_heart_d = Polygon(Point(155.0, 71.0), Point(160.0, 67.0), Point(166.0, 64.0), Point(175.0, 70.0),
                          Point(182.0, 63.0), Point(189.0, 65.0), Point(196.0, 72.0), Point(196.0, 80.0),
                          Point(191.0, 88.0), Point(182.0, 90.0), Point(174.0, 85.0), Point(167.0, 81.0),
                          Point(161.0, 77.0))
   mini_heart_d.setFill("red")
   mini_heart_d.draw(win)

   chocolate = Rectangle(Point(450, 650), Point(650, 550))
   chocolate.setFill("red")
   chocolate_text = Text(Point(550, 600), "Chocolate")
   chocolate.draw(win)
   chocolate_text.draw(win)



   arrow = Polygon(Point(237.0, 429.0), Point(244.0, 466.0), Point(232.0, 461.0), Point(221.0, 474.0),
                   Point(210.0, 489.0), Point(199.0, 501.0), Point(187.0, 515.0), Point(176.0, 525.0),
                   Point(163.0, 536.0), Point(154.0, 547.0), Point(140.0, 558.0), Point(122.0, 571.0),
                   Point(106.0, 582.0), Point(90.0, 592.0), Point(86.0, 610.0), Point(73.0, 623.0),
                   Point(48.0, 642.0), Point(32.0, 633.0), Point(26.0, 624.0), Point(15.0, 612.0),
                   Point(26.0, 602.0), Point(42.0, 597.0), Point(51.0, 587.0), Point(65.0, 592.0),
                   Point(81.0, 582.0), Point(95.0, 575.0), Point(113.0, 560.0), Point(122.0, 547.0),
                   Point(137.0, 536.0), Point(151.0, 526.0), Point(162.0, 517.0), Point(175.0, 505.0),
                   Point(186.0, 496.0), Point(194.0, 485.0), Point(201.0, 472.0), Point(206.0, 462.0),
                   Point(189.0, 452.0), Point(210.0, 444.0), Point(222.0, 440.0))
   arrow.setFill("gray")
   arrow.move(-250, 250)
   arrow.draw(win)

   for _ in range(90):
       arrow.move(10, -10)
       time.sleep(.1)

   closing_remark = Text(Point(350, 650), "Click to close")
   closing_remark.draw(win)


   win.getMouse()
   win.close()
