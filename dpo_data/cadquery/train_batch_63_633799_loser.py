import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-65,0))
r=w0.sketch().arc((-18,29),(-13,25),(-8,24)).arc((-5,26),(-3,26)).arc((4,30),(8,40)).arc((-4,35),(-18,29)).assemble().finalize().extrude(-35).union(w0.sketch().segment((-15,-25),(-4,-40)).segment((18,-25)).close().assemble().finalize().extrude(165))