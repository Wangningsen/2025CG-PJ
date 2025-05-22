import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().segment((-100,-4),(30,-4)).arc((84,-56),(54,11)).segment((54,62)).segment((-100,63)).close().assemble().push([(63,-25)]).circle(30,mode='s').finalize().extrude(12)