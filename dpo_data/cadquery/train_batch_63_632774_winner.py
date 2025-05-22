import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,61,0))
r=w0.sketch().segment((63,-100),(70,-100)).segment((70,-19)).segment((67,-19)).arc((69,-15),(70,-11)).segment((70,9)).arc((73,27),(70,46)).segment((70,60)).segment((65,60)).arc((-73,28),(63,-9)).close().assemble().finalize().extrude(-149).union(w0.workplane(offset=27/2).moveTo(0,27.5).box(16,7,27))