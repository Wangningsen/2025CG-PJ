import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-65,0))
r=w0.sketch().arc((-18,29),(-14,26),(-9,25)).segment((-9,27)).segment((-6,27)).segment((-6,25)).arc((4,30),(8,40)).segment((3,38)).segment((6,35)).segment((5,33)).segment((1,37)).close().assemble().finalize().extrude(-35).union(w0.sketch().segment((-15,-25),(-4,-40)).segment((18,-25)).close().assemble().finalize().extrude(165))