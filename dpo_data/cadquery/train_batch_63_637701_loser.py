import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
r=w0.workplane(offset=-127/2).moveTo(-72,-80).cylinder(127,18).union(w0.sketch().arc((51,89),(61,67),(64,43)).arc((99,77),(51,89)).assemble().finalize().extrude(59)).union(w0.workplane(offset=64/2).moveTo(-72,-80.5).box(56,27,64))