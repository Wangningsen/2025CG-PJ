import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-10,0))
r=w0.sketch().arc((-96,-29),(79,62),(-69,-72)).arc((-41,-76),(-15,-85)).arc((56,69),(-87,-16)).arc((-93,-22),(-96,-29)).assemble().finalize().extrude(20)