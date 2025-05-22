import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,25))
w1=cq.Workplane('XY',origin=(0,0,26))
r=w0.sketch().push([(-67,3)]).circle(33).circle(29,mode='s').finalize().extrude(-50).union(w1.workplane(offset=-51/2).moveTo(30,0).cylinder(51,70))