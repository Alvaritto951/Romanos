r = 0
for pos in range(len(romano)):
    caracter = romano[pos]
    r += simbolos_romanos[caracter]

return r


for caracter in romano:
    r += simbolos_romanos[caracter]

return r