import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
r=w0.workplane(offset=-29/2).moveTo(13,-82).cylinder(29,18).union(w0.workplane(offset=-25/2).moveTo(5.5,-5.5).box(95,11,25)).union(w0.sketch().arc((-15,58),(-27,-20),(16,47)).arc((18,99),(-15,58)).assemble().finalize().extrude(7))