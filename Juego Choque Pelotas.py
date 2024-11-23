# El juego se llama CHOQUE DE PELOTAS CON FAMOSOS EN UNA PISTA DE HIELO
# El usuario introduce su peso y velocidad, y devolverá a qué velocidad y distancia saldría disparado él y el famoso si chocaran en direcciones opuestas

def calculo_velocidades_distancias_impulso(m1, v1, m2, v2):
    # Cálculo de las velocidades después del choque
    v1f = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2f = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    
    # Cálculo de los impulsos
    impulso1 = m1 * (v1f - v1)
    impulso2 = m2 * (v2f - v2)
    
    # Cálculo de las distancias después del choque
    d1 = abs(v1f) * 0.2  # Tiempo de interacción
    d2 = abs(v2f) * 0.2
    
    return v1f, v2f, d1, d2, impulso1, impulso2

def roca():
    m = 118  # Peso en kg
    v = 5.55  # Velocidad en m/s
    return m, v

def usainBolt():
    m = 94  # Peso en kg
    v = 12.5  # Velocidad en m/s
    return m, v

def peterD():
    m = 55  # Peso en kg
    v = 2.22  # Velocidad en m/s
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
    print('Introduce la velocidad a la que corres (Velocidad promedio de un humano: 15 km/h)')
    vu = int(input())  # Velocidad Usuario
    vu = vu / 3.6  # Pasar velocidad a m/s
    
    if fam == 1:
        v1f, v2f, d1, d2, impulso1, impulso2 = calculo_velocidades_distancias_impulso(mu, vu, *roca())
        print('Si chocaras con La Roca, saldrías a una:')
        print(f'Velocidad de {v1f * 3.6:.2f} km/h')  # Convierte v a km/h
        print(f'y a una Distancia de {d1:.2f} metros')
        print(f'El Impulso de La Roca es: {impulso2:.2f} N·s')
        print(f'Mientras que La Roca saldría a una:')
        print(f'Velocidad de {v2f * 3.6:.2f} km/h')  # Convierte v a km/h
        print(f'y a una Distancia de {d2:.2f} metros')
        print(f'El Impulso de tu cuerpo es: {impulso1:.2f} N·s')
    
    elif fam == 2:
        v1f, v2f, d1, d2, impulso1, impulso2 = calculo_velocidades_distancias_impulso(mu, vu, *usainBolt())
        print('Si chocaras con Usain Bolt, saldrías a una:')
        print(f'Velocidad de {v1f * 3.6:.2f} km/h')  # Convierte v a km/h
        print(f'y a una Distancia de {d1:.2f} metros')
        print(f'El Impulso de Usain Bolt es: {impulso2:.2f} N·s')
        print(f'Mientras que Usain Bolt saldría a una:')
        print(f'Velocidad de {v2f * 3.6:.2f} km/h')  # Convierte v a km/h
        print(f'y a una Distancia de {d2:.2f} metros')
        print(f'El Impulso de tu cuerpo es: {impulso1:.2f} N·s')
    
    elif fam == 3:
        v1f, v2f, d1, d2, impulso1, impulso2 = calculo_velocidades_distancias_impulso(mu, vu, *peterD())
        print('Si chocaras con Peter Dinklage, saldrías a una:')
        print(f'Velocidad de {v1f * 3.6:.2f} km/h')  # Convierte v a km/h
        print(f'y a una Distancia de {d1:.2f} metros')
        print(f'El Impulso de Peter Dinklage es: {impulso2:.2f} N·s')
        print(f'Mientras que Peter Dinklage saldría a una:')
        print(f'Velocidad de {v2f * 3.6:.2f} km/h')  # Convierte v a km/h
        print(f'y a una Distancia de {d2:.2f} metros')
        print(f'El Impulso de tu cuerpo es: {impulso1:.2f} N·s')

main()
