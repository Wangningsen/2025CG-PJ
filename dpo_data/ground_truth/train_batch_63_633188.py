import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
w1=cq.Workplane('XY',origin=(0,0,-40))
r=w0.sketch().arc((-3,-14),(-11,-32),(8,-35)).arc((93,26),(-3,-14)).assemble().finalize().extrude(-79).union(w0.workplane(offset=43/2).moveTo(-45.5,25.5).box(21,37,43)).union(w1.sketch().push([(-73.5,25)]).rect(53,58).push([(-66,41)]).rect(6,26,mode='s').finalize().extrude(122))