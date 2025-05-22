import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
r=w0.sketch().arc((-14,88),(-96,24),(-5,-21)).arc((79,-86),(18,3)).arc((23,28),(18,53)).arc((26,90),(-14,88)).assemble().push([(-37,31)]).circle(43,mode='s').finalize().extrude(22)