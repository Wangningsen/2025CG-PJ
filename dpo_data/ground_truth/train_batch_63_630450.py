import cadquery as cq
w0=cq.Workplane('YZ',origin=(-35,0,0))
r=w0.sketch().segment((-100,-87),(100,-87)).segment((100,87)).segment((37,87)).arc((33,83),(27,79)).segment((27,55)).segment((-61,55)).segment((-61,87)).segment((-100,87)).close().assemble().push([(-69,25)]).circle(9,mode='s').finalize().extrude(70)