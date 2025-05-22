import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
r=w0.sketch().arc((-17,88),(-96,23),(-9,-22)).arc((80,-85),(18,4)).arc((22,39),(6,71)).arc((22,93),(-4,95)).arc((-11,96),(-17,88)).assemble().push([(-37,31)]).circle(43,mode='s').finalize().extrude(22)