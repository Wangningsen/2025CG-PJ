import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().arc((-52,15),(53,-15),(-49,23)).segment((-41,26)).segment((-36,11)).segment((-50,7)).close().assemble().finalize().extrude(200)