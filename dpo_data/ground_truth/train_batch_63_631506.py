import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-97))
r=w0.sketch().arc((-96,-40),(95,-15),(-77,69)).arc((-9,2),(-96,-40)).assemble().push([(18,-78.5)]).rect(8,15,mode='s').finalize().extrude(193)