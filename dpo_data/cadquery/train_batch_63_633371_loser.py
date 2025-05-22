import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().segment((-61,74),(-27,-43)).segment((-15,-38)).segment((-15,-73)).arc((2,-70),(18,-67)).segment((18,-100)).segment((23,-100)).segment((23,-28)).arc((25,-26),(27,-26)).segment((61,-16)).segment((27,100)).close().assemble().finalize().extrude(-56)