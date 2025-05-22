import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-6,39),(48,33)).segment((48,35)).segment((-6,41)).close().assemble().finalize().extrude(-200).union(w0.sketch().arc((1,-45),(9,-27),(25,-36)).arc((-18,43),(1,-45)).assemble().finalize().extrude(-139))