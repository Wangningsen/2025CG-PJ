import cadquery as cq
w0=cq.Workplane('YZ',origin=(-75,0,0))
w1=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.sketch().push([(-27,-34)]).circle(66).push([(-23,-95)]).circle(3,mode='s').finalize().extrude(146).union(w0.workplane(offset=132/2).moveTo(42,49).cylinder(132,51)).union(w1.sketch().push([(-34,21)]).circle(54).push([(-53,50)]).circle(17,mode='s').finalize().extrude(93))