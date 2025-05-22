import cadquery as cq
w0=cq.Workplane('YZ',origin=(-59,0,0))
r=w0.sketch().arc((-59,-68),(55,-58),(-17,23)).segment((-16,23)).segment((-17,-68)).close().assemble().finalize().extrude(46).union(w0.sketch().push([(14,84)]).circle(16).push([(9,90)]).rect(12,8,mode='s').finalize().extrude(118))