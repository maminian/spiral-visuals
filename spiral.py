from matplotlib import pyplot
import numpy as np

fig2,ax2 = pyplot.subplots(1,1, figsize=(6,6))
ax2.set_facecolor('k')

def get_arc(rs,ths, narc=16):
    if ths[0]==ths[1]:
        # purely radial movement; only need two points.
        ss = np.linspace(0,1,2)
    else:
        ss = np.linspace(0,1,narc)
    #

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
def gen_polar(xvs,yvs,myax, cmap=pyplot.cm.plasma):
    for j in range(len(xvs)-1):
        xrec,yrec = get_arc(xvs[j:j+2], yvs[j:j+2]) # pretend they are polar.
        myax.plot(xrec, yrec, c=cmap(float(j)/(len(xvs)-2)), lw=2)
    return
#

def gen_spiral(nit=200, r=0.99, cmap=pyplot.cm.plasma, show=True):

    fig,ax = pyplot.subplots(1,1, figsize=(6,6))
    ax.set_facecolor('k')
    xs,ys = generate(nit,r)
    gen_polar(xs,ys,ax, cmap=cmap)

    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('equal')
    fig.tight_layout()

    if show: fig.show()
    
    return fig,ax
#
