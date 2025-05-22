import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
r=w0.workplane(offset=-96/2).moveTo(0.5,0).box(21,28,96).union(w0.sketch().push([(0,-1)]).circle(10).push([(-8.5,-1.5)]).rect(3,3,mode='s').finalize().extrude(104))