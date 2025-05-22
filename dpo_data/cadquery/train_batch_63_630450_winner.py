import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.sketch().segment((-100,-87),(100,-87)).segment((100,87)).segment((34,87)).segment((27,76)).segment((27,55)).segment((-61,55)).segment((-61,87)).segment((-100,87)).close().assemble().push([(-70,25)]).circle(9,mode='s').finalize().extrude(-70)