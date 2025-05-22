import cadquery as cq
w0=cq.Workplane('YZ',origin=(-47,0,0))
w1=cq.Workplane('YZ',origin=(-28,0,0))
r=w0.sketch().arc((-44,27),(-58,1),(-30,-11)).arc((47,29),(-44,27)).assemble().push([(2,17)]).rect(34,68,mode='s').finalize().extrude(49).union(w0.sketch().push([(-20,92)]).circle(8).circle(6,mode='s').finalize().extrude(94)).union(w1.workplane(offset=45/2).moveTo(22,-63).cylinder(45,37))