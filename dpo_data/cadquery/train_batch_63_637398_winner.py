import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-47,-86),(21,-86)).segment((21,-93)).segment((47,-93)).segment((47,-79)).arc((-29,3),(47,85)).segment((47,93)).segment((-47,93)).close().assemble().finalize().extrude(200)