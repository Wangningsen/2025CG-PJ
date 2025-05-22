import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
w1=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.sketch().segment((-51,25),(1,25)).segment((1,37)).segment((10,32)).segment((10,25)).segment((22,25)).segment((34,18)).segment((51,49)).segment((29,61)).segment((29,68)).segment((17,68)).segment((5,75)).segment((1,68)).segment((1,100)).segment((-51,100)).close().assemble().finalize().extrude(-64).union(w1.sketch().push([(-80,14)]).circle(20).circle(9,mode='s').finalize().extrude(5))