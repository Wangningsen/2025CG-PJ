import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().segment((-63,-42),(-59,-42)).arc((-61,-40),(-63,-39)).close().assemble().finalize().extrude(-77).union(w0.workplane(offset=123/2).moveTo(12.5,9).box(101,66,123))