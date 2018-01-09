x_0=0.4
lamb=0.9
list_k=[x_0]
x_n=0

for i in range(999):
	x_n=4*x_0*lamb*(1-x_0)
	list_k.append(x_n)
	x_0=x_n
print list_k
c=TCanvas("c","c",200,200)
list_k.Draw("hist")
c.SaveAs("example_hist.eps")


