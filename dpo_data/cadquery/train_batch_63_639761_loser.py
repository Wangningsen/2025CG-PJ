import cadquery as cq
w0=cq.Workplane('YZ',origin=(-63,0,0))
w1=cq.Workplane('XY',origin=(0,0,38))
r=w0.workplane(offset=34/2).moveTo(-24,-77).cylinder(34,23).union(w1.sketch().arc((55,16),(63,31),(55,47)).close().assemble().finalize().extrude(62))