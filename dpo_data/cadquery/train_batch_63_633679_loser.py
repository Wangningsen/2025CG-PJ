import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,63))
r=w0.sketch().segment((-100,-23),(48,-91)).segment((66,-51)).segment((100,23)).segment((-48,91)).close().assemble().finalize().extrude(-127)