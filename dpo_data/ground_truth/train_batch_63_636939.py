import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-39,0))
r=w0.workplane(offset=-8/2).moveTo(17,-33.5).box(98,43,8).union(w0.workplane(offset=-8/2).moveTo(-34,48).box(100,104,8)).union(w0.sketch().segment((33,-98),(33,-40)).segment((83,-40)).arc((-33,10),(33,-98)).assemble().finalize().extrude(85))