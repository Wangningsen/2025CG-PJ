import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-70))
r=w0.sketch().arc((-54,-78),(27,-88),(34,-3)).arc((36,82),(-47,84)).arc((32,-39),(-54,-78)).assemble().reset().face(w0.sketch().segment((-25,13),(18,-16)).segment((26,-3)).segment((-18,27)).close().assemble()).finalize().extrude(141)