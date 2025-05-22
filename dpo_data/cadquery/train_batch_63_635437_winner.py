import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
w1=cq.Workplane('ZX',origin=(0,41,0))
r=w0.sketch().arc((-1,19),(23,-50),(16,23)).segment((16,19)).close().assemble().push([(-3,-13)]).circle(3,mode='s').finalize().extrude(-110).union(w0.workplane(offset=83/2).moveTo(-42,60.5).box(22,21,83)).union(w1.workplane(offset=9/2).moveTo(-19,60).box(104,80,9))