import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
w1=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.sketch().push([(6,19)]).circle(44).circle(25,mode='s').finalize().extrude(-45).union(w0.sketch().segment((-6,41),(11,15)).segment((61,85)).segment((43,100)).close().assemble().finalize().extrude(-18)).union(w1.workplane(offset=-85/2).moveTo(-3,-31).box(66,60,85))