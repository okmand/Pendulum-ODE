import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
from tkinter import messagebox

def RungeKutt(dx, dVx, h):
    x.append(dx)
    y.append(dVx)
    L = 0   # вспомогательная переменная
    i = 0
    while(L < n):   # n = const = 300
        k1X2 = h * Function(x[i], y[i])
        k2X2 = h * Function(x[i] + h / 2, y[i] + k1X2 / 2)
        k3X2 = h * Function(x[i] + h / 2, y[i] + k2X2 / 2)
        k4X2 = h * Function(x[i] + h, y[i] + k3X2)

        k1X1 = h * y[i]
        k2X1 = h * (y[i] + k1X1 / 2)
        k3X1 = h * (y[i] + k2X1 / 2)
        k4X1 = h * (y[i] + k3X1)
        
        xResult = x[i] + (k1X1 + 2 * k2X1 + 2 * k3X1 + k4X1) / 6 
        yResult = y[i] + (k1X2 + 2 * k2X2 + 2 * k3X2 + k4X2) / 6
        x.append(xResult)
        y.append(yResult)
        L += h
        i += 1

def Function(dx, dVx):
    return float(- dx - k*dVx)

if __name__ == '__main__':
    x = []
    y = []
    checkError = 1
    n = 300
    dx = 10
    dVx = 10
    h = 0.01
    k = 0.4
    plt.style.use('seaborn-ticks')

    def buildFromButton(event):
        global ax, x, y
        global k, dx, dVx, n, h
        global checkError # проверяет на ввод данных в TextBox
        if checkError == 1:
            RungeKutt(dx, dVx, h)
            ax.plot(x, y)
            plt.draw()
        checkError = 1
        x = []
        y = []

    def clearFromButton(event):
        global ax 
        ax.clear()
        ax.minorticks_on()
        ax.grid(which='major',
            color = 'k', 
            linewidth = 1)
        ax.grid(which='minor', 
            color = 'k', 
            linestyle = ':')
        plt.draw()


    def kFromSubmit(text):
        global k, checkError
        try:
            k = float(text)
        except ValueError:  
            checkError = 0      
            messagebox.showinfo("GUI Python", "Could not convert string to float: '" + text + "'")
            
    def hFromSubmit(text):
        global h, checkError
        try:
            h = float(text)
        except ValueError:
            checkError = 0
            messagebox.showinfo("GUI Python", "Could not convert string to float: '" + text + "'")

    def dxFromSubmit(text):
        global dx, checkError
        try:
            dx = float(text)
        except ValueError:
            checkError = 0
            messagebox.showinfo("GUI Python", "Could not convert string to float: '" + text + "'")

    def dVxFromSubmit(text):
        global dVx, checkError
        try:
            dVx = float(text)
        except ValueError:
            checkError = 0
            messagebox.showinfo("GUI Python", "Could not convert string to float: '" + text + "'")


    fig, ax = plt.subplots()
    fig.set(facecolor = 'lightgray')
    ax.set(facecolor = 'white')
    fig.canvas.set_window_title('ODE')
    fig.subplots_adjust(left=0.25, right=0.96, top=0.92, bottom=0.06)
    ax.set_title("$\ddot{x} = -x -k\dot{x}$", size = 16)
    ax.minorticks_on()
    ax.grid(which='major',
        color = 'k', 
        linewidth = 1)
    ax.grid(which='minor', 
        color = 'k', 
        linestyle = ':')


    dxBox = plt.axes([0.055, 0.81, 0.1, 0.05])
    dxText = TextBox(dxBox, 'x = ', initial="10", color = '#f0f0f0')
    dxText.on_submit(dxFromSubmit)

    dVxBox = plt.axes([0.055, 0.66, 0.1, 0.05])
    dVxText = TextBox(dVxBox, "x' = ", initial= "10", color = '#f0f0f0')
    dVxText.on_submit(dVxFromSubmit)
    
    hBox = plt.axes([0.055, 0.51, 0.1, 0.05])
    hText = TextBox(hBox, 'h = ', initial="0.01", color = '#f0f0f0')
    hText.on_submit(hFromSubmit)
    
    kBox = plt.axes([0.055, 0.36, 0.1, 0.05])
    kText = TextBox(kBox, 'k = ', initial= "0.4", color = '#f0f0f0')
    kText.on_submit(kFromSubmit)
    
    buttonBuild = plt.axes([0.04, 0.195, 0.13, 0.1])
    buildButton = Button(buttonBuild, 'Построить\nфазовый\nпортрет', color = '#f0f0f0')
    buildButton.on_clicked(buildFromButton)

    buttonClear = plt.axes([0.04, 0.06, 0.13, 0.075])
    clearButton = Button(buttonClear, 'Очистить', color = '#f0f0f0')
    clearButton.on_clicked(clearFromButton)

    plt.show()
