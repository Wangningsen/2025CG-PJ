import cadquery as cq
w0=cq.Workplane('YZ',origin=(54,0,0))
r=w0.sketch().circle(99).push([(-26,51)]).circle(32,mode='s').push([(0,0)]).circle(3,mode='s').finalize().extrude(-115).union(w0.sketch().segment((-100,-18),(-66,-18)).arc((0,-67),(66,-18)).segment((100,-18)).segment((100,18)).segment((66,18)).arc((0,67),(-66,18)).segment((-100,18)).close().assemble().finalize().extrude(7))