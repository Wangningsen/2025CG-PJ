import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.sketch().segment((-16,-67),(100,-67)).segment((100,-15)).segment((7,-15)).segment((7,-7)).segment((-16,-7)).close().assemble().push([(1,-33)]).circle(5,mode='s').finalize().extrude(49).union(w0.workplane(offset=86/2).moveTo(-54,21).cylinder(86,46))