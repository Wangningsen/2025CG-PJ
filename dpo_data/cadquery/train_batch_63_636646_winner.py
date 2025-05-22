import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-1))
w1=cq.Workplane('ZX',origin=(0,10,0))
r=w0.workplane(offset=-99/2).moveTo(-16.5,0).box(117,86,99).union(w1.workplane(offset=27/2).moveTo(48,23).cylinder(27,52))