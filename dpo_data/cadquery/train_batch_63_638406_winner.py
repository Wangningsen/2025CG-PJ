import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
r=w0.workplane(offset=-42/2).moveTo(-6,-29).cylinder(42,71).union(w0.sketch().segment((56,-10),(59,-10)).segment((59,4)).arc((78,22),(59,39)).segment((59,100)).segment((56,100)).segment((56,39)).arc((37,22),(56,4)).close().assemble().finalize().extrude(-21))