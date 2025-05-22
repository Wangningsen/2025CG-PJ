import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().segment((-90,-44),(-78,-44)).segment((-78,-56)).segment((-83,-56)).arc((80,60),(-90,-44)).assemble().push([(80.5,14.5)]).rect(19,17,mode='s').finalize().extrude(-28)