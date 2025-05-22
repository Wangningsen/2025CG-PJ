import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-99))
w1=cq.Workplane('YZ',origin=(34,0,0))
r=w0.sketch().segment((-100,-65),(100,-65)).segment((100,-12)).segment((15,-12)).segment((15,20)).segment((-14,20)).segment((-14,-12)).segment((-100,-12)).close().assemble().finalize().extrude(199).union(w1.sketch().push([(42,5)]).circle(23).circle(3,mode='s').finalize().extrude(-11))