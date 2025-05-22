import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,71))
r=w0.workplane(offset=-143/2).moveTo(-55,20).cylinder(143,45).union(w0.sketch().segment((80,-39),(93,-65)).segment((100,-59)).segment((86,-39)).close().assemble().finalize().extrude(-7))