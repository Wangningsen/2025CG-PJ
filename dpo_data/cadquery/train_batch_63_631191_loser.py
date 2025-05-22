import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,60,0))
r=w0.sketch().segment((-95,44),(-74,42)).arc((67,34),(3,-79)).segment((4,-100)).arc((75,60),(-95,44)).assemble().finalize().extrude(-120)