import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().rect(188,26).circle(11,mode='s').push([(40,-10)]).circle(4,mode='s').finalize().extrude(-200).union(w0.workplane(offset=-175/2).cylinder(175,89))