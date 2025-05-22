import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-59,0))
r=w0.sketch().segment((-33,-100),(33,-100)).segment((33,-18)).segment((32,-18)).segment((32,-16)).segment((33,-16)).segment((33,100)).segment((-33,100)).close().assemble().push([(-5,-13)]).circle(2,mode='s').finalize().extrude(118)