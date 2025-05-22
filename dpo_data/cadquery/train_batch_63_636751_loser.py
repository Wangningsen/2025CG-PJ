import cadquery as cq
w0=cq.Workplane('YZ',origin=(63,0,0))
r=w0.sketch().push([(-88,96)]).circle(4).push([(42,-49)]).circle(51).circle(14,mode='s').finalize().extrude(-127)