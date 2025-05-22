import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,31,0))
r=w0.sketch().segment((-46,-64),(-33,-64)).segment((-33,-54)).arc((-39,-55),(-46,-54)).close().assemble().finalize().extrude(-131).union(w0.sketch().segment((36,34),(46,34)).segment((46,64)).segment((36,54)).close().assemble().finalize().extrude(69))