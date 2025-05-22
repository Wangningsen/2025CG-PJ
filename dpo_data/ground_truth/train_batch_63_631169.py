import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
w1=cq.Workplane('YZ',origin=(-63,0,0))
r=w0.workplane(offset=40/2).moveTo(-23,-3).cylinder(40,77).union(w1.workplane(offset=163/2).moveTo(75,-29).box(10,10,163))