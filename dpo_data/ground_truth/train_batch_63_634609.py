import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
w1=cq.Workplane('YZ',origin=(-37,0,0))
r=w0.workplane(offset=76/2).moveTo(19.5,-27.5).box(35,31,76).union(w1.workplane(offset=68/2).moveTo(0,-42).cylinder(68,58))