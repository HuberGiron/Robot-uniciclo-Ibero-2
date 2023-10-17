
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
