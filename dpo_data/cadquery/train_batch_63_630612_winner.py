import cadquery as cq
w0=cq.Workplane('YZ',origin=(-19,0,0))
w1=cq.Workplane('YZ',origin=(-5,0,0))
r=w0.sketch().push([(8,-69)]).circle(31).push([(27,7)]).circle(35).finalize().extrude(-52).union(w0.sketch().segment((-47,95),(-37,39)).segment((-8,44)).segment((-18,100)).close().assemble().finalize().extrude(-20)).union(w0.sketch().push([(27,7)]).rect(76,44).push([(57,18)]).circle(6,mode='s').finalize().extrude(-20)).union(w1.sketch().arc((-63,-45),(-58,-60),(-47,-70)).arc((-38,-62),(-31,-72)).arc((-8,-42),(-30,-11)).arc((-57,-17),(-63,-45)).assemble().finalize().extrude(76))