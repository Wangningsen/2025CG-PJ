import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,60,0))
r=w0.sketch().arc((-95,44),(-84,44),(-73,42)).arc((61,45),(9,-79)).arc((7,-90),(3,-100)).arc((78,56),(-95,44)).assemble().finalize().extrude(-120)