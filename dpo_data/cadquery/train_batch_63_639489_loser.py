import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
w1=cq.Workplane('XY',origin=(0,0,6))
r=w0.sketch().segment((-49,42),(-19,42)).arc((-17,39),(-16,42)).segment((18,42)).arc((-16,46),(-49,42)).assemble().finalize().extrude(-25).union(w0.sketch().segment((-39,-92),(-2,-100)).segment((15,-29)).segment((-19,-21)).close().assemble().finalize().extrude(-2)).union(w1.sketch().arc((-49,42),(45,30),(2,100)).segment((2,42)).close().assemble().finalize().extrude(-21))