import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
w1=cq.Workplane('XY',origin=(0,0,-28))
r=w0.sketch().push([(-8,-53)]).circle(27).push([(-20,-49)]).circle(8,mode='s').finalize().extrude(-22).union(w1.workplane(offset=63/2).moveTo(16,-36).cylinder(63,64))