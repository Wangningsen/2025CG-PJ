import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
r=w0.workplane(offset=-4/2).moveTo(76,-63).cylinder(4,24).union(w0.sketch().segment((-100,0),(6,0)).segment((7,36)).segment((42,36)).segment((42,72)).segment((7,72)).segment((8,85)).segment((-99,87)).close().assemble().push([(9,54.5)]).rect(4,33,mode='s').finalize().extrude(33))