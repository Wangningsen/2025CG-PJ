import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,1,0))
r=w0.sketch().segment((-100,-90),(16,-90)).segment((16,-15)).segment((51,-19)).segment((63,84)).segment((-39,96)).segment((-47,26)).segment((-100,26)).close().assemble().push([(-24.5,-62)]).rect(39,46,mode='s').finalize().extrude(-79).union(w0.workplane(offset=77/2).moveTo(48,-44).cylinder(77,52))