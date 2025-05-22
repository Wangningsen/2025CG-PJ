import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
w1=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.sketch().arc((-15,-55),(-4,-44),(6,-54)).arc((-6,55),(-15,-55)).assemble().finalize().extrude(-97).union(w0.workplane(offset=69/2).moveTo(-7,0).cylinder(69,10)).union(w1.workplane(offset=63/2).moveTo(-3,-99).cylinder(63,1))