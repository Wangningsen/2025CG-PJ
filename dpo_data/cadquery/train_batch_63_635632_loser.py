import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
r=w0.sketch().segment((-100,51),(-61,-17)).segment((-41,-5)).segment((-80,62)).close().assemble().reset().face(w0.sketch().segment((-30,-12),(-25,-13)).segment((-22,-9)).segment((-28,-3)).close().assemble()).finalize().extrude(-107).union(w0.sketch().push([(61,-23)]).circle(39).push([(64,-37)]).circle(6,mode='s').finalize().extrude(88))