import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().arc((-41,43),(5,50),(37,14)).segment((37,100)).segment((-41,100)).close().assemble().push([(14,-82)]).circle(18).finalize().extrude(-74).union(w0.workplane(offset=-67/2).moveTo(6,-48).cylinder(67,35))