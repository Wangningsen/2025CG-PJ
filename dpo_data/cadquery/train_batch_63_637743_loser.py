import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,47,0))
w1=cq.Workplane('XY',origin=(0,0,8))
r=w0.sketch().push([(-49,-70.5)]).rect(52,59).push([(-49,-70)]).circle(9,mode='s').finalize().extrude(-102).union(w0.sketch().segment((-11,-44),(44,-68)).segment((52,-50)).segment((60,-50)).segment((60,-31)).segment((75,-1)).segment((52,10)).segment((75,93)).segment((53,100)).segment((27,14)).segment((13,18)).segment((9,1)).segment((1,1)).segment((1,-18)).close().assemble().finalize().extrude(8)).union(w1.workplane(offset=44/2).moveTo(-21,30.5).box(52,49,44))