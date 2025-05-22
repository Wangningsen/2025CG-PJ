import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.sketch().segment((-100,-2),(-78,-2)).segment((-80,-4)).segment((-69,-14)).segment((-59,-2)).segment((20,-2)).segment((20,71)).segment((-2,71)).segment((0,72)).segment((-11,82)).segment((-20,71)).segment((-100,71)).close().assemble().push([(42,-49.5)]).rect(116,65).finalize().extrude(35)