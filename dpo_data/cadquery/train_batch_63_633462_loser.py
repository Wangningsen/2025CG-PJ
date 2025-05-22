import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('XY',origin=(0,0,4))
r=w0.sketch().segment((-4,-44),(-4,-41)).arc((-28,22),(41,35)).segment((63,54)).arc((-61,18),(38,-70)).arc((29,-53),(26,-36)).segment((23,-46)).close().assemble().finalize().extrude(-77).union(w1.sketch().segment((-10,-29),(11,-29)).segment((11,-25)).segment((10,-25)).segment((10,-24)).segment((11,-24)).segment((11,100)).segment((-10,100)).close().assemble().push([(0,19)]).rect(4,2,mode='s').finalize().extrude(-57))