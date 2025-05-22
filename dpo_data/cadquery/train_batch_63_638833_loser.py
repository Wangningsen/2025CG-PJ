import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
w1=cq.Workplane('YZ',origin=(-14,0,0))
r=w0.sketch().arc((-18,-55),(-5,-44),(10,-54)).arc((-6,55),(-18,-55)).assemble().finalize().extrude(-97).union(w0.workplane(offset=69/2).moveTo(-7,0).cylinder(69,10)).union(w1.workplane(offset=76/2).moveTo(-4,-99).cylinder(76,1))