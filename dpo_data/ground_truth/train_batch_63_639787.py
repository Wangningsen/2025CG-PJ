import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.workplane(offset=-200/2).moveTo(10,0).cylinder(200,5).union(w0.sketch().segment((7,-25),(7,25)).arc((-15,0),(7,-25)).assemble().finalize().extrude(-80))