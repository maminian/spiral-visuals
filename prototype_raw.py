from matplotlib import pyplot
import numpy as np
fig,ax = pyplot.subplots(1,1, figsize=(5,10))
fig.show()
fig,ax = pyplot.subplots(1,1, figsize=(4,8))
fig.show()
fig.tight_layout()
pyplot.ion()
ax.set_facecolor('k')
xs = []
ys = []
y0 = 100
x0 = 0.
xs.append(x0)
ys.append(y0)
j = 0
while ys[-1]>0:
    xs.append( xs[-1] + 0.9**j * np.random.randn() )
    ys.append( ys[-1] )
    xs.append( xs[-1] )
    ys.append( ys[-1] -1 )
    j += 1
xs
ys
xs = np.array(xs)
ys = np.array(ys)
for j in range(len(xs)-1):
    ax.plot(xs[j:j+2], ys[j:j+2], c=pyplot.cm.magma(float(j)/(len(xs)-2)), lw=2)
ax.cla()
for j in range(len(xs)-1):
    ax.plot(xs[j:j+2], ys[j:j+2], c=pyplot.cm.plasma(float(j)/(len(xs)-2)), lw=2)
fig2,ax2 = pyplot.subplots(1,1, figsize=(6,6))
ax2.set_facecolor('k')
fig2.tight_layout()
def get_arc(rs,ths):
    ss = np.linspace(0,1,101)
    xvs = (rs[0] + ss*rs[1])*np.cos(ths[0] + ss*ths[1])
    yvs = (rs[0] + ss*rs[1])*np.sin(ths[0] + ss*ths[1])
    return xvs,yvs
for j in range(len(xs)-1):
    xrec,yrec = get_arc(xs[j:j+2], ys[j:j+2]) # pretend they are polar.
    ax2.plot(xrec, yrec c=pyplot.cm.plasma(float(j)/(len(xs)-2)), lw=2)
for j in range(len(xs)-1):
    xrec,yrec = get_arc(xs[j:j+2], ys[j:j+2]) # pretend they are polar.
    ax2.plot(xrec, yrec, c=pyplot.cm.plasma(float(j)/(len(xs)-2)), lw=2)
ax2.cla()
def get_arc(rs,ths):
    ss = np.linspace(0,1,101)
    xvs = (rs[0] + ss*(rs[1]-rs[0]))*np.cos(ths[0] + ss*(ths[1]-ths[0]))
    yvs = (rs[0] + ss*(rs[1]-rs[0]))*np.sin(ths[0] + ss*(ths[1]-ths[0]))
    return xvs,yvs
for j in range(len(xs)-1):
    xrec,yrec = get_arc(xs[j:j+2], ys[j:j+2]) # pretend they are polar.
    ax2.plot(xrec, yrec, c=pyplot.cm.plasma(float(j)/(len(xs)-2)), lw=2)
def generate(n,r=0.9):
    x0 = 0
    y0 = n
    xs = [x0]
    ys = [y0]
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
ax2.cla()
xs,ys = generate(100)
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
xs,ys = generate(100)
for j in range(len(xs)-1):
    xrec,yrec = get_arc(xs[j:j+2], ys[j:j+2]) # pretend they are polar.
    ax2.plot(xrec, yrec, c=pyplot.cm.plasma(float(j)/(len(xs)-2)), lw=2)
ax2.cla()
def gen_polar(xvs,yvs,myax):
    for j in range(len(xvs)-1):
        xrec,yrec = get_arc(xvs[j:j+2], yvs[j:j+2]) # pretend they are polar.
        myax.plot(xrec, yrec, c=pyplot.cm.plasma(float(j)/(len(xvs)-2)), lw=2)
    return
xs,ys = generate(100)
gen_polar(xs,ys,ax2)
xs,ys = generate(100,0.95)
xs,ys = generate(200,0.95)
ax2.cla(); gen_polar(xs,ys,ax2)
xs,ys = generate(200,0.99)
ax2.cla(); gen_polar(xs,ys,ax2)
xs,ys = generate(200,0.99)
def get_arc(rs,ths):
    ss = np.linspace(0,1,21)
    xvs = (rs[0] + ss*(rs[1]-rs[0]))*np.cos(ths[0] + ss*(ths[1]-ths[0]))
    yvs = (rs[0] + ss*(rs[1]-rs[0]))*np.sin(ths[0] + ss*(ths[1]-ths[0]))
    return xvs,yvs
ax2.cla(); gen_polar(xs,ys,ax2)
cd Documents/GitHub/spiral-visuals/
ax2.set_xticks([])
ax2.set_yticks([])
fig2.tight_layout()
fig2.savefig('example.png', dpi=120, bbox_inches='tight')
%history -f prototype_raw.py
ax2.axis('equal')
fig2.savefig('example.png', dpi=120, bbox_inches='tight')
%history -f prototype_raw.py
