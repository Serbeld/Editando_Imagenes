import cv2

def generar_imagen(cond_i,name,tmx,tmy,formato = '.png',color = (0, 0, 0),tamaño_de_la_letra = 1.4,bold = 7):
	extra = ''

	if cond_i < 10:
		extra = '000'

	elif cond_i < 100:
		extra = '00'

	elif cond_i < 1000:
		extra = '0'

	img = cv2.imread(name)
	file = str(cond_i) + formato
	cv2.putText(img,extra+str(cond_i),(tmx,tmy),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,tamaño_de_la_letra,color,bold)
	cv2.imwrite(file,img)

# Nombre del archivo
name = 'Tx.png'

# Coordenadas
tmx = 72
tmy = 110

for cond_i in range (1,1001):
	generar_imagen(cond_i,name,tmx,tmy)