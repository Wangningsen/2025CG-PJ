import cadquery as cq
w0=cq.Workplane('YZ',origin=(82,0,0))
r=w0.workplane(offset=-164/2).moveTo(-60,-4.5).box(50,97,164).union(w0.sketch().arc((-3,-35),(85,-81),(32,2)).arc((-80,75),(-3,-35)).assemble().push([(-30.5,26.5)]).rect(33,99,mode='s').finalize().extrude(-100))