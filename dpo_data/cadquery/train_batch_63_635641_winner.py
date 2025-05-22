import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
r=w0.sketch().arc((-13,-100),(13,0),(-13,100)).close().assemble().finalize().extrude(25)