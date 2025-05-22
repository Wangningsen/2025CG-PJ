import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().segment((5,-36),(18,-45)).segment((5,-64)).segment((25,-64)).arc((45,-45),(64,-38)).segment((64,-36)).close().assemble().finalize().extrude(-63).union(w0.workplane(offset=137/2).moveTo(-63,3.5).box(2,121,137))