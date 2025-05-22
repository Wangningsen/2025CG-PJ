import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.workplane(offset=-200/2).moveTo(-31.5,60).box(7,74,200).union(w0.sketch().segment((-82,-97),(82,-97)).segment((82,68)).segment((-82,68)).segment((-82,46)).segment((-70,46)).segment((-70,-81)).segment((-82,-81)).close().assemble().finalize().extrude(-155))