import cadquery as cq
w0=cq.Workplane('YZ',origin=(-77,0,0))
r=w0.sketch().segment((-100,-85),(63,-85)).segment((63,-33)).arc((69,77),(-23,18)).segment((-100,18)).close().assemble().push([(59,61)]).circle(5,mode='s').finalize().extrude(154)