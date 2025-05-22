import cadquery as cq
w0=cq.Workplane('YZ',origin=(3,0,0))
r=w0.sketch().segment((-84,-66),(-41,-100)).segment((84,66)).segment((36,100)).close().assemble().finalize().extrude(-6)