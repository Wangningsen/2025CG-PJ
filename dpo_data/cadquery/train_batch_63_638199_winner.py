import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().arc((-65,59),(0,-59),(65,59)).close().assemble().finalize().extrude(200)