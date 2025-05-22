import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.workplane(offset=-200/2).moveTo(-70,-37).cylinder(200,11).union(w0.sketch().segment((-1,-66),(5,-66)).arc((34,-32),(81,-18)).segment((81,66)).segment((-1,66)).close().assemble().finalize().extrude(-65))