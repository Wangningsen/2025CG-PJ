import cadquery as cq
w0=cq.Workplane('YZ',origin=(55,0,0))
r=w0.sketch().arc((-1,-8),(94,-37),(13,24)).arc((-14,17),(-1,-8)).assemble().finalize().extrude(-109).union(w0.workplane(offset=-79/2).moveTo(-52,16).cylinder(79,48))