import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.workplane(offset=50/2).moveTo(0,-24).cylinder(50,76).union(w1.sketch().arc((-65,6),(28,-95),(60,33)).arc((-17,99),(-65,6)).assemble().finalize().extrude(50))