import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
r=w0.sketch().segment((-100,51),(-61,-17)).segment((-42,-6)).segment((-81,62)).close().assemble().push([(-27,-8)]).circle(5).finalize().extrude(-106).union(w0.sketch().push([(61,-23)]).circle(39).push([(64,-37)]).circle(6,mode='s').finalize().extrude(89))