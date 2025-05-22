import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().push([(1,-21)]).circle(49).circle(33,mode='s').finalize().extrude(18).union(w0.sketch().segment((-89,-34),(-68,-34)).segment((-68,-7)).segment((90,-7)).arc((-13,68),(-89,-34)).assemble().finalize().extrude(200))