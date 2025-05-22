import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-42))
w1=cq.Workplane('YZ',origin=(-10,0,0))
r=w0.sketch().arc((-36,52),(-26,-42),(67,-39)).segment((67,-40)).segment((100,-40)).segment((100,81)).segment((98,81)).segment((98,93)).segment((64,93)).segment((84,73)).segment((20,32)).segment((1,48)).segment((-24,65)).segment((-1,81)).segment((-36,81)).close().assemble().finalize().extrude(84).union(w1.sketch().push([(-85,-6)]).circle(8).circle(7,mode='s').finalize().extrude(-90))