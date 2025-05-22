import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('YZ',origin=(6,0,0))
r=w0.workplane(offset=16/2).moveTo(15,82).box(98,36,16).union(w1.sketch().push([(-11,-47)]).circle(53).push([(23,-47)]).circle(16,mode='s').finalize().extrude(-27))