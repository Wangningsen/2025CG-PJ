import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().arc((-60,21),(-44,11),(-27,9)).segment((2,21)).segment((3,21)).arc((16,54),(-2,89)).close().assemble().finalize().extrude(-112).union(w0.sketch().segment((16,-68),(46,-89)).segment((60,-69)).segment((30,-49)).close().assemble().finalize().extrude(88))