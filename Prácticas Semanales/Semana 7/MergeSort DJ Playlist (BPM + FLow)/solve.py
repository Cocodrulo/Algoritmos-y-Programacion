# MergeSort estable para ordenar canciones por BPM (asc), y opcionalmente por energy (desc).
# Devuelve únicamente la lista de títulos ordenados (list[str]).

def sort_playlist_by_flow(tracks, use_energy):
    """
    Ordena una playlist aplicando MergeSort estable por BPM ascendente y, si
    `use_energy` es True, desempatando por energía descendente. Devuelve
    exclusivamente los títulos en el orden final.

    Parámetros:
      - tracks: lista de tuplas (title:str, bpm:int [, energy:int])
      - use_energy: bool → si True, en empates de BPM se usa energy descendente

    Devuelve:
      - list[str]: títulos en el orden final

    Detalles del comparador y estabilidad:
      - Siempre prioriza menor BPM (ascendente).
      - Si `use_energy` es True y el BPM empata, mayor energía primero
        (descendente).
      - Si vuelve a haber empate, se preserva orden de llegada (estabilidad),
        seleccionando el elemento del subarray izquierdo.
    """

    original_tracks = tracks[:]
    
    def compare_tracks(track1, track2):
        if track1[1] != track2[1]:
            return track1[1] < track2[1]
        
        if use_energy and track1[2] != track2[2]:
            return track1[2] > track2[2]
            
        return original_tracks.index(track1) < original_tracks.index(track2)
            
    def merge(left, mid, right):
        left_array = tracks[left:mid]
        right_array = tracks[mid:right]
        
        tracks_idx = left
        left_idx = 0
        right_idx = 0
        
        while tracks_idx < right:
            if left_idx >= len(left_array) or right_idx >= len(right_array):
                if left_idx < len(left_array):
                    tracks[tracks_idx] = left_array[left_idx]
                    left_idx += 1

                if right_idx < len(right_array):
                    tracks[tracks_idx] = right_array[right_idx]
                    right_idx += 1

                tracks_idx += 1
                continue
            
            comp = compare_tracks(left_array[left_idx], right_array[right_idx])
            if comp is True:
                tracks[tracks_idx] = left_array[left_idx]
                left_idx += 1
            elif comp is False:
                tracks[tracks_idx] = right_array[right_idx]
                right_idx += 1
            else:
                tracks[tracks_idx] = left_array[left_idx]
                tracks_idx += 1
                left_idx += 1
                tracks[tracks_idx] = right_array[right_idx]
                right_idx += 1

            tracks_idx += 1
        
    def merge_sort(left, right):
        if left >= right:
            return

        mid = (left+right)//2
        
        merge_sort(left, mid)
        merge_sort(mid+1, right)
        merge(left, mid+1, right)
        
    def getTitles(track):
        return track[0]
    
    merge_sort(0, len(tracks))

    return map(getTitles, tracks)
