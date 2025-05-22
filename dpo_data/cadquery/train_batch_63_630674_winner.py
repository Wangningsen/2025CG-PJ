import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,62,0))
w1=cq.Workplane('YZ',origin=(-34,0,0))
r=w0.workplane(offset=-140/2).moveTo(-94,34).box(12,4,140).union(w0.sketch().push([(-45,-15)]).circle(54).push([(44.5,44)]).rect(111,50).finalize().extrude(-3)).union(w1.sketch().segment((63,-17),(78,-17)).segment((78,5)).arc((70,4),(63,5)).close().assemble().finalize().extrude(9))