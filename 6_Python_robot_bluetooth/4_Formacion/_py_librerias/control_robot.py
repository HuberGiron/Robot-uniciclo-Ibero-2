
def convergencia(x,y,xs,ys,k):
    #Calculo de error
    ex=x-xs
    ey=y-ys
    
    #Control proporcional
    ux=-k*ex
    uy=-k*ey

    return ex,ey,ux,uy
