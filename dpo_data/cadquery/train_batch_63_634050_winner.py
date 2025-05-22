import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,84,0))
r=w0.sketch().push([(-55,-94)]).circle(6).reset().face(w0.sketch().arc((16,-52),(19,-57),(22,-64)).segment((23,-64)).segment((23,100)).segment((16,100)).close().assemble()).finalize().extrude(-168).union(w0.workplane(offset=-22/2).moveTo(19.5,18).box(83,30,22))