import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().push([(0,-1)]).circle(68).circle(52,mode='s').finalize().extrude(18).union(w0.sketch().segment((-89,-34),(-68,-34)).segment((-68,-7)).segment((89,-7)).arc((-11,69),(-89,-34)).assemble().finalize().extrude(200))