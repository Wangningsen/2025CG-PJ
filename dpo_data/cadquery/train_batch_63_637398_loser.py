import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-47,-86),(23,-86)).segment((23,-93)).segment((47,-93)).segment((47,-79)).arc((-29,0),(47,85)).segment((47,93)).segment((-47,93)).close().assemble().finalize().extrude(-200)