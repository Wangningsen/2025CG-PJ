import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
r=w0.sketch().arc((-17,88),(-96,26),(-6,-20)).arc((81,-84),(15,2)).arc((23,27),(19,52)).arc((23,93),(-17,88)).assemble().push([(-37,31)]).circle(43,mode='s').finalize().extrude(-22)