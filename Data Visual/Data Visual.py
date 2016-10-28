from graphics import *
color = color_rgb(115, 108, 108)
def main():
    win = GraphWin("Visualisation", 900, 500)
    
    win.setBackground('grey')
    
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    p4 = win.getMouse()
    p4.draw(win)
    p5 = win.getMouse()
    p5.draw(win)
    p6 = win.getMouse()
    p6.draw(win)
    vertices = [p1, p2, p3, p4 , p5 , p6 ]

    
    dot = Polygon(vertices)
    dot.setFill('color')
    dot.setOutline('cyan')
    dot.setWidth(6)  # width of boundary line
    dot.draw(win)
    
    win.getMouse()
    win.close()
    
main()