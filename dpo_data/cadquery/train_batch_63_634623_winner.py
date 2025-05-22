import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-24,0))
r=w0.sketch().segment((-91,-100),(-60,-100)).arc((-15,32),(91,51)).segment((91,100)).segment((-91,100)).close().assemble().push([(-34,22)]).circle(3,mode='s').finalize().extrude(49)