import cadquery as cq
w0=cq.Workplane('YZ',origin=(53,0,0))
r=w0.sketch().arc((-98,33),(-99,29),(-96,32)).close().assemble().finalize().extrude(-107).union(w0.workplane(offset=-58/2).moveTo(39,0).cylinder(58,61))