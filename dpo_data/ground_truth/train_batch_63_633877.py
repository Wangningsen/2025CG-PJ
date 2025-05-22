import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,26,0))
r=w0.sketch().arc((-98,52),(-89,-8),(-42,-48)).arc((-34,-31),(-38,-49)).arc((23,-43),(65,2)).segment((97,-10)).segment((100,-1)).segment((68,11)).arc((70,20),(70,29)).arc((64,21),(56,15)).segment((27,25)).segment((24,16)).segment((47,8)).arc((-36,-3),(-98,52)).assemble().finalize().extrude(-51)