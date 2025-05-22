import cadquery as cq
w0=cq.Workplane('YZ',origin=(-30,0,0))
w1=cq.Workplane('XY',origin=(0,0,38))
r=w0.workplane(offset=-34/2).moveTo(-24,-77).cylinder(34,23).union(w1.sketch().arc((55,47),(56,32),(55,16)).arc((62,24),(63,34)).arc((63,37),(62,39)).arc((60,43),(55,47)).assemble().finalize().extrude(62))