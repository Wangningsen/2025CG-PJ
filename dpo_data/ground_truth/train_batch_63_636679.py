import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.workplane(offset=-200/2).moveTo(-31.5,58).box(7,78,200).union(w0.sketch().segment((-82,-97),(82,-97)).segment((82,68)).segment((-82,68)).segment((-82,46)).segment((-70,46)).segment((-70,-81)).segment((-82,-81)).close().assemble().push([(77.5,-64)]).rect(3,4,mode='s').finalize().extrude(-155))