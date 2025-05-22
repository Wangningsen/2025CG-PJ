import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
w1=cq.Workplane('YZ',origin=(-41,0,0))
r=w0.workplane(offset=-21/2).moveTo(-40,-51).cylinder(21,49).union(w0.sketch().push([(-44,-41.5)]).rect(102,7).push([(23,-72)]).circle(6).push([(69.5,55.5)]).rect(51,89).finalize().extrude(86)).union(w1.sketch().push([(23,-72)]).circle(6).push([(22.5,-72)]).rect(3,6,mode='s').finalize().extrude(103))