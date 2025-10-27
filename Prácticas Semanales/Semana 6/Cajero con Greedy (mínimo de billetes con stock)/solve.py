# solve_vpl.py — Esqueleto para alumnos

def solve(total: int, max10: int, max20: int, max50: int) -> str:
    """
    Calcula una combinación de billetes de 10, 20 y 50 que suma exactamente
    el importe `total`, respetando el stock disponible para cada denominación
    (`max10`, `max20`, `max50`) y minimizando el número total de billetes.

    Estrategia Greedy:
    - Si `total` es negativo o no es múltiplo de 10, devuelve "ERROR".
    - Intenta primero con el mayor número posible de billetes de 50 
      (sin superar `max50`) y, para cada cantidad de 50 fijada:
        1) Calcula el resto y toma el máximo posible de billetes de 20 (≤ `max20`).
        2) Ajusta los billetes de 20 hacia abajo hasta que el resto sea múltiplo de 10.
        3) Completa el resto con billetes de 10 y verifica que no supere `max10`.
        4) Si la combinación respeta el stock, devuelve "B10 B20 B50" (en ese orden).
    - Si no existe combinación válida, devuelve "ERROR".
    """
    
    if total < 0 or total % 10 != 0:
        return "ERROR"
        
    
    for possible_50 in range(max50, -1, -1):
        rest = total - possible_50*50
        if rest < 0:
            continue
        elif rest == 0:
            return f'0 0 {possible_50}'

        for possible_20 in range(rest//20 if rest <= max20 else max20, -1, -1):
            new_rest = rest - possible_20*20
            
            if new_rest < 0:
                continue
            elif new_rest == 0:
                return f'0 {possible_20} {possible_50}'
            elif new_rest%10 != 0:
                continue

            for possible_10 in range(new_rest//10 if new_rest <= max10 else max10, -1, -1):
                if (possible_50*50+possible_20*20+possible_10*10) == total:
                    return f'{possible_10} {possible_20} {possible_50}'

    # retornando error por defecto
    return "ERROR"
