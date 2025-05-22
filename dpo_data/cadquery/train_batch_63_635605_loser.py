import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
r=w0.sketch().arc((44,-17),(40,-68),(80,-39)).arc((85,13),(44,-17)).assemble().finalize().extrude(-78).union(w0.workplane(offset=-35/2).moveTo(-68,39).cylinder(35,32))