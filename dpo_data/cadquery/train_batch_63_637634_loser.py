import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.sketch().segment((-100,-73),(-24,-73)).segment((8,-95)).segment((29,-64)).segment((73,-64)).segment((73,-10)).segment((100,34)).segment((73,52)).segment((73,59)).segment((64,59)).segment((15,95)).segment((4,80)).segment((4,87)).segment((-100,87)).close().assemble().finalize().extrude(18)