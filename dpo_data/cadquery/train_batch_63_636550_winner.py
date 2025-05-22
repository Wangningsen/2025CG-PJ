import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,78,0))
w1=cq.Workplane('XY',origin=(0,0,35))
r=w0.sketch().push([(-8,-52)]).circle(27).push([(-18,-44)]).rect(12,24,mode='s').finalize().extrude(22).union(w1.workplane(offset=-63/2).moveTo(16,-36).cylinder(63,64))