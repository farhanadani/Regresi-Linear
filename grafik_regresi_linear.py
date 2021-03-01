import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
produksi = [32,51,39,64,82,72,64,39,82,64,72,39,88,72,32,39,82,88,88,39,51,64,72,39,51,64,72,51]
jam_kerja = [3,5,4,6,8,7,6,4,8,6,7,4,9,7,3,4,8,9,9,4,5,6,7,4,5,6,7,5]

def linearRegresion(data):

	x2=[]
	y2=[]
	xy=[]
	n = len(data[0])

	for x in data[0]:
		x2.append(x**2)

	for y in data[0]:
		y2.append(y**2)

	i=0;
	while(i<n):
		dump = data[0][i]*data[1][i]
		xy.append(dump)
		i+=1
	jumlahx = sum(data[0])
	jumlahy = sum(data[1])
	jumlahx2 = sum(x2)
	jumlahxy = sum(xy)

	a = ((jumlahy*jumlahx2)-(jumlahx*jumlahxy))/(n*jumlahx2-(jumlahx**2))
	b = ((n*jumlahxy)-(jumlahx*jumlahy))/(n*jumlahx2-(jumlahx**2))

	return(a,b)

def grafik(dtProses):
	a,b = linearRegresion(dtProses)
	def f1(nilai,a,b):
		hit = []
		for x in nilai:
			y = b*x+a
			hit.append(y)
		return(hit)
	plt.plot(dtProses[0],f1(dtProses[0],a,b),color='blue',linewidth=3)
	plt.scatter(dtProses[0],dtProses[1],s=15, color='green')
	plt.title("Hasil Regresi Linear")
	plt.ylabel("Jam Kerja")
	plt.xlabel("Produksi")
	plt.legend()
	fig = plt.figure(1)
	fig.canvas.set_window_title("Regresi Linear - Farhan Adani (152017120)")
	plt.show()

grafik([produksi,jam_kerja])