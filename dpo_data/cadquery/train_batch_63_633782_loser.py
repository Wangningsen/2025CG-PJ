import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().arc((-60,22),(-39,9),(-14,15)).arc((16,53),(-2,89)).close().assemble().finalize().extrude(-112).union(w0.sketch().segment((17,-68),(46,-89)).segment((60,-69)).segment((30,-49)).close().assemble().finalize().extrude(88))