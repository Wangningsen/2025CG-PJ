import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-55))
r=w0.workplane(offset=17/2).moveTo(38,20).cylinder(17,62).union(w0.sketch().arc((-63,-70),(-6,-68),(-26,-13)).arc((-93,-9),(-63,-70)).assemble().finalize().extrude(110))