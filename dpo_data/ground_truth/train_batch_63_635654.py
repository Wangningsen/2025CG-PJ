import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().arc((-29,-72),(95,-36),(26,74)).arc((-95,36),(-29,-72)).assemble().push([(-20,8)]).circle(20,mode='s').push([(-11,59.5)]).rect(22,13,mode='s').finalize().extrude(9)