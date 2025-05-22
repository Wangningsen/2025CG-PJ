import cadquery as cq
w0=cq.Workplane('YZ',origin=(41,0,0))
r=w0.sketch().segment((17,-95),(28,-100)).segment((77,9)).segment((67,14)).close().assemble().finalize().extrude(-130).union(w0.sketch().arc((-20,44),(-57,-44),(13,22)).segment((76,69)).segment((54,100)).close().assemble().finalize().extrude(48))