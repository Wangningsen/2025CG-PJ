import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().arc((45,-89),(-1,4),(93,-37)).arc((-73,69),(45,-89)).assemble().push([(39,59)]).rect(54,30,mode='s').finalize().extrude(-14)