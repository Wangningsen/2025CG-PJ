import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().push([(-56,37)]).circle(41).reset().face(w0.sketch().segment((28,-85),(67,-91)).segment((97,84)).segment((56,91)).close().assemble()).push([(62,-1)]).circle(15,mode='s').finalize().extrude(200)