import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,15,0))
w1=cq.Workplane('XY',origin=(0,0,80))
r=w0.sketch().segment((-80,-34),(-64,-34)).segment((-64,-60)).segment((54,-60)).segment((54,60)).segment((-64,60)).segment((-64,48)).segment((-80,48)).close().assemble().push([(-5,0)]).circle(59,mode='s').finalize().extrude(85).union(w1.workplane(offset=-99/2).moveTo(-17,-88).cylinder(99,12))