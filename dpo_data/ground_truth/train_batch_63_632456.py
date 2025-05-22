import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.workplane(offset=-117/2).moveTo(19,41).cylinder(117,29).union(w0.sketch().arc((-51,-27),(-39,-19),(-24,-18)).arc((19,-3),(-4,-42)).arc((-8,-56),(-19,-66)).arc((40,15),(-51,-27)).assemble().finalize().extrude(83))