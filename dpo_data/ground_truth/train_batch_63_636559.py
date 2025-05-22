import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
w1=cq.Workplane('YZ',origin=(90,0,0))
r=w0.workplane(offset=-35/2).moveTo(65,46).cylinder(35,9).union(w0.workplane(offset=62/2).moveTo(-54.5,18.5).box(91,121,62)).union(w1.workplane(offset=10/2).moveTo(-75.5,-69).box(7,20,10))