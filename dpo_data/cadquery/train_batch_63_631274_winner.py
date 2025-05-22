import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().segment((23,67),(28,67)).segment((28,52)).arc((92,38),(54,-5)).segment((61,-6)).arc((96,56),(23,67)).assemble().finalize().extrude(-69).union(w0.workplane(offset=99/2).moveTo(-64,-46).cylinder(99,36))