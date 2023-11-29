def DefinEstrella(request):
    tiempo = request.data['tiempo']
    if tiempo < 60:
        return 1
    elif tiempo > 60 and tiempo < 90:
        return 2
    elif tiempo > 90 and tiempo < 180:
        return 3
