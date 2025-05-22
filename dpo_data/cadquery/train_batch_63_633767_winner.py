import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('XY',origin=(0,0,-42))
r=w0.workplane(offset=20/2).moveTo(-16,-74).cylinder(20,26).union(w0.sketch().segment((35,93),(69,93)).segment((69,100)).arc((52,94),(35,100)).close().assemble().finalize().extrude(86)).union(w1.workplane(offset=-57/2).moveTo(-22,1).cylinder(57,47))