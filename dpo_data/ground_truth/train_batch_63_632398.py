import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((81,53),(81,56)).arc((-40,-91),(83,53)).close().assemble().push([(17,25)]).circle(49,mode='s').finalize().extrude(200)