
import matplotlib.pyplot as plt

def plot_xy_x0y0_xsys_(e,x, y, xs, ys):
    plt.figure(figsize=(9,6), dpi=300)
    #plt.xlim(-1,10)
    #plt.ylim(-1,10)
    plt.plot(x, y,ls=':', color = 'b', linewidth = '3')
    
    plt.plot(x[0], y[0], 'o', ms = 10, mec = 'b', mfc = 'b')
    plt.plot(xs, ys, 'o', ms = 10, mec = 'g', mfc = 'g')
    plt.plot(x[len(x)-1], y[len(y)-1], 'o', ms = 10, mec = 'r', mfc = 'r')

    plt.text(x[0]+0.2, y[0], 
         'Xo,Yo', 
         style = 'italic',
         fontsize = 10,
         color = "blue")
    plt.text(x[0]+0.2, y[0]-0.2, 
         '('+str(x[0])+','+str(y[0])+')', 
         style = 'italic',
         fontsize = 10,
         color = "blue")
    

    plt.text(xs+0.2, ys-0.2, 
         'Xs,Ys', 
         style = 'italic',
         fontsize = 10,
         color = "green")
    plt.text(xs+0.2, ys-0.4, 
         '('+str(xs)+','+str(ys)+')', 
         style = 'italic',
         fontsize = 10,
         color = "green")

    plt.text(x[len(x)-1]+0.2,y[len(y)-1], 
         '('+str("%.2f" % x[len(x)-1])+','+str("%.2f" % y[len(y)-1])+')', 
         style = 'italic',
         fontsize = 10,
         color = "red")

    font1 = {'family':'arial','color':'black','size':20}
    font2 = {'family':'arial','color':'black','size':15}

    plt.title("XY particle position", fontdict = font1)
    plt.xlabel("X", fontdict = font2)
    plt.ylabel("Y", fontdict = font2)
    plt.grid()
    
    plt.savefig('images/'+str(e.year)+'-'+str(e.month).zfill(2)+'-'+str(e.day).zfill(2)+'_'+str(e.hour).zfill(2)+str(e.minute).zfill(2)+str(e.second).zfill(2)+'_'+'5_position_xy.png')
    #plt.show()
    plt.close()


def plot_x_(e,x, t):
    plt.figure(figsize=(9,6), dpi=300)
    #plt.xlim(-1,10)
    #plt.ylim(-1,10)
    plt.plot(t,x, color = 'g', linewidth = '3')

    font1 = {'family':'arial','color':'black','size':20}
    font2 = {'family':'arial','color':'black','size':15}

    plt.title("X position", fontdict = font1)
    plt.xlabel("time", fontdict = font2)
    plt.ylabel("X", fontdict = font2)
    plt.grid()
    
    plt.savefig('images/'+str(e.year)+'-'+str(e.month).zfill(2)+'-'+str(e.day).zfill(2)+'_'+str(e.hour).zfill(2)+str(e.minute).zfill(2)+str(e.second).zfill(2)+'_'+'1_position_x.png')
    #plt.show()
    plt.close()

def plot_y_(e,y, t):
    plt.figure(figsize=(9,6), dpi=300)
    #plt.xlim(-1,10)
    #plt.ylim(-1,10)
    plt.plot(t,y, color = 'g', linewidth = '3')

    font1 = {'family':'arial','color':'black','size':20}
    font2 = {'family':'arial','color':'black','size':15}

    plt.title("Y position", fontdict = font1)
    plt.xlabel("time", fontdict = font2)
    plt.ylabel("Y", fontdict = font2)
    plt.grid()
    
    plt.savefig('images/'+str(e.year)+'-'+str(e.month).zfill(2)+'-'+str(e.day).zfill(2)+'_'+str(e.hour).zfill(2)+str(e.minute).zfill(2)+str(e.second).zfill(2)+'_'+'2_position_y.png')
    #plt.show()
    plt.close()

def plot_error_x_(e,ex, t):
    plt.figure(figsize=(9,6), dpi=300)
    #plt.xlim(-1,10)
    #plt.ylim(-1,10)
    plt.plot(t,ex, color = 'r', linewidth = '3')

    font1 = {'family':'arial','color':'black','size':20}
    font2 = {'family':'arial','color':'black','size':15}

    plt.title("X error", fontdict = font1)
    plt.xlabel("time", fontdict = font2)
    plt.ylabel("X error ", fontdict = font2)
    plt.grid()
    
    plt.savefig('images/'+str(e.year)+'-'+str(e.month).zfill(2)+'-'+str(e.day).zfill(2)+'_'+str(e.hour).zfill(2)+str(e.minute).zfill(2)+str(e.second).zfill(2)+'_'+'3_error_x.png')
    #plt.show()
    plt.close()

def plot_error_y_(e,ey, t):
    plt.figure(figsize=(9,6), dpi=300)
    #plt.xlim(-1,10)
    #plt.ylim(-1,10)
    plt.plot(t,ey, color = 'r', linewidth = '3')

    font1 = {'family':'arial','color':'black','size':20}
    font2 = {'family':'arial','color':'black','size':15}

    plt.title("Y error", fontdict = font1)
    plt.xlabel("time", fontdict = font2)
    plt.ylabel("Y error ", fontdict = font2)
    plt.grid()
    
    plt.savefig('images/'+str(e.year)+'-'+str(e.month).zfill(2)+'-'+str(e.day).zfill(2)+'_'+str(e.hour).zfill(2)+str(e.minute).zfill(2)+str(e.second).zfill(2)+'_'+'4_error_y.png')
    #plt.show()
    plt.close()
