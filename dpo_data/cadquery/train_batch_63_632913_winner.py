import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,24,0))
r=w0.sketch().arc((43,-81),(97,-31),(68,37)).segment((68,-48)).segment((43,-48)).close().assemble().finalize().extrude(-48).union(w0.workplane(offset=-40/2).box(196,200,40))