import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,54,0))
r=w0.sketch().arc((-100,5),(-95,-2),(-88,0)).segment((-88,2)).segment((-87,2)).segment((-87,0)).arc((-87,8),(-98,10)).arc((-98,7),(-100,5)).assemble().finalize().extrude(-108).union(w0.workplane(offset=-29/2).moveTo(55,0).cylinder(29,45))