import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().arc((-2,-80),(44,-48),(49,1)).close().assemble().finalize().extrude(87).union(w1.sketch().segment((-48,7),(-37,7)).arc((-19,-100),(10,4)).segment((10,7)).segment((80,7)).segment((80,36)).segment((13,36)).segment((13,66)).segment((-48,66)).close().assemble().push([(-18,-43)]).rect(82,76,mode='s').finalize().extrude(-37))