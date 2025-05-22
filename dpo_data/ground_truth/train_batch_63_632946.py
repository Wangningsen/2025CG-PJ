import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
w1=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.workplane(offset=79/2).moveTo(-40,14.5).box(74,89,79).union(w0.workplane(offset=91/2).moveTo(20,-37).cylinder(91,8)).union(w1.sketch().push([(-61,28.5)]).rect(78,97).push([(-82.5,31.5)]).rect(11,5,mode='s').push([(-67,10.5)]).rect(26,17,mode='s').finalize().extrude(21))