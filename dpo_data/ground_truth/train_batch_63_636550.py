import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,35))
w1=cq.Workplane('ZX',origin=(0,78,0))
r=w0.workplane(offset=-63/2).moveTo(16,-36).cylinder(63,64).union(w1.sketch().push([(-8,-53)]).circle(27).push([(-18,-44.5)]).rect(12,25,mode='s').finalize().extrude(22))