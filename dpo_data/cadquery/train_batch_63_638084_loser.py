import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().push([(-33,53)]).rect(34,94).reset().face(w0.sketch().segment((-7,-12),(5,-21)).segment((23,1)).segment((11,10)).close().assemble()).finalize().extrude(-77).union(w0.workplane(offset=40/2).moveTo(3,-53).cylinder(40,47))