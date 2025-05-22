import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
w1=cq.Workplane('YZ',origin=(-30,0,0))
r=w0.sketch().arc((55,16),(63,32),(55,47)).close().assemble().finalize().extrude(62).union(w1.workplane(offset=-34/2).moveTo(-24,-77).cylinder(34,23))