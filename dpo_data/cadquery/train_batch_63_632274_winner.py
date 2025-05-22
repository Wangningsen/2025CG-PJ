import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,60,0))
w1=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().arc((-23,-37),(-38,-88),(14,-81)).segment((64,-81)).segment((64,-17)).segment((-23,-17)).close().assemble().finalize().extrude(-65).union(w0.sketch().push([(-34,-48)]).circle(44).push([(18,19)]).circle(17).finalize().extrude(-31)).union(w1.sketch().push([(-14.5,28.5)]).rect(91,97).push([(-14,28)]).circle(43,mode='s').finalize().extrude(89))