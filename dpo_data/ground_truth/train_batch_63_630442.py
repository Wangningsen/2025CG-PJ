import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
r=w0.workplane(offset=-28/2).moveTo(13,-82).cylinder(28,18).union(w0.workplane(offset=-25/2).moveTo(6,-5.5).box(94,11,25)).union(w0.sketch().arc((-17,57),(-26,-22),(19,44)).arc((18,98),(-17,57)).assemble().finalize().extrude(7))