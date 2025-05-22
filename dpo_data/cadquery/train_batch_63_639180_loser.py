import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,57,0))
r=w0.sketch().segment((-41,-68),(-27,-100)).segment((16,-81)).segment((15,-80)).arc((15,99),(-41,-68)).assemble().finalize().extrude(-128).union(w0.sketch().segment((-50,-17),(-34,-17)).segment((-34,13)).segment((46,13)).segment((46,51)).segment((-46,51)).segment((-46,22)).segment((-50,22)).close().assemble().finalize().extrude(14))