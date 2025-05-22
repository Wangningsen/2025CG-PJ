import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().segment((-29,98),(27,34)).segment((29,36)).segment((-26,100)).close().assemble().finalize().extrude(-8).union(w0.sketch().segment((-19,-92),(5,-100)).segment((14,-74)).segment((-10,-66)).close().assemble().finalize().extrude(23))