import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,72))
r=w0.workplane(offset=-143/2).moveTo(-55,20).cylinder(143,45).union(w0.sketch().segment((80,-39),(94,-65)).arc((98,-46),(80,-39)).assemble().finalize().extrude(-7))