import cadquery as cq
w0=cq.Workplane('YZ',origin=(-80,0,0))
w1=cq.Workplane('YZ',origin=(-82,0,0))
r=w0.workplane(offset=104/2).moveTo(-35,64).box(22,72,104).union(w0.workplane(offset=162/2).moveTo(-34.5,64).box(51,22,162)).union(w1.sketch().arc((-43,-48),(45,-84),(2,2)).arc((-15,-29),(-43,-48)).assemble().finalize().extrude(24))