# El juego se llama CHOQUE DE PELOTAS CON FAMOSOS EN UNA PISTA DE HIELO
# El usuario introduce su peso y velocidad, y devolverá a qué velocidad y distancia saldría disparado él y el famoso si chocaran en direcciones opuestas

def calculo_velocidades_distancias(m1, v1, m2, v2):
    # Cálculo de las velocidades después del choque
    v1f = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2f = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    
    # Cálculo de las distancias después del choque (suponiendo tiempo de interacción de 0.2s)
    d1 = v1f * 0.2  # Distancia en metros
    d2 = v2f * 0.2  
    
    return v1f, v2f, d1, d2

def roca():
    m = 118  # Peso en kg
    v = -5.55  # Velocidad en m/s
    return m, v

def usainBolt():
    m = 94  
    v = -12.5  
    return m, v

def peterD():
    m = 55  
    v = -2.22  
    return m, v

def main():
    print('Bienvenido al juego CHOQUE DE PELOTAS CON FAMOSOS EN UNA PISTA DE HIELO')
    print('Elige el famoso con el que quisieras chocar:')
    print('1. La Roca')
    print('2. Usain Bolt')
    print('3. Peter Dinklage')
    fam = int(input())  # Famoso con el que chocará
    
    print('Introduce tu peso en kg:')
    mu = int(input())  # Masa Usuario
    print('Introduce la velocidad a la que corres (Velocidad promedio de un humano: 15 km/h):')
    vu = int(input())  # Velocidad Usuario
    vu = vu / 3.6  # Convertir a m/s
    
    if fam == 1:
        m2, v2 = roca()
        v1f, v2f, d1, d2 = calculo_velocidades_distancias(mu, vu, m2, v2)
        print('Si chocaras con La Roca, saldrías disparado con una:')
        print(f'Velocidad de {v1f*3.6:.2f} km/h')  # Convierte v1f a km/h
        print(f'y una distancia de {d1:.2f} metros')
        print(f'Mientras que La Roca saldría a una:')
        print(f'Velocidad de {v2f*3.6:.2f} km/h')  # Convierte v2f a km/h
        print(f'y una distancia de {d2:.2f} metros')
    
    elif fam == 2:
        m2, v2 = usainBolt()
        v1f, v2f, d1, d2 = calculo_velocidades_distancias(mu, vu, m2, v2)
        print('Si chocaras con Usain Bolt, saldrías disparado con una:')
        print(f'Velocidad de {v1f*3.6:.2f} km/h')  # Convierte v1f a km/h
        print(f'y una distancia de {d1:.2f} metros')
        print(f'Mientras que Usain Bolt saldría a una:')
        print(f'Velocidad de {v2f*3.6:.2f} km/h')  # Convierte v2f a km/h
        print(f'y una distancia de {d2:.2f} metros')
    
    elif fam == 3:
        m2, v2 = peterD()
        v1f, v2f, d1, d2 = calculo_velocidades_distancias(mu, vu, m2, v2)
        print('Si chocaras con Peter Dinklage, saldrías disparado con una:')
        print(f'Velocidad de {v1f*3.6:.2f} km/h')  # Convierte v1f a km/h
        print(f'y una distancia de {d1:.2f} metros')
        print(f'Mientras que Peter Dinklage saldría a una:')
        print(f'Velocidad de {v2f*3.6:.2f} km/h')  # Convierte v2f a km/h
        print(f'y una distancia de {d2:.2f} metros')

main()
