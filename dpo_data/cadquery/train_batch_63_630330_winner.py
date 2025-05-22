import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
w1=cq.Workplane('XY',origin=(0,0,36))
r=w0.sketch().segment((-52,-73),(52,-73)).segment((52,13)).arc((44,18),(43,26)).segment((-52,26)).close().assemble().push([(-23,11)]).circle(10,mode='s').finalize().extrude(-72).union(w1.workplane(offset=-73/2).cylinder(73,100))