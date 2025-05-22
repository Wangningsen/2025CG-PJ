import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
w1=cq.Workplane('YZ',origin=(-38,0,0))
r=w0.workplane(offset=79/2).moveTo(-40,14.5).box(74,89,79).union(w0.sketch().push([(20,-37)]).circle(8).push([(19,-38)]).circle(3,mode='s').finalize().extrude(91)).union(w1.sketch().push([(-61,28.5)]).rect(78,97).push([(-67,14)]).circle(14,mode='s').finalize().extrude(-21))