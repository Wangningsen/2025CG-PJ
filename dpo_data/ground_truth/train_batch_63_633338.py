import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,52))
r=w0.sketch().segment((-100,-89),(-51,-89)).segment((-51,-93)).segment((67,-93)).segment((67,-44)).segment((100,-26)).segment((34,93)).segment((-58,42)).segment((-38,7)).segment((-100,7)).close().assemble().finalize().extrude(-105)