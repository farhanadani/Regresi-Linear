import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
penjualan = [9300000,9000000, 12000000,5200000,6000000,7000000,10000000,
		7500000,14500000, 5000000, 16000000, 7000000,11000000, 14000000,
		12500000,14000000,12000000, 11050000,12200000,12200000,14200000,
		12000000,14500000,9500000,13000000, 10500000, 14200000, 9500000]
laba = [2800000,3300000,4160000,2100000,2500000,3000000, 4000000,
		2400000,5000000,1800000,5000000, 2000000,4200000, 5000000,
		4700000,4500000,3700000, 3100000,4300000,4300000,4600000,
		4160000,5000000,3700000,4000000, 3500000, 4600000,  3700000]

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
	print("Nilai a = %.4f"%(a))
	print("Nilai b = %.4f"%(b))
	def f1(nilai,a,b):
		hit = []
		for x in nilai:
			y = b*x+a
			hit.append(y)
		return(hit)
	plt.plot(dtProses[0],f1(dtProses[0],a,b),color='blue',linewidth=3)
	plt.scatter(dtProses[0],dtProses[1],s=15, color='green')
	plt.title("Hasil Regresi Linear")
	plt.ylabel("Laba")
	plt.xlabel("Penjualan")
	plt.legend()
	fig = plt.figure(1)
	fig.canvas.set_window_title("Regresi Linear - Farhan Adani (152017120)")
	plt.show()

grafik([penjualan,laba])