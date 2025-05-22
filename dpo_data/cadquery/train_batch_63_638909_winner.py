import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,53))
r=w0.sketch().segment((-1,27),(28,27)).arc((49,21),(70,27)).segment((99,27)).segment((99,95)).segment((70,95)).arc((49,100),(28,95)).segment((-1,95)).close().assemble().finalize().extrude(-107).union(w0.workplane(offset=-82/2).moveTo(-46,-47).cylinder(82,53)).union(w0.workplane(offset=-3/2).moveTo(-46,-47).cylinder(3,39))