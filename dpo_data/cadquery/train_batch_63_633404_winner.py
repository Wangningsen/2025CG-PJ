import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
w1=cq.Workplane('XY',origin=(0,0,35))
r=w0.sketch().segment((-60,-62),(-6,-100)).segment((34,-48)).segment((-20,-8)).close().assemble().reset().face(w0.sketch().segment((-16,31),(12,-5)).segment((12,-6)).segment((13,-6)).segment((24,-23)).segment((60,4)).segment((42,28)).segment((42,100)).segment((-2,100)).segment((-2,39)).close().assemble()).finalize().extrude(15).union(w1.workplane(offset=-89/2).moveTo(-30,-15).cylinder(89,27))