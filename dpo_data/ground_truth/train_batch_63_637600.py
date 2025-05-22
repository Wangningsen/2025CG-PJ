import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,73))
r=w0.sketch().push([(-17,46)]).circle(54).reset().face(w0.sketch().arc((49,-84),(49,-81),(52,-83)).arc((42,-67),(49,-84)).assemble()).finalize().extrude(-147).union(w0.workplane(offset=-146/2).moveTo(46,-75).cylinder(146,25))