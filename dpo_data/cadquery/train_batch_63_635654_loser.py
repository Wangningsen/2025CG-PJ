import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-5))
r=w0.sketch().arc((-33,-72),(95,-34),(15,74)).arc((-96,34),(-33,-72)).assemble().push([(-20,8)]).circle(20,mode='s').push([(-10,64)]).circle(5,mode='s').finalize().extrude(10)