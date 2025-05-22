import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.workplane(offset=-117/2).moveTo(19,41).cylinder(117,29).union(w0.sketch().segment((-52,-26),(-24,-18)).arc((13,2),(14,-38)).segment((21,-41)).segment((-19,-66)).arc((37,18),(-52,-26)).assemble().finalize().extrude(83))