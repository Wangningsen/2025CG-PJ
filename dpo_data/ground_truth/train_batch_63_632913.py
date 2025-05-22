import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,24,0))
r=w0.sketch().arc((25,-92),(92,-23),(66,68)).close().assemble().finalize().extrude(-48).union(w0.workplane(offset=-40/2).box(196,200,40))