from tkinter import mainloop
from graphics import*

#definiçao da minha aba 
def main():


    #tamanho e fundo da aba

    win = GraphWin( "Quiz preparado?" , 1000, 800)
    fundoimg = Image(Point(500,400), "Preparado.png")
    fundoimg.draw(win)

    #Botao

 
    # #botoes do inicio
    while True:
        X = win.getMouse().getX()    #XY = win.getMouse() 
        Y = win.getMouse().getY()
        #botao iniciar
        if (375 < X < 600) and (425 < Y < 535):  
            
            # primeira pergutna
            win.redraw   
            #pergunta
            fundoimg = Image(Point(500,400), "pergt1.png")  
            fundoimg.draw(win)
            #lugar da resposta
            rect = Rectangle(Point(530,335),Point(820,470))
            rect.setFill('navajowhite1')
            #rect.draw(win)
            #botao da resposta pergunta 1
            while True:
                X = win.getMouse().getX()    #XY = win.getMouse() 
                Y = win.getMouse().getY()
        
                #funçao do botao da pergunta 1 
                if (530 < X < 820) and (335 < Y < 470):
                    #pergunta 2
                    fundoimg = Image(Point(500,400), "pergt2.png")
                    fundoimg.draw(win)

                    #lugar da resposta perfunta 2

                    rect = Rectangle(Point(80,375),Point(390,750))
                    rect.setFill('navajowhite1')
                    #rect.draw(win)

                    #botao pergunta 2
                    while True:
                        X = win.getMouse().getX()    #XY = win.getMouse() 
                        Y = win.getMouse().getY()

                        if (80< X < 390) and (375 < Y < 750):

                            #pergunta 3
                            fundoimg = Image(Point(500,400), "pergt3.png")
                            fundoimg.draw(win)
                            
                            #lugar da resposta perfunta 3

                            rect = Rectangle(Point(515,310),Point(800,440))
                            rect.setFill('navajowhite1')
                            #rect.draw(win)
                            while True:
                                X = win.getMouse().getX()    #XY = win.getMouse() 
                                Y = win.getMouse().getY()

                                if (515 < X < 800) and (310 < Y < 440):
                                    #pergunta 4
                                     fundoimg = Image(Point(500,400), "pergt4.png")
                                     fundoimg.draw(win)

                                     rect = Rectangle(Point(180,335),Point(465,470))
                                     rect.setFill('navajowhite1')
                                     #rect.draw(win)

                                     while True:
                                          X = win.getMouse().getX()    #XY = win.getMouse() 
                                          Y = win.getMouse().getY()
                                          if (180 < X < 465) and (335 < Y < 470):
                                             #pergunta 5
                                             fundoimg = Image(Point(500,400), "pergt5.png")
                                             fundoimg.draw(win)
                                             rect = Rectangle(Point(15,20),Point(55,80))
                                             rect.setFill('navajowhite1')
                                             #rect.draw(win)
                                             while True:
                                                 X = win.getMouse().getX()    #XY = win.getMouse() 
                                                 Y = win.getMouse().getY()
                                                 if (15 < X < 55) and (20 < Y < 80):
                                                     #pergunta 6
                                                     fundoimg = Image(Point(500,400), "pergt6.png")
                                                     fundoimg.draw(win)
                                                     rect = Rectangle(Point(375,30),Point(635,300))
                                                     rect.setFill('navajowhite1')
                                                     #rect.draw(win)
                                                     while True:
                                                         X = win.getMouse().getX()    #XY = win.getMouse() 
                                                         Y = win.getMouse().getY()
                                                         if (375 < X < 635) and (30 < Y < 300):
                                                             #pergunta 7
                                                             fundoimg = Image(Point(500,400), "pergt7.png")
                                                             fundoimg.draw(win)  
                                                             rect = Rectangle(Point(180,340),Point(465,480))
                                                             rect.setFill('navajowhite1')
                                                             #rect.draw(win)
                                                             while True:
                                                              X = win.getMouse().getX()    #XY = win.getMouse() 
                                                              Y = win.getMouse().getY()
                                                              if (180 < X < 465) and (340 < Y < 480):
                                                                  #pergunta 8
                                                                  fundoimg = Image(Point(500,400), "pergt8.png")
                                                                  fundoimg.draw(win)
                                                                  rect = Rectangle(Point(180,530),Point(465,660))
                                                                  rect.setFill('navajowhite1')
                                                                  #rect.draw(win)
                                                                  while True:
                                                                    X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                    Y = win.getMouse().getY()
                                                                    if (180 < X < 465) and (180 < Y < 660):
                                                                        #perguta 9
                                                                        fundoimg = Image(Point(500,400), "pergt9.png")
                                                                        fundoimg.draw(win)
                                                                        rect = Rectangle(Point(15,20),Point(67,80))
                                                                        rect.setFill('navajowhite1')
                                                                        #rect.draw(win)
                                                                        while True:
                                                                            X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                            Y = win.getMouse().getY()
                                                                            if (15 < X < 55) and (20 < Y < 80):
                                                                               #pergunta 10
                                                                                fundoimg = Image(Point(500,400), "pergt10.png")
                                                                                fundoimg.draw(win)
                                                                                rect = Rectangle(Point(180,530),Point(465,662))
                                                                                rect.setFill('navajowhite1')
                                                                                #rect.draw(win)
                                                                                while True:
                                                                                    X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                    Y = win.getMouse().getY()
                                                                                    if (180 < X < 465) and (180 < Y < 662):
                                                                                        #pergunta 11
                                                                                        fundoimg = Image(Point(500,400), "pergt11.png")
                                                                                        fundoimg.draw(win)
                                                                                        rect = Rectangle(Point(220,250),Point(285,360))
                                                                                        rect.setFill('navajowhite1')
                                                                                        #rect.draw(win)
                                                                                        while True:
                                                                                            X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                            Y = win.getMouse().getY()
                                                                                            if (220 < X < 285) and (250 < Y < 360):
                                                                                                #pergunta 12
                                                                                                fundoimg = Image(Point(500,400), "pergt12.png")
                                                                                                fundoimg.draw(win)
                                                                                                rect = Rectangle(Point(120,180),Point(360,230))
                                                                                                rect.setFill('navajowhite1')
                                                                                                #rect.draw(win)
                                                                                                while True:
                                                                                                    X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                                    Y = win.getMouse().getY()
                                                                                                    if (120 < X < 360) and (180 < Y < 230):
                                                                                                        #pergunta 13
                                                                                                        fundoimg = Image(Point(500,400), "pergt13.png")
                                                                                                        fundoimg.draw(win)
                                                                                                        rect = Rectangle(Point(530,530),Point(820,662))
                                                                                                        rect.setFill('navajowhite1')
                                                                                                        #rect.draw(win)
                                                                                                        while True:
                                                                                                            X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                                            Y = win.getMouse().getY()
                                                                                                            if (530 < X < 820) and (530 < Y < 662):
                                                                                                                #pergunta 14
                                                                                                                
                                                                                                                fundoimg = Image(Point(500,400), "pergt14.png")
                                                                                                                fundoimg.draw(win)
                                                                                                                rect = Rectangle(Point(180,530),Point(465,662))
                                                                                                                rect.setFill('navajowhite1')
                                                                                                                #rect.draw(win)
                                                                                                                while True:
                                                                                                                    X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                                                    Y = win.getMouse().getY()
                                                                                                                    if (180 < X < 465) and (530 < Y < 662):
                                                                                                                        #pergunta 15
                                                                                                                                 
                                                                                                                        fundoimg = Image(Point(500,400), "pergt15.png")
                                                                                                                        fundoimg.draw(win)
                                                                                                                        rect = Rectangle(Point(180,530),Point(465,662))
                                                                                                                        rect.setFill('navajowhite1')
                                                                                                                        #rect.draw(win)
                                                                                                                        while True:
                                                                                                                            X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                                                            Y = win.getMouse().getY()
                                                                                                                            if (180 < X < 465) and (530 < Y < 662):
                                                                                                                                #pergunta 16
                                                                                                                                         
                                                                                                                                fundoimg = Image(Point(500,400), "pergt16.png")
                                                                                                                                fundoimg.draw(win)
                                                                                                                                rect = Rectangle(Point(180,335),Point(465,470))
                                                                                                                                rect.setFill('navajowhite1')
                                                                                                                                #rect.draw(win)
                                                                                                                                while True:
                                                                                                                                    X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                                                                    Y = win.getMouse().getY()
                                                                                                                                    if (180 < X < 465) and (335 < Y < 470):
                                                                                                                                        #pergunta 17
                                                                                                                                                 
                                                                                                                                        fundoimg = Image(Point(500,400), "pergt17.png")
                                                                                                                                        fundoimg.draw(win)
                                                                                                                                        rect = Rectangle(Point(180,530),Point(465,662))
                                                                                                                                        rect.setFill('navajowhite1')
                                                                                                                                        #rect.draw(win)
                                                                                                                                        while True:
                                                                                                                                            X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                                                                            Y = win.getMouse().getY()
                                                                                                                                            if (180 < X < 465) and (335 < Y < 470):
                                                                                                                                                #pergunta 18
                                                                                                                                                         
                                                                                                                                                fundoimg = Image(Point(500,400), "pergt18.png")
                                                                                                                                                fundoimg.draw(win)
                                                                                                                                                rect = Rectangle(Point(845,125),Point(854,135))
                                                                                                                                                rect.setFill('navajowhite1')
                                                                                                                                                #rect.draw(win)
                                                                                                                                                while True:
                                                                                                                                                    X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                                                                                    Y = win.getMouse().getY()
                                                                                                                                                    if (845 < X < 855) and (125 < Y < 135):
                                                                                                                                                        #pergunta 18
                                                                                                                                                                 
                                                                                                                                                        fundoimg = Image(Point(500,400), "pergt19.png")
                                                                                                                                                        fundoimg.draw(win)
                                                                                                                                                        rect = Rectangle(Point(530,530),Point(820,662))
                                                                                                                                                        rect.setFill('navajowhite1')
                                                                                                                                                        #rect.draw(win)
                                                                                                                                                        while True:
                                                                                                                                                            X = win.getMouse().getX()    #XY = win.getMouse() 
                                                                                                                                                            Y = win.getMouse().getY()
                                                                                                                                                            if (530 < X < 820) and (530 < Y < 662):
                                                                                                                                                                #pergunta 19
                                                                                                                                                                         
                                                                                                                                                                fundoimg = Image(Point(500,400), "fim.png")
                                                                                                                                                                fundoimg.draw(win)
                                                                                                                                                                time.sleep(15)
                                                                                                                                                                win.close()
                                                                                                                                                                main()





                                                                                                                                                            #pergunta 19
                                                                                                                                                            else:
                                                                                                                                                                win.close()
                                                                                                                                                                main()
                                                                                                                              
                                                                                                                                                    #pegunta 18
                                                                                                                                                    else:
                                                                                                                                                        win.close()
                                                                                                                                                        main()

                                                                                                                                            #pergunta 17
                                                                                                                                            else: 
                                                                                                                                                win.close()
                                                                                                                                                main()

                                                                                                                                    #pergunta 16
                                                                                                                                    else:
                                                                                                                                        win.close()
                                                                                                                                        main()

                                                                                                                            #pergunta 15
                                                                                                                            else:
                                                                                                                                win.close()
                                                                                                                                main()

                                                                                                                    #pergunta 14
                                                                                                                    
                                                                                                                    else:
                                                                                                                        win.close()
                                                                                                                        main()
                                                                                                                                                
                                                                                                            #pergunta 13
                                                                                                            else:
                                                                                                              win.close()
                                                                                                              main()

                                                                                                    #pergunta 12
                                                                                                    else: 
                                                                                                        win.close()
                                                                                                        main()

                                                                                            #pergunta 11
                                                                                            else:
                                                                                                win.close()
                                                                                                main()

                                                                                    #pergunta 10
                                                                                    else:
                                                                                        win.close()
                                                                                        main()

                                                                           #pergunta 9
                                                                            else:
                                                                                win.close()
                                                                                main()
                                                                    
                                                                    #pergunta 8
                                                                    else:
                                                                        win.close()
                                                                        main()
                                                                    
                                                              #pergunta 7
                                                              else:
                                                                  win.close()
                                                                  main()

                                                         #pergunta 6
                                                         else:
                                                             win.close()
                                                             main()

                                                 #pergunta 5
                                                 else:
                                                     win.close()
                                                     main()

                                        # pergunta 4
                                          else:
                                             win.close()
                                             main()

                                #pergunta 3     
                                else:
                                    win.close()
                                    main()

                        #pergunta 2
                        else:
                            win.close()
                            main()

                #pergutna 1
                else:
                    win.close()
                    main()
                    
     

main()