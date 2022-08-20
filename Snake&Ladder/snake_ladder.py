import numpy as np
import matplotlib.pyplot as plt
import time

num = []
N = 10
for games in range(N):
    img = plt.imread("snake_board.png")
    fig, ax = plt.subplots()
    ax.imshow(img, extent=[-0.5, 9.5, -0.5, 9.5])

    pos = 1 
    posx = 0.0
    posy = 0.0
    snake_ladder = {1:38, 4:14, 8:30, 28:76, 21:42, 50:67, 71:92, 80:99,  32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:78}

    l, =  plt.plot(posx,posy, 'bo', markersize = 15)
    i = 0
    while True:
        i = i+1
        dice = np.random.randint(1,7)
        if pos+dice <= 100:
            pos = pos + dice
            if pos in snake_ladder.keys():
                posy = int((pos-1)/10)
                posx = (pos - 1)%10 if posy % 2 == 0 else (10*(posy+1) - pos%10)%10
                l.set_ydata(posy)
                l.set_xdata(posx)
                # time.sleep(.5)
                plt.pause(0.01)
                pos = snake_ladder[pos]
            posy = int((pos-1)/10)
            posx = (pos - 1)%10 if posy % 2 == 0 else (10*(posy+1) - pos%10)%10
            l.set_ydata(posy)
            l.set_xdata(posx)
            ax.set_title(f'# dice thrown = {i}, Dice = {dice}')
            # time.sleep(.5)
            plt.pause(0.1)
            if pos == 100:
                break
    
    num.append(i)
    plt.show(block=False)
    plt.pause(0.5)
    plt.close()
x = np.arange(1,N+1)
plt.plot(x,num, '-o')
plt.ylabel("Number of times dice thrown")
plt.xlabel("Game Number")
plt.show()

    


