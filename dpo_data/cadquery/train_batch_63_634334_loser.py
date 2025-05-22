import cadquery as cq
w0=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.sketch().arc((-58,-68),(53,-63),(-16,23)).segment((-16,-68)).close().assemble().finalize().extrude(46).union(w0.sketch().push([(14,84)]).circle(16).push([(12,90)]).circle(4,mode='s').finalize().extrude(118))