import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().push([(64,70)]).circle(30).circle(19,mode='s').finalize().extrude(-22).union(w0.sketch().segment((-94,-53),(-82,-53)).segment((-71,-100)).segment((-32,-93)).segment((-41,-53)).segment((59,-53)).segment((59,-23)).arc((20,-16),(-9,13)).segment((-94,13)).close().assemble().finalize().extrude(2))