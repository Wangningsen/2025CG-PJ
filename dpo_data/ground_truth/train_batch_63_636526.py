import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.sketch().arc((45,-89),(-6,5),(93,-37)).arc((-74,67),(45,-89)).assemble().push([(39,54.5)]).rect(54,39,mode='s').finalize().extrude(15)