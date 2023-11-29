def DefinEstrella(request):
    tiempo = request.data['tiempo']
    if tiempo < 60:
        return 1
    elif 60 < tiempo < 90:
        return 2
    elif 90 < tiempo < 180:
        return 3
    else:
        return 0
