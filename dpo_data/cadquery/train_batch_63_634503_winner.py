import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-65))
r=w0.sketch().arc((31,45),(-33,-92),(52,31)).segment((52,100)).segment((31,100)).close().assemble().finalize().extrude(130)