import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-35,0))
r=w0.sketch().arc((-33,-19),(-35,-100),(-19,-20)).arc((-12,99),(-33,-19)).assemble().push([(78,9)]).circle(4).finalize().extrude(35).union(w0.workplane(offset=71/2).moveTo(-3,-53).cylinder(71,24))