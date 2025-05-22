import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-76,-7),(-33,-69)).segment((76,7)).segment((33,69)).segment((28,66)).segment((28,65)).segment((27,65)).close().assemble().push([(-34,10)]).circle(5,mode='s').finalize().extrude(-200)