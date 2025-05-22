import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,59,0))
r=w0.sketch().segment((-33,-100),(33,-100)).segment((33,-19)).segment((30,-19)).segment((30,-15)).segment((33,-15)).segment((33,100)).segment((-33,100)).close().assemble().push([(-5,-12)]).circle(2,mode='s').finalize().extrude(-118)