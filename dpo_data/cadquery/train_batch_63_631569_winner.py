import cadquery as cq
w0=cq.Workplane('YZ',origin=(23,0,0))
w1=cq.Workplane('XY',origin=(0,0,-99))
r=w0.sketch().push([(40,2)]).circle(25).push([(39.5,2)]).rect(9,34,mode='s').finalize().extrude(11).union(w1.sketch().segment((-100,-65),(100,-65)).segment((100,-12)).segment((15,-12)).segment((15,20)).segment((-14,20)).segment((-14,-12)).segment((-100,-12)).close().assemble().finalize().extrude(199))