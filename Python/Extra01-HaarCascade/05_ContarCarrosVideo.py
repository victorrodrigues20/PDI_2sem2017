# Desafio para fazer na sala
# Verificar quantos carros passam pelo vídeo

# Dicas:
'''

# Pular 4 frames
for contAux in range(0, 4):
    if not cap.isOpened():
        print("Passei")
        break
    ret, frame = cap.read()

if (frame is None):
    break
'''

# Utilizar Flags para controlar se existe um carro
# que está sendo detectado no momento ou não