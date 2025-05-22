import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().segment((-100,-73),(-21,-73)).segment((9,-95)).segment((32,-62)).segment((73,-64)).segment((76,0)).segment((100,34)).segment((78,50)).segment((78,59)).segment((64,59)).segment((14,95)).segment((8,87)).segment((-100,87)).close().assemble().finalize().extrude(-18)