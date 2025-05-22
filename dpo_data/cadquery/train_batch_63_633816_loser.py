import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().push([(-11,-47)]).circle(53).push([(23,-47)]).circle(16,mode='s').finalize().extrude(-26).union(w0.workplane(offset=17/2).moveTo(15,82).box(98,36,17))