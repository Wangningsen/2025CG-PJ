import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,1,0))
r=w0.sketch().arc((-15,37),(-84,-73),(36,-17)).arc((87,77),(-15,37)).assemble().finalize().extrude(-60).union(w0.workplane(offset=58/2).moveTo(-26,60.5).box(64,3,58))