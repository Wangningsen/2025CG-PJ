import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().arc((-25,16),(73,14),(-9,83)).arc((-44,53),(-25,16)).assemble().finalize().extrude(13).union(w0.workplane(offset=16/2).moveTo(-6,-31).cylinder(16,69))