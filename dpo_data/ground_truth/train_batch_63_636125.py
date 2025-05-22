import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().segment((-100,-16),(-62,-62)).segment((32,16)).segment((30,19)).segment((100,19)).segment((100,37)).segment((15,37)).segment((-6,62)).close().assemble().push([(-34,0)]).circle(17,mode='s').finalize().extrude(-11)