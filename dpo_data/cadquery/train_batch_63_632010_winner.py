import cadquery as cq
w0=cq.Workplane('YZ',origin=(-80,0,0))
r=w0.sketch().segment((-13,8),(18,-35)).segment((54,-12)).segment((42,9)).segment((44,25)).segment((36,27)).segment((34,13)).segment((17,35)).close().assemble().push([(19,0)]).circle(14,mode='s').finalize().extrude(-20).union(w0.sketch().arc((-48,-1),(37,-9),(-45,17)).arc((-54,8),(-48,-1)).assemble().finalize().extrude(180))