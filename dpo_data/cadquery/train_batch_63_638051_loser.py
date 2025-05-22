import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
r=w0.sketch().segment((-100,8),(-99,8)).arc((-44,-71),(47,-35)).segment((47,-84)).segment((100,-84)).segment((100,27)).segment((54,27)).arc((-24,84),(-99,19)).segment((-100,19)).close().assemble().push([(21,10)]).circle(20,mode='s').finalize().extrude(12)