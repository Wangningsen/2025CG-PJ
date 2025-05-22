import cadquery as cq
w0=cq.Workplane('YZ',origin=(-47,0,0))
w1=cq.Workplane('YZ',origin=(-28,0,0))
r=w0.sketch().arc((-44,26),(-59,5),(-37,-10)).arc((48,26),(-44,26)).assemble().push([(2,17)]).rect(34,68,mode='s').finalize().extrude(49).union(w0.workplane(offset=94/2).moveTo(-20,92).cylinder(94,8)).union(w1.workplane(offset=45/2).moveTo(22,-63).cylinder(45,37))