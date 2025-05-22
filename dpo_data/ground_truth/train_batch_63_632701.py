import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.workplane(offset=-200/2).cylinder(200,52).union(w0.sketch().rect(118,106).circle(21,mode='s').finalize().extrude(-174))