import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().arc((-2,-80),(42,-51),(49,1)).close().assemble().finalize().extrude(87).union(w1.sketch().segment((-48,21),(-45,21)).arc((-42,15),(-37,11)).arc((-23,-100),(9,7)).segment((80,7)).segment((80,36)).segment((13,36)).segment((13,66)).segment((-48,66)).close().assemble().push([(-18,-43)]).rect(82,76,mode='s').finalize().extrude(-37))