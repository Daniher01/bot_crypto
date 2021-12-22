from indicadores import *
import funciones

def cruce_hma(df, periodo1, periodo2): #estrategia solo para opciones BUY
    market = None
    precio_actual = float(df['close'][-1:])
    vela_anterior = float(df['close'][-2:-1])
    dos_velas_antes = float(df['close'][-3:-2])
    hma50 = HMA(df, periodo1)
    hma80 = HMA(df, periodo2)
    #ejecutar opcion de compra
    if hma80 > hma50 and precio_actual > hma80:
        print('Cruce medias moviles')
        if dos_velas_antes < vela_anterior and vela_anterior < precio_actual:
            print('Oportunidad de compra')
            market = True
    elif hma50 > hma80 and precio_actual < hma50 and market:
        print('Cerrar Operacion')
        market = False
    else:
        print('No se esta cumpliendo la estrategia')
        market = None
    return market
    #retorna booleano


