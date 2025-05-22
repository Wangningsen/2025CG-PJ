import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('YZ',origin=(-11,0,0))
r=w0.workplane(offset=-64/2).moveTo(-34,8).cylinder(64,6).union(w0.sketch().segment((-100,-20),(-33,-20)).arc((100,-1),(-27,35)).segment((-100,35)).close().assemble().push([(31.5,0.5)]).rect(73,111,mode='s').finalize().extrude(84)).union(w1.sketch().segment((-39,-2),(-39,13)).arc((-40,6),(-39,-2)).assemble().finalize().extrude(34))