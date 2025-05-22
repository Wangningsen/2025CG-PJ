import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.workplane(offset=-29/2).moveTo(13,-82).cylinder(29,18).union(w0.sketch().arc((-15,58),(-22,-23),(15,49)).arc((19,98),(-15,58)).assemble().finalize().extrude(7)).union(w1.workplane(offset=-25/2).moveTo(5.5,-5.5).box(95,11,25))