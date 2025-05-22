import cadquery as cq
w0=cq.Workplane('YZ',origin=(-19,0,0))
w1=cq.Workplane('YZ',origin=(-5,0,0))
r=w0.sketch().push([(8,-69)]).circle(31).push([(27,7)]).circle(35).finalize().extrude(-52).union(w0.sketch().segment((-46,96),(-37,39)).segment((-9,43)).segment((-18,100)).close().assemble().push([(27,7)]).rect(76,44).push([(-1,8)]).circle(5,mode='s').finalize().extrude(-20)).union(w1.sketch().arc((-61,-49),(-55,-64),(-40,-72)).segment((-40,-61)).arc((-34,-61),(-29,-59)).segment((-29,-72)).arc((-9,-55),(-13,-30)).arc((-48,-11),(-61,-49)).assemble().finalize().extrude(76))