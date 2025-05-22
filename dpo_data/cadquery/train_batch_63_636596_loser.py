import cadquery as cq
w0=cq.Workplane('YZ',origin=(41,0,0))
r=w0.sketch().segment((17,-95),(28,-100)).segment((77,9)).segment((67,14)).close().assemble().finalize().extrude(-130).union(w0.sketch().arc((-19,43),(-61,-40),(13,20)).segment((77,67)).segment((55,100)).close().assemble().finalize().extrude(48))