import cadquery as cq
w0=cq.Workplane('YZ',origin=(4,0,0))
w1=cq.Workplane('XY',origin=(0,0,83))
r=w0.workplane(offset=63/2).moveTo(-93,31).box(14,88,63).union(w1.workplane(offset=-167/2).moveTo(-6,39).cylinder(167,61))