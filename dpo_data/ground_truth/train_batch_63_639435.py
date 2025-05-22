import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,51))
w1=cq.Workplane('ZX',origin=(0,49,0))
r=w0.workplane(offset=-127/2).moveTo(1.5,0).box(163,144,127).union(w1.sketch().segment((7,39),(33,39)).segment((33,94)).arc((-38,-92),(30,95)).segment((7,95)).close().assemble().finalize().extrude(-5))