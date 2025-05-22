import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-28))
r=w0.sketch().segment((-61,74),(-27,-43)).segment((-15,-38)).segment((-15,-73)).segment((-6,-73)).arc((5,-68),(18,-68)).segment((18,-100)).segment((23,-100)).segment((23,-27)).segment((61,-16)).segment((26,100)).close().assemble().finalize().extrude(56)