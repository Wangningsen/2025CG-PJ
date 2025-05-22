import cadquery as cq
w0=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.workplane(offset=-82/2).cylinder(82,34).union(w0.sketch().rect(42,78).push([(-12,-3)]).rect(2,6,mode='s').push([(7,-3)]).circle(9,mode='s').finalize().extrude(118))