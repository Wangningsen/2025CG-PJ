import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-20))
w1=cq.Workplane('ZX',origin=(0,15,0))
r=w0.sketch().push([(-17,-88)]).circle(12).push([(-17.5,-88)]).rect(17,12,mode='s').finalize().extrude(100).union(w1.sketch().segment((-80,-34),(-64,-34)).segment((-64,-60)).segment((54,-60)).segment((54,60)).segment((-64,60)).segment((-64,48)).segment((-80,48)).close().assemble().push([(-5,0)]).circle(59,mode='s').finalize().extrude(85))