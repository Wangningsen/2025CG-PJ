import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.sketch().push([(-38,-51)]).circle(49).circle(3,mode='s').finalize().extrude(-21).union(w0.sketch().push([(-44,-41.5)]).rect(102,7).push([(69.5,55.5)]).rect(51,89).finalize().extrude(85)).union(w1.workplane(offset=105/2).moveTo(23,-72).cylinder(105,6))