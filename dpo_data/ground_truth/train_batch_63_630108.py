import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-60))
r=w0.sketch().push([(-77,17)]).circle(23).push([(52,0)]).circle(48).reset().face(w0.sketch().segment((28,-13),(39,-13)).arc((59,-30),(79,-13)).segment((90,-13)).segment((90,-7)).segment((79,-7)).arc((59,10),(39,-7)).segment((28,-7)).close().assemble(),mode='s').push([(37,-1)]).circle(2,mode='s').finalize().extrude(121)