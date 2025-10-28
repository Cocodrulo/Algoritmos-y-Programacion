# Esqueleto para ejercicio del VPL
from typing import List

def solve_mfd_feasible(exams: List[int], rooms: List[int]):
    """    

    Objetivo propuesto: 
    Implementar la estrategia MFD (Max-Fit Decreasing)
    para asignar exámenes a aulas con formato de salida esperado:

    "rooms_used=<k> waste=<w>\nassign=[cap1, cap2, ...]"

    donde 'assign[i]' -> capacidad del aula asignada al examen 'exams[i]'.

    Parámetros:
      - exams: lista de enteros con los tamaños/necesidades de cada examen.
      - rooms: lista de enteros con las capacidades de las aulas disponibles.

    Devuelve:
      - (rooms_used, waste, assign_cap) si es factible
      - None si no hay asignación posible

    Implementación de estrategia MFD:
      - Ordenar exámenes de mayor a menor.
      - Ordenar aulas de mayor a menor.
      - Asignar secuencialmente la primera aula suficientemente grande a cada examen.
      - Calcular rooms_used, waste y la lista assign en el orden original de exams.
    """

    # Valor por defecto: indicar que no hay solución.
    
    original_exams = exams[:]
    
    exams.sort(reverse=True)
    rooms.sort(reverse=True)
    assign = [0] * len(exams)
    
    picked_rooms = []
    picked_exams = []
    
    for exam_idx, exam in enumerate(exams):
        for room_idx, room in enumerate(rooms):
            if room_idx in picked_rooms:
                continue
            
            if exam <= room:
                picked_rooms.append(room_idx)
                picked_exams.append(exam_idx)

                index = original_exams.index(exam)
                assign[index] = room
                original_exams[index] = 0

                break
            
        if not exam_idx in picked_exams:
            return None
    
    waste = 0

    for idx in range(len(picked_rooms)):
        waste += rooms[idx] - exams[idx]
    
    return len(picked_rooms), waste, assign

