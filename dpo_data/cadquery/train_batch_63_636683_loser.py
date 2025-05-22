import cadquery as cq
w0=cq.Workplane('YZ',origin=(55,0,0))
r=w0.sketch().arc((-3,-9),(97,-30),(5,18)).arc((-16,10),(-3,-9)).assemble().finalize().extrude(-110).union(w0.workplane(offset=-79/2).moveTo(-52,16).cylinder(79,48))