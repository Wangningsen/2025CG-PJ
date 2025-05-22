import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-51,0))
w1=cq.Workplane('XY',origin=(0,0,-49))
r=w0.sketch().push([(25,-68)]).circle(32).push([(41.5,-60)]).rect(7,18,mode='s').finalize().extrude(97).union(w1.sketch().segment((38,38),(61,38)).segment((61,18)).segment((76,18)).segment((76,-5)).arc((83,-2),(88,3)).segment((88,6)).segment((91,6)).arc((96,5),(100,3)).segment((100,32)).segment((88,32)).segment((88,39)).segment((78,39)).arc((59,51),(38,38)).assemble().finalize().extrude(-8))