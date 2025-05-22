import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((4,92),(4,100)).arc((-21,-98),(36,93)).close().assemble().finalize().extrude(-43)