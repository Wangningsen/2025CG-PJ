import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,66,0))
r=w0.sketch().segment((-88,-86),(-51,-86)).arc((0,-100),(51,-86)).segment((88,-86)).segment((88,-48)).arc((100,0),(88,48)).segment((88,86)).segment((51,86)).arc((0,100),(-51,86)).segment((-88,86)).segment((-88,48)).arc((-100,0),(-88,-48)).close().assemble().circle(17,mode='s').finalize().extrude(-133)