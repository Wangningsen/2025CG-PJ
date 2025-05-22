import cadquery as cq
w0=cq.Workplane('YZ',origin=(38,0,0))
r=w0.sketch().arc((-88,26),(-92,-11),(-58,-3)).arc((-28,6),(-15,33)).arc((-52,73),(-88,26)).assemble().finalize().extrude(-82).union(w0.workplane(offset=5/2).moveTo(49,-22).cylinder(5,51))