import cadquery as cq
w0=cq.Workplane('YZ',origin=(-38,0,0))
w1=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().push([(6,-10)]).circle(34).push([(41.5,63)]).rect(51,74).finalize().extrude(58).union(w0.sketch().push([(-2.5,-75.5)]).rect(1,49).push([(-2.5,-75)]).rect(1,2,mode='s').finalize().extrude(76)).union(w1.sketch().arc((-66,-12),(-65,-11),(-64,-11)).segment((-64,-10)).segment((-66,-10)).close().assemble().finalize().extrude(-3))