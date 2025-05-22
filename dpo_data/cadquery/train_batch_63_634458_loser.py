import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
w1=cq.Workplane('YZ',origin=(-20,0,0))
r=w0.workplane(offset=-111/2).moveTo(-8,-8).cylinder(111,17).union(w0.workplane(offset=-42/2).moveTo(-8,-8).cylinder(42,51)).union(w0.sketch().segment((-58,-25),(-43,-47)).segment((-17,-31)).arc((38,52),(-28,-21)).segment((-35,-10)).close().assemble().finalize().extrude(89)).union(w1.workplane(offset=118/2).moveTo(13,13).cylinder(118,46))