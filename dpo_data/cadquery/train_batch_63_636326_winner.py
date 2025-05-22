import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
w1=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.workplane(offset=-57/2).moveTo(0,-43).box(34,6,57).union(w1.workplane(offset=20/2).moveTo(11,77).box(70,46,20))