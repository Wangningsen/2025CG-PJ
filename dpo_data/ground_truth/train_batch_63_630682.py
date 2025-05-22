import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().push([(-56,37)]).circle(41).reset().face(w0.sketch().segment((28,-84),(66,-91)).segment((97,84)).segment((56,91)).close().assemble()).push([(62,0)]).circle(16,mode='s').finalize().extrude(-200)