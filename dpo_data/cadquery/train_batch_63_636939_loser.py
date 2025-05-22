import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-39,0))
w1=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.sketch().push([(-34,48)]).rect(100,104).reset().face(w0.sketch().segment((-14,-55),(69,-55)).segment((69,-40)).segment((60,-40)).segment((60,-41)).segment((58,-41)).segment((58,-40)).segment((-14,-40)).close().assemble()).finalize().extrude(-7).union(w0.sketch().segment((33,-98),(33,-40)).segment((83,-40)).arc((-31,12),(33,-98)).assemble().finalize().extrude(86)).union(w1.workplane(offset=7/2).moveTo(21,-33).box(106,44,7))