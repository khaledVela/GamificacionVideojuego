def DefinEstrella(request):
    tiempo = request.data['tiempo']
    if tiempo < 60:
        return 3
    if tiempo < 120:
        return 2
    if tiempo < 180:
        return 1
