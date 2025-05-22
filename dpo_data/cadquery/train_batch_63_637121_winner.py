import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,33))
r=w0.sketch().push([(-42,13)]).rect(70,18).reset().face(w0.sketch().arc((13,23),(35,54),(30,17)).arc((48,98),(13,23)).assemble()).finalize().extrude(-66).union(w0.workplane(offset=-66/2).moveTo(22,-58).cylinder(66,42))