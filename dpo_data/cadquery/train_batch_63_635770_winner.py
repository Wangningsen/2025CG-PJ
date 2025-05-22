import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().push([(0,-20)]).circle(50).circle(34,mode='s').finalize().extrude(18).union(w0.sketch().segment((-89,-34),(-68,-33)).segment((-68,-7)).segment((-66,-7)).segment((-66,-6)).segment((-64,-7)).segment((89,-7)).arc((-13,68),(-89,-34)).assemble().finalize().extrude(200))