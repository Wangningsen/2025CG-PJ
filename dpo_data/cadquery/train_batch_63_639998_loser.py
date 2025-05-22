import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,11))
w1=cq.Workplane('YZ',origin=(-22,0,0))
r=w0.sketch().arc((-100,66),(-95,64),(-90,66)).close().assemble().finalize().extrude(20).union(w1.workplane(offset=122/2).moveTo(-42,-10.5).box(48,41,122))