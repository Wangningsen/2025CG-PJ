import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
r=w0.sketch().segment((54,-84),(100,-84)).segment((100,27)).segment((54,27)).arc((-100,5),(54,-18)).close().assemble().push([(21,10)]).circle(20,mode='s').finalize().extrude(12)