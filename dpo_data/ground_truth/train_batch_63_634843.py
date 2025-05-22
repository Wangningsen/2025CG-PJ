import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,56,0))
r=w0.workplane(offset=-112/2).moveTo(-38,0).cylinder(112,7).union(w0.sketch().segment((-42,-49),(-14,32)).segment((20,20)).arc((-94,26),(-17,-58)).close().assemble().push([(67,-7)]).circle(33).finalize().extrude(-16))