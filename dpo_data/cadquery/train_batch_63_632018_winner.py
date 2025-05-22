import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
w1=cq.Workplane('ZX',origin=(0,-70,0))
r=w0.sketch().segment((-100,-24),(-93,-48)).segment((-31,-29)).segment((-38,-5)).close().assemble().finalize().extrude(12).union(w0.sketch().segment((-43,-35),(-29,-35)).segment((-43,-24)).close().assemble().push([(78,40)]).circle(22).push([(84,46)]).circle(2,mode='s').finalize().extrude(100)).union(w1.sketch().segment((-62,-93),(-56,-93)).arc((-42,-69),(-14,-57)).segment((-14,-37)).segment((-62,-37)).close().assemble().finalize().extrude(37))