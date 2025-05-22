import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,79))
r=w0.workplane(offset=-158/2).moveTo(33,99).box(76,2,158).union(w0.workplane(offset=-70/2).moveTo(-51,-80).cylinder(70,20))