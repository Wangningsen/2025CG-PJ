import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
w1=cq.Workplane('YZ',origin=(-24,0,0))
r=w0.sketch().segment((-51,25),(1,25)).segment((1,37)).segment((10,32)).segment((10,25)).segment((23,25)).segment((34,18)).segment((41,31)).segment((45,37)).segment((43,38)).segment((51,49)).segment((28,62)).segment((28,68)).segment((16,68)).segment((6,74)).segment((1,68)).segment((1,100)).segment((-51,100)).close().assemble().finalize().extrude(-64).union(w1.sketch().push([(-80,14)]).circle(20).push([(-79.5,14)]).rect(11,24,mode='s').finalize().extrude(-5))