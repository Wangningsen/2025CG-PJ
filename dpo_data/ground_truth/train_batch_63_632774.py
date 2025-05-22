import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,61,0))
w1=cq.Workplane('ZX',origin=(0,88,0))
r=w0.sketch().segment((63,-100),(70,-100)).segment((70,8)).arc((73,27),(70,46)).segment((70,60)).segment((65,60)).arc((-73,29),(63,-9)).close().assemble().finalize().extrude(-149).union(w1.workplane(offset=-175/2).moveTo(0,27).cylinder(175,8))