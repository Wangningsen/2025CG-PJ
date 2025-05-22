import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
r=w0.sketch().push([(-23.5,73.5)]).rect(41,53).push([(-24,74)]).circle(19,mode='s').reset().face(w0.sketch().segment((-35,-84),(15,-100)).segment((23,-78)).arc((35,-58),(36,-37)).segment((44,-13)).segment((-8,3)).segment((-16,-23)).arc((-27,-38),(-27,-57)).close().assemble()).finalize().extrude(62)