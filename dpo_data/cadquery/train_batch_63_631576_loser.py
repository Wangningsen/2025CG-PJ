import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-18))
w1=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.sketch().push([(-74.5,44.5)]).rect(51,19).push([(-75,44)]).circle(4,mode='s').finalize().extrude(-19).union(w1.workplane(offset=-11/2).moveTo(5,94).box(64,12,11))