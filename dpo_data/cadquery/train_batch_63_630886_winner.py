import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,81,0))
r=w0.sketch().segment((-70,-59),(48,-59)).segment((48,-100)).segment((62,-100)).segment((62,-59)).segment((70,-59)).segment((70,100)).segment((-70,100)).close().assemble().push([(0,21)]).circle(9,mode='s').finalize().extrude(-163)