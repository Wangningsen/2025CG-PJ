import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
w1=cq.Workplane('XY',origin=(0,0,-1))
r=w0.workplane(offset=27/2).moveTo(49,23).cylinder(27,51).union(w1.workplane(offset=-99/2).moveTo(-16.5,0).box(117,84,99))