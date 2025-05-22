import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-34,0))
w1=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((41,-1),(91,-17)).segment((100,11)).segment((51,27)).arc((49,12),(41,-1)).assemble().finalize().extrude(68).union(w1.sketch().segment((-27,-25),(-24,-25)).arc((-16,-21),(-8,-20)).segment((-8,13)).segment((-27,13)).close().assemble().finalize().extrude(137))