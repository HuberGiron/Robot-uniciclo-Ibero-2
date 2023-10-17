
def convergencia(x,y,xs,ys,k):
    #Calculo de error
    ex=x-xs
    ey=y-ys
    
    #Control proporcional
    ux=-k*ex
    uy=-k*ey

    xx=x+ux #X[1]=X(0)+V*t
    yy=y+uy #Y[1]=Y(0)+V*t

    return ex,ey,xx,yy

def convergencia_xyr1_(x,y,xs,ys,k,xr1,yr1):
    #Potencial atractivo
    ex=x-xs
    ey=y-ys
    ax=-k*ex
    ay=-k*ey

    #Potencial repulsivo
    b=((x-xr1)*(x-xr1))+((y-yr1)*(y-yr1))
    r=2
    dbdx=-2*(x-xr1)*(1/b)*(1/b)
    dbdy=-2*(y-yr1)*(1/b)*(1/b)

    if b<=(r*r):
        GRx=2*((1/b) -(1/(r*r)))*dbdx
        GRy=2*((1/b) -(1/(r*r)))*dbdy
    else:
        GRx=0
        GRy=0

    et=0.01
    RX=-et*GRx
    RY=-et*GRy

    #Ley Final
    ux=ax+RX
    uy=ay+RY

    #Valores siguientes
    xx=x+ux #X[1]=X(0)+V*t
    yy=y+uy #Y[1]=Y(0)+V*t

    return ex,ey,xx,yy