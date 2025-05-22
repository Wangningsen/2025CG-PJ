import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
r=w0.workplane(offset=-42/2).moveTo(-6,-29).cylinder(42,71).union(w0.sketch().segment((56,18),(77,18)).arc((59,59),(59,100)).segment((56,100)).close().assemble().finalize().extrude(-21))