import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
r=w0.sketch().arc((44,-17),(38,-67),(80,-39)).arc((87,11),(44,-17)).assemble().finalize().extrude(-77).union(w0.workplane(offset=-34/2).moveTo(-68,39).cylinder(34,32))