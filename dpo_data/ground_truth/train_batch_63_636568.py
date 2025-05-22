import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().arc((-96,-29),(84,54),(-70,-72)).arc((-60,-73),(-51,-71)).arc((74,48),(-88,-13)).arc((-93,-21),(-96,-29)).assemble().finalize().extrude(-20)