import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
w1=cq.Workplane('XY',origin=(0,0,-48))
r=w0.workplane(offset=86/2).moveTo(-96,-72).cylinder(86,4).union(w1.sketch().segment((0,-36),(38,-36)).segment((38,-50)).arc((96,-9),(76,63)).segment((76,54)).segment((65,54)).segment((65,69)).segment((69,69)).arc((-14,49),(0,-36)).assemble().finalize().extrude(60))