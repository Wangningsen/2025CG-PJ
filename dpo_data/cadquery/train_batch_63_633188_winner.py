import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
w1=cq.Workplane('XY',origin=(0,0,-40))
r=w0.sketch().arc((-4,-10),(-12,-30),(8,-35)).arc((95,21),(-4,-10)).assemble().finalize().extrude(-79).union(w0.workplane(offset=43/2).moveTo(-43,25).box(16,38,43)).union(w1.sketch().push([(-73.5,24.5)]).rect(53,59).push([(-66,44.5)]).rect(6,23,mode='s').finalize().extrude(122))