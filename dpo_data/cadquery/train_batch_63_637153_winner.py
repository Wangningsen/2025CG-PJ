import cadquery as cq
w0=cq.Workplane('YZ',origin=(77,0,0))
r=w0.sketch().segment((-100,-85),(63,-85)).segment((63,-33)).arc((75,73),(-23,18)).segment((-100,18)).close().assemble().push([(60,65)]).circle(7,mode='s').finalize().extrude(-154)