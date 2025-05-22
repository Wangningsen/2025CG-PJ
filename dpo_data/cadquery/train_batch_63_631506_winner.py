import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,96))
r=w0.sketch().arc((-96,-40),(95,-13),(-77,68)).arc((-9,4),(-96,-40)).assemble().push([(16,-78.5)]).rect(4,15,mode='s').finalize().extrude(-192)