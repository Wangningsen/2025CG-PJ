import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().push([(-28,87)]).rect(32,4).push([(53,62)]).circle(38).push([(41,66)]).circle(19,mode='s').finalize().extrude(-9).union(w0.sketch().push([(-83,-60)]).circle(8).push([(-23,-54)]).circle(46).push([(-69,-59.5)]).rect(2,13,mode='s').push([(-36.5,-44.5)]).rect(27,1,mode='s').finalize().extrude(73))