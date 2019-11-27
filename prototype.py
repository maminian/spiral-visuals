from matplotlib import pyplot
import numpy as np

fig2,ax2 = pyplot.subplots(1,1, figsize=(6,6))
ax2.set_facecolor('k')

def get_arc(rs,ths, narc=21):
    ss = np.linspace(0,1,narc)
    xvs = (rs[0] + ss*(rs[1]-rs[0]))*np.cos(ths[0] + ss*(ths[1]-ths[0]))
    yvs = (rs[0] + ss*(rs[1]-rs[0]))*np.sin(ths[0] + ss*(ths[1]-ths[0]))
    return xvs,yvs
#

def generate(n,r=0.9):
    x0 = 0
    y0 = n
    xs = [x0]
    ys = [y0]
    j=0
    while ys[-1]>0:
        xs.append( xs[-1] + r**j * np.random.randn() )
        ys.append( ys[-1] )
        xs.append( xs[-1] )
        ys.append( ys[-1] -1 )
        j += 1
    #
    xs = np.array(xs)
    ys = np.array(ys)
    return xs,ys
#
def gen_polar(xvs,yvs,myax):
    for j in range(len(xvs)-1):
        xrec,yrec = get_arc(xvs[j:j+2], yvs[j:j+2]) # pretend they are polar.
        myax.plot(xrec, yrec, c=pyplot.cm.plasma(float(j)/(len(xvs)-2)), lw=2)
    return
#

xs,ys = generate(100)
for j in range(len(xs)-1):
    xrec,yrec = get_arc(xs[j:j+2], ys[j:j+2]) # pretend they are polar.
    ax2.plot(xrec, yrec, c=pyplot.cm.plasma(float(j)/(len(xs)-2)), lw=2)
#

xs,ys = generate(200,0.99)
gen_polar(xs,ys,ax2)

ax2.set_xticks([])
ax2.set_yticks([])
ax2.axis('equal')
fig2.tight_layout()

fig2.show()
