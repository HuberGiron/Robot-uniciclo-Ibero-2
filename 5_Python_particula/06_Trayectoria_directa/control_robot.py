
def convergencia(x,y,xs,ys,k):
    #Calculo de error
    ex=x-xs
    ey=y-ys
    
    ux, uy =potencial_atractivo(ex,ey,k)

    xx=x+ux #X[1]=X(0)+V*t
    yy=y+uy #Y[1]=Y(0)+V*t

    return ex,ey,xx,yy

def convergencia_xyr1_(x,y,xs,ys,k,xr1,yr1):
    #Potencial atractivo
    ex=x-xs
    ey=y-ys
    ax, ay =potencial_atractivo(ex,ey,k)
    RX, RY =potencial_repulsivo(x,y,xr1,yr1,3,0.5)

    #Ley Final
    ux=ax+RX
    uy=ay+RY

    #Valores siguientes
    xx=x+ux #X[1]=X(0)+V*t
    yy=y+uy #Y[1]=Y(0)+V*t

    return ex,ey,xx,yy

def convergencia_xyr1_espiral(x,y,xs,ys,k,xr1,yr1):
    
    ex=x-xs
    ey=y-ys

    ax, ay =potencial_atractivo_espiral(ex,ey,k,0.06)
    RX, RY =potencial_repulsivo(x,y,xr1,yr1,3,0.5)

    #Ley Final
    ux=ax+RX
    uy=ay+RY

    #Valores siguientes
    xx=x+ux #X[1]=X(0)+V*t
    yy=y+uy #Y[1]=Y(0)+V*t

    return ex,ey,xx,yy

def convergencia_xyr3_espiral(x,y,xs,ys,k,xr1,yr1,xr2,yr2,xr3,yr3):
    
    ex=x-xs
    ey=y-ys

    ax, ay =potencial_atractivo_espiral(ex,ey,k,0.01)
    RX1, RY1 =potencial_repulsivo(x,y,xr1,yr1,1,0.01)
    RX2, RY2 =potencial_repulsivo(x,y,xr2,yr2,1,0.01)
    RX3, RY3 =potencial_repulsivo(x,y,xr3,yr3,1,0.01)

    #Ley Final
    ux=ax+RX1+RX2+RX3
    #print(ax,RX1,RX2,RX3)
    #print('ux='+str(ux))
    uy=ay+RY1+RY2+RY3
    #print(ay,RY1,RY2,RY3)
    #print('uy='+str(uy))

    #Valores siguientes
    xx=x+ux #X[1]=X(0)+V*t
    yy=y+uy #Y[1]=Y(0)+V*t

    return ex,ey,xx,yy

def potencial_atractivo_espiral(ex,ey,k,c):
    #Potencial atractivo
    ax=(-k*ex)-(c*ey) #Espiral
    ay=(-k*ey)+(c*ex) #Espiral

    return ax, ay

def potencial_atractivo(ex,ey,k):
    #Potencial atractivo
    ax=-k*ex
    ay=-k*ey

    return ax, ay


def potencial_repulsivo(x,y,xr1,yr1,r,et):
#Potencial repulsivo
    GRx=0
    GRy=0

    b=((x-xr1)*(x-xr1))+((y-yr1)*(y-yr1))
    #print('b='+str(b))

    dbdx=-2*(x-xr1)*(1/b)*(1/b)
    #print('dbdx='+str(dbdx))
    dbdy=-2*(y-yr1)*(1/b)*(1/b)
    #print('dbdy='+str(dbdy))

    if b<=(r*r):
        GRx=2*((1/b) -(1/(r*r)))*dbdx
        #print('Grx='+str(GRx))
        GRy=2*((1/b) -(1/(r*r)))*dbdy
        #print('Gry='+str(GRy))

        if GRx<=(-1):
            GRx=-1
        if GRy<=(-1):
            GRy=-1

    else:
        GRx=0
        GRy=0

    RX=-et*GRx
    RY=-et*GRy

    return RX, RY