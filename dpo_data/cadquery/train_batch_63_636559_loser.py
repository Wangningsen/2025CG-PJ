import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
w1=cq.Workplane('YZ',origin=(91,0,0))
r=w0.sketch().push([(65,46)]).circle(9).circle(3,mode='s').finalize().extrude(-35).union(w0.workplane(offset=62/2).moveTo(-54.5,18.5).box(91,121,62)).union(w1.workplane(offset=9/2).moveTo(-75.5,-69).box(7,20,9))