import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().segment((-11,-97),(-4,-100)).segment((-2,-96)).arc((28,-74),(12,-40)).segment((11,-39)).arc((-27,-56),(-10,-93)).close().assemble().finalize().extrude(-15).union(w1.sketch().push([(5,24)]).circle(4).circle(3,mode='s').finalize().extrude(90))