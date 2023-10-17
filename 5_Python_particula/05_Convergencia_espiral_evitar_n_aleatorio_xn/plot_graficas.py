
import matplotlib.pyplot as plt

def plot_xy_x0y0_xsys_xyr(e,x, y, xs, ys, xr, yr, aleatorios,iter):
    plt.figure(figsize=(9,6), dpi=300)
    #plt.xlim(-1,10)
    #plt.ylim(-1,10)
    plt.plot(x, y,ls='-', color = 'b', linewidth = '3')
    
    plt.plot(x[0], y[0], 'o', ms = 10, mec = 'b', mfc = 'b')
    plt.plot(xs, ys, 'o', ms = 10, mec = 'g', mfc = 'g')
    plt.plot(x[len(x)-1], y[len(y)-1], 'o', ms = 10, mec = 'r', mfc = 'r')

    plt.text(x[0]+0.2, y[0]-0.2, 
         '('+str(x[0])+','+str(y[0])+')', 
         style = 'italic',
         fontsize = 10,
         color = "blue")
    

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
    
    for i in range(0,aleatorios):
     plt.plot(xr[i], yr[i], 'o', ms = 10, mec = 'm', mfc = 'm')
     plt.text(xr[i]+0.2,yr[i], 
          '('+str(xr[i])+','+str(yr[i])+')', 
          style = 'italic',
          fontsize = 10,
          color = "magenta")

    font1 = {'family':'arial','color':'black','size':20}
    font2 = {'family':'arial','color':'black','size':15}

    plt.title("XY particle position", fontdict = font1)
    plt.xlabel("X", fontdict = font2)
    plt.ylabel("Y", fontdict = font2)
    plt.grid()
    
    plt.savefig('images/'+str(e.year)+'-'+str(e.month).zfill(2)+'-'+str(e.day).zfill(2)+'_'+str(e.hour).zfill(2)+str(e.minute).zfill(2)+str(e.second).zfill(2)+'_'+str(iter)+'position_xy.png')
    #plt.show()
    plt.close()

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

def plot_xy_x0y0_xsys_xyr1(e,x, y, xs, ys, xr, yr):
    plt.figure(figsize=(9,6), dpi=300)
    #plt.xlim(-1,10)
    #plt.ylim(-1,10)
    plt.plot(x, y,ls=':', color = 'b', linewidth = '3')
    
    plt.plot(x[0], y[0], 'o', ms = 10, mec = 'b', mfc = 'b')
    plt.plot(xs, ys, 'o', ms = 10, mec = 'g', mfc = 'g')
    plt.plot(xr, yr, 'o', ms = 10, mec = 'm', mfc = 'm')
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
    
    plt.text(xr+0.2,yr, 
         '('+str("%.2f" % xr)+','+str("%.2f" % yr)+')', 
         style = 'italic',
         fontsize = 10,
         color = "magenta")

    font1 = {'family':'arial','color':'black','size':20}
    font2 = {'family':'arial','color':'black','size':15}

    plt.title("XY particle position", fontdict = font1)
    plt.xlabel("X", fontdict = font2)
    plt.ylabel("Y", fontdict = font2)
    plt.grid()
    
    plt.savefig('images/'+str(e.year)+'-'+str(e.month).zfill(2)+'-'+str(e.day).zfill(2)+'_'+str(e.hour).zfill(2)+str(e.minute).zfill(2)+str(e.second).zfill(2)+'_'+'5_position_xy.png')
    #plt.show()
    plt.close()

def plot_xy_x0y0_xsys_xyr3(e,x, y, xs, ys, xr1, yr1, xr2, yr2, xr3, yr3):
    plt.figure(figsize=(9,6), dpi=300)
    #plt.xlim(-1,10)
    #plt.ylim(-1,10)
    plt.plot(x, y,ls=':', color = 'b', linewidth = '3')
    
    plt.plot(x[0], y[0], 'o', ms = 10, mec = 'b', mfc = 'b')
    plt.plot(xs, ys, 'o', ms = 10, mec = 'g', mfc = 'g')
    plt.plot(xr1, yr1, 'o', ms = 10, mec = 'm', mfc = 'm')
    plt.plot(xr2, yr2, 'o', ms = 10, mec = 'm', mfc = 'm')
    plt.plot(xr3, yr3, 'o', ms = 10, mec = 'm', mfc = 'm')
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
    
    plt.text(xr1+0.2,yr1, 
         '('+str("%.2f" % xr1)+','+str("%.2f" % yr1)+')', 
         style = 'italic',
         fontsize = 10,
         color = "magenta")
    plt.text(xr2+0.2,yr2, 
         '('+str("%.2f" % xr2)+','+str("%.2f" % yr2)+')', 
         style = 'italic',
         fontsize = 10,
         color = "magenta")
    plt.text(xr3+0.2,yr3, 
         '('+str("%.2f" % xr3)+','+str("%.2f" % yr3)+')', 
         style = 'italic',
         fontsize = 10,
         color = "magenta")

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
